from django.urls import path
from . import views

#app_name = 'mini_url'
# Apres oblige de faire rajouter ci dessous le app_name:name sinon Reverse for 'creation' not found. 'creation' is not a valid view function or pattern name.
#<a href="{% url 'mini_url:creation' %}"> qund je precise lapp</a>
urlpatterns = [
    path('voir-urls/', views.voir_urls, name='voir-urls'),
    path('nouveau-url/', views.creation_miniurl, name='creation'),
    path('m/<code>', views.redirection, name='redirection'),
#    path('article/<int:id>-<slug:slug>', views.lire, name='lire')
]