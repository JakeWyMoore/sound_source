from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def index(request):
  return render(request, 'first_app/login.html')

# LOGIN, SIGN UP, AND LOGOUT
def user_home(request):
  the_user = User.objects.get(id=request.session['id'])


  if request.method == 'POST':
    artist_uri = request.POST.get('uri')

    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='84741dfeaa7f422b86aae5963b573550', client_secret='4850b29725b74296b9074b63b2f56c68'))
    results = spotify.artist_top_tracks(artist_uri)
    final_result = results['tracks'][:10]

    context = {
      'user': the_user,
      'results': final_result,
    }

    return render(request, 'first_app/user_home.html', context)
  else:
    context = {
      'user': the_user,
    }

    return render(request, 'first_app/user_home.html', context)
  
########### LOGIN
def login(request):
  logged_user = User.objects.filter(email=request.POST['email'])

  if logged_user[0]:
    if logged_user[0].password == request.POST['password']:
      request.session['user'] = logged_user[0].email
      request.session['id'] = logged_user[0].id

      print('User in Session: ', logged_user)

      return redirect('/user_home')

  else:
    print('Error')
    return redirect('/')

########### SIGN UP
def sign_up_page(request):
  return render(request, 'first_app/sign_up.html')

def sign_up(request):
  errors = User.objects.basic_validator(request.POST)

  if len(errors) > 0:
    for key, value in errors. items():
      messages.error(request, value)
    return redirect('/sign_up_page')

  if request.POST['password'] == request.POST['confirm_password']:
    new_user = User.objects.create(email=request.POST['email'], password=request.POST['password'], nickname=request.POST['nickname'])
    print('User Created')

    request.session['user'] = new_user.email
    request.session['id'] = new_user.id

    return redirect('/user_home')
  
  else:
    return redirect('/')

########### EDIT 
def edit_profile_page(request):
  logged_user = User.objects.get(id=request.session['id'])

  context = {
    'user': logged_user,
  }

  return render(request, 'first_app/edit_profile.html', context)

def edit_profile(request):
  the_user = User.objects.get(id = request.session['id'])

  if request.POST['password'] == request.POST['confirm_password']:
    the_user.email = request.POST['email']
    the_user.password = request.POST['password']
    the_user.nickname = request.POST['nickname']
    the_user.save()
  
  else:
    return redirect('/edit_profile_page')
  
  return redirect('/edit_profile_page')

def image(request):
  the_user = User.objects.get(id = request.session['id'])

  the_user.image = request.POST['image']
  the_user.save()

  return redirect('/edit_profile_page')

def logout(request):
  request.session.flush()
  return redirect('/')

def none(request):
  return render(request, 'first_app/error.html')

