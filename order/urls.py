from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('order/',views.order,name='order'),
    path('show/',views.show,name='show'),
    path('dispatcher/',views.dispatcher,name='dispatcher'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('editDispatch/<int:id>/',views.editDispatch,name='editDispatch'),
    path('delete/<int:id>/',views.delete,name='delete'),
]