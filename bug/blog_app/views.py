from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth import login
from django.urls import reverse
from django.contrib import messages
from .models import Wiadomosc

# Create your views here.
def home(request):
    # if request.method == "POST":
    #     logout(request)
    #     redirect('blog_app:home')
    #
    # return render(
    #     request,
    #     'blog_app/home.html',
    # )
    return render(request, 'blog_app/home.html')


# def login_view(request):
#     if request.method == "POST":
#         data = request.POST
#         user = authenticate(
#             username=data.get('user'),
#             password=data.get('password')
#         )
#         if user:
#             login(request, user=user)
#         return redirect('blog_app:home')
#     return render(
#         request,
#         "blog_app/login.html"
#     )


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


def wiadomosci(request):
    """Dodawanie i wyświetlanie wiadomości"""
    if request.method == 'POST':
        tekst = request.POST.get('tekst', '')
        if not 0 < len(tekst) <= 250:
            messages.error(
                request,
                "Wiadomość nie może być pusta, może mieć maks. 250 znaków!")
        else:
            wiadomosc = Wiadomosc(
                tekst=tekst,
                author=request.user)
            wiadomosc.save()
            return redirect(reverse('blog_app:wiadomosci'))

    wiadomosci = Wiadomosc.objects.all()
    kontekst = {'wiadomosci': wiadomosci}
    return render(request, 'blog_app/wiadomosci.html', kontekst)

