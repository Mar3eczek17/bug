from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth import login
from django.urls import reverse
from django.contrib import messages

from .models import Wiadomosc
from django.utils import timezone


# Create your views here.
from django.views.generic import CreateView, UpdateView


def home(request):
    return render(request, 'blog_app/home.html')


def login_view(request):
    """Logowanie użytkownika"""
    from django.contrib.auth.forms import AuthenticationForm
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, "Zostałeś zalogowany!")
            return redirect(reverse('blog_app:home'))

    kontekst = {'form': AuthenticationForm()}
    return render(request, 'blog_app/login.html', kontekst)


def zaloguj(request):
    from django.contrib.auth.forms import AuthenticationForm
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, "Zostałeś zalogowany!")
            return redirect(reverse('blog_app:home'))

    kontekst = {'form': AuthenticationForm()}
    return render(request, 'blog_app/zaloguj.html', kontekst)


def wyloguj(request):
    """Wylogowanie użytkownika"""
    logout(request)
    messages.info(request, "Zostałeś wylogowany!")
    return redirect(reverse('blog_app:home'))


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('blog_app:login-view')
    form = UserCreationForm()
    return render(
        request,
        'blog_app/register.html',
        context={
            'form': form,
        }
    )


class DodajWiadomosc(CreateView):
    model = Wiadomosc
    fields = ['tekst', 'created_date']
    context_object_name = 'wiadomosci'
    success_url = '/blog_app/dodaj'

    def get_initial(self):
        initial = super(DodajWiadomosc, self).get_initial()
        initial['created_date'] = timezone.now()
        return initial

    def get_context_data(self, **kwargs):
        context = super(DodajWiadomosc, self).get_context_data(**kwargs)
        context['wiadomosci'] = Wiadomosc.objects.all()
        return context

    def form_valid(self, form):
        wiadomosc = form.save(commit=False)
        wiadomosc.autor = self.request.user
        wiadomosc.save()
        messages.success(self.request, "Dodano wiadomość!")
        return super(DodajWiadomosc, self).form_valid(form)


class EdytujWiadomosc(UpdateView):
    model = Wiadomosc
    from .forms import EdytujWiadomoscForm
    form_class = EdytujWiadomoscForm
    context_object_name = 'wiadomosci'
    template_name = 'blog_app/wiadomosc_form.html'
    success_url = '/blog_app/wiadomosci'

    def get_context_data(self, **kwargs):
        context = super(EdytujWiadomosc, self).get_context_data(**kwargs)
        context['wiadomosci'] = Wiadomosc.objects.filter(
            author=self.request.user)
        return context

    def get_object(self, queryset=None):
        wiadomosc = Wiadomosc.objects.get(id=self.kwargs['pk'])
        return wiadomosc