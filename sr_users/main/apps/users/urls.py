from django.conf.urls import url
from . import views          

urlpatterns = [
    url(r'^$', views.index),
    url(r'add$', views.addform),
    url(r'new$', views.create),
    url(r'(?P<id>\d+)$', views.getperson),
    url(r'update$', views.update),
    url(r'changeuser$', views.changeuser)
]   