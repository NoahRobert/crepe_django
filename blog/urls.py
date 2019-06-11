from django.urls import path
from . import views

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
