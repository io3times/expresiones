from django.urls import path
from .import views

urlpatterns=[path('dic/<int:id>', views.index, name='index')]