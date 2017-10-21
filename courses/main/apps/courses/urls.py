from django.conf.urls import url
from . import views        
urlpatterns = [
    url(r'^$', views.index),
    url(r'add$', views.addclass),
    url(r'remove/(?P<id>\d+)$', views.removecourse),
    url(r'destroy$', views.destroy)  
]