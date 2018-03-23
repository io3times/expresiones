from django.urls import path
from .import views

urlpatterns=[path('dic/<int:id>', views.primer, name='primer'),
             path('dic/', views.index, name='index'),]