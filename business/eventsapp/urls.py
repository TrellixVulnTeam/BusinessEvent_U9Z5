from django.urls import path
from.import views


urlpatterns=[
path('', views.home,name='home'),

path('blog', views.blog,name='blog'),

path('register', views.register,name='register'),

path('profile', views.profile,name='profile'),
path('login', views.login,name='login'),
path('event1', views.event1,name='event1'),
path('logout', views.logout,name='logout'),
path('sample', views.sample,name='sample'),]