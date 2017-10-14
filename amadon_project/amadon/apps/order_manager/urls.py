from django.conf.urls import url
from . import views           
urlpatterns = [
    url(r'^$', views.index),
    url(r'^item_1$', views.item_1),
    url(r'^item_2$', views.item_2),
    url(r'^item_3$', views.item_3),
    url(r'^item_4$', views.item_4),
    url(r'^back$', views.back),
    url(r'^gotocheckout$', views.checkout)
]