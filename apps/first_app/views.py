from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def index(request):
  return render(request, 'first_app/login.html')

# LOGIN, SIGN UP, AND LOGOUT
def user_home(request):
  logged_user = User.objects.get(id=request.session['id'])

  if request.method == 'POST':
    artist_uri = request.POST.get('uri')

    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='84741dfeaa7f422b86aae5963b573550', client_secret='4850b29725b74296b9074b63b2f56c68'))
    results = spotify.artist_top_tracks(artist_uri)
    final_result = results['tracks'][:10]

    return render(request, 'first_app/user_home.html', {"results": final_result}, )
  else:
    return render(request, 'first_app/user_home.html')
  

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

def logout(request):
  request.session.flush()
  return redirect('/')

