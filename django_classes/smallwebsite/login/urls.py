from django.contrib import admin
from django.urls import path
from login import views

urlpatterns = [
    path('',views.login),
    path('home/',views.home,name='home'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/',views.delete,name='delete')
]