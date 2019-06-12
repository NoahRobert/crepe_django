from django.shortcuts import render

# Create your views here.
import random
import string


def generer(nb_caracteres):
    caracteres = string.ascii_letters + string.digits
    aleatoire = [random.choice(caracteres) for _ in range(nb_caracteres)]

    return ''.join(aleatoire)

from .forms import ContactForm
from .models import MiniURL
def creation_miniurl(request):
    sauvegarde = False
    form = ContactForm(request.POST or None, request.FILES)
    # je peux mettre en commentaire, dans un formulaire la methode view est executee 2 fois
    # la deuxieme fois avec url du template

    if form.is_valid():
        murl = MiniURL()
        murl.url_longue = form.cleaned_data["url"]
        murl.pseudo_createur = form.cleaned_data["pseudo"]
        murl.code_raccourci = generer(5)
        murl.save()
        sauvegarde = True


    return render(request, 'mini_url/creation_url.html', {
        'form': form,
        'sauvegarde': sauvegarde
    })

def voir_urls(request):

    return render(
        request,
        'mini_url/voir_urls.html',
        {'urls': MiniURL.objects.all()}
    )


from django.shortcuts import redirect


def redirection(request,code):

    try:
        mini = MiniURL.objects.get(code_raccourci=code)
        mini.nombre_acces = mini.nombre_acces + 1
        mini.save()
    except MiniURL.DoesNotExist:
        mini = None
        return HttpResponse("Ce code nexiste pas {} ".format(code)
        )

    #response = redirect('/redirect-success/'
    response = redirect(mini.url_longue)
    return response
