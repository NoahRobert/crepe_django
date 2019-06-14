from django.urls import path

from django.conf.urls import  url, include
#from django.views.generic import ListView

from . import views
#from .models import Article

urlpatterns = [
    # Nous allons réécrire l'URL de l'accueil
    #url(r'^$', ListView.as_view(model=Article,
    #    context_object_name="derniers_articles",
    #    template_name="blog/accueil.html")),
    # Via la fonction as_view, comme vu tout à l'heure
    url(r'^$', views.ListeArticles.as_view(), name="blog_liste"),
    #url(r'^categorie/(\d+)$', views.ListeArticles.as_view(), name='blog_categorie'),
    url(r'categorie/(?P<id>\d+)', views.ListeArticles.as_view(), name='blog_categorie'),
    # Et nous avons toujours nos autres pages…
    #url(r'^article/(?P<id>\d+)$', views.lire),
    #url(r'^(?P<page>\d+)$', views.archives),
    #url(r'^categorie/(?P<slug>.+)$', views.voir_categorie),
    path('article/<int:id>', views.lire, name='lire'),
    url(r'^categorie/(\w+)$', views.ListeArticles.as_view()),
    url(r'^article/(?P<pk>\d+)$', views.LireArticle.as_view(), name='blog_lire'),
]

"""
from django.views.generic import ListView
urlpatterns = [
    #path('accueil', views.home),
    #path('article/<id_article>', views.view_article),
    #path('date', views.date_actuelle),
    #path('addition/<int:nombre1>/<int:nombre2>', views.addition),
    path('', views.accueil, name='accueil'),
    path('article/<int:id>', views.lire, name='lire'),
    path('contact/', views.contact, name='contact'),
    path('test/', views.test_article, name='test_article'),
    path('nouveau-contact/', views.nouveau_contact, name='nouveau_contact'),
    path('voir-contacts/', views.voir_contacts),
#    path('article/<int:id>-<slug:slug>', views.lire, name='lire')
]
"""