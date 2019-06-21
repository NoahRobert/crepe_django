from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login

from django import forms
class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

def connexion(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'toto_login.html', locals())

from django.contrib.auth import logout
from django.shortcuts import render
#from django.core.urlresolvers import reverse
from django.urls import reverse
from django.shortcuts import redirect

def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))