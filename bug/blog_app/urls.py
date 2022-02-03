from django.urls import path
from . import views

app_name = 'blog_app'  # przestrzeń nazw aplikacji

urlpatterns = [
    path('', views.home, name='home'),
    path('login-view/', views.login_view, name='login-view'),
    path('wyloguj/', views.wyloguj, name='wyloguj'),
    path('register/', views.register, name='register'),
    path('wiadomosci/', views.wiadomosci, name='wiadomosci'),
]
