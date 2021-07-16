from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create', views.create),
    path('<int:number>', views.show),
    path('<int:number>/edit', views.edit),
    path('<int:number>/delete', views.destroy),
    ]