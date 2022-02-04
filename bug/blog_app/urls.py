from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import path, reverse_lazy
from . import views
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth import views as auth_views
from django.views.generic import ListView

from .models import Wiadomosc

app_name = 'blog_app'  # przestrzeń nazw aplikacji

urlpatterns = [
    path('', views.home, name='home'),
    path('login-view/', views.login_view, name='login-view'),
    path('wyloguj/', views.wyloguj, name='wyloguj'),
    path('register/', views.register, name='register'),
    # path('wiadomosci/', views.wiadomosci, name='wiadomosci'),
    path('rejestruj/', CreateView.as_view(template_name='blog_app/rejestruj.html',
                                           form_class=UserCreationForm,
                                           success_url='/'),
         name='rejestruj'),
    path('zaloguj/', views.zaloguj, name='zaloguj'),
    path('wyloguj/', auth_views.LogoutView.as_view(),
         {'next_page': reverse_lazy('blog_app:home')},
         name='wyloguj'),
    path('wiadomosci/', login_required(
        ListView.as_view(
            model=Wiadomosc,
            context_object_name='wiadomosci',
            paginate_by=2)),
         name='wiadomosci'),
    path('dodaj/', login_required(
        views.DodajWiadomosc.as_view(),
        login_url='/loguj'),
         name='dodaj'),
    path('edytuj/<int:pk>/', login_required(
        views.EdytujWiadomosc.as_view(),
        login_url='/loguj'),
        name='edytuj'),
    # path('edytuj/<int:pk>/', views.EdytujWiadomosc.as_view, name='edytuj'),
    path('usun/<int:pk>/', login_required(
        DeleteView.as_view(
            model=Wiadomosc,
            template_name='blog_app/wiadomosc_usun.html',
            success_url='/blog_app/wiadomosci'),
        login_url='/loguj'),
        name='usun'),

]
