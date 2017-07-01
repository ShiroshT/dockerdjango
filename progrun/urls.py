from django.conf.urls import include, url
from progrun import views

urlpatterns =[
        url(r'^$', views.index, name='index'),
]