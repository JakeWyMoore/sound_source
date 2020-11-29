from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index),
  url(r'^login$', views.login),
  url(r'^sign_up_page$', views.sign_up_page),
  url(r'^sign_up$', views.sign_up),
  url(r'^logout$', views.logout),
  url(r'^user_home$', views.user_home),
  url(r'^edit_profile_page$', views.edit_profile_page),
  url(r'^edit_profile$', views.edit_profile),
  url(r'^image$', views.image),

  url(r'^None$', views.none),

]