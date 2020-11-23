from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index),
  url(r'^login$', views.login),
  url(r'^sign_up_page$', views.sign_up_page),
  url(r'^sign_up$', views.sign_up),
  url(r'^logout$', views.logout),
  url(r'^user_home$', views.user_home),

  url(r'^None$', views.none),

]