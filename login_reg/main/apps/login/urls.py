from django.conf.urls import url
from . import views           

urlpatterns = [
    url(r'^$', views.index),
    url(r'useradd$', views.useradd),
    #url(r'success$', views.logsuccess),
    url(r'userlogin$', views.userlogin),  
]