from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.liste, name='url_liste'),   # Pas d'argument page précisé -> vaudra 1 par défaut
    url(r'^(?P<page>\d+)$', views.liste, name='url_liste'),
    #url(r'^nouveau$', views.nouveau, name='url_nouveau'),
    url(r'^nouveau$', views.URLCreate.as_view(), name='url_nouveau'),
    #url(r'^edition/(?P<pk>\d)$', views.URLUpdate.as_view(), name='url_update'),
    # (?P<code>\w{6}) capturera 6 caractères alphanumériques.
    url(r'^(?P<code>\w{6})/$', views.redirection, name='url_redirection'),
    url(r'^edition/(?P<code>\w{6})$', views.URLUpdate.as_view(), name='url_update'),
    url(r'^supprimer/(?P<code>\w{6})$', views.URLDelete.as_view(), name='url_delete'),
    # …
]