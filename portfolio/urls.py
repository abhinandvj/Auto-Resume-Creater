from django.urls import path
from .import views

urlpatterns = [
    path('',views.id1),
    path('home/',views.id2)
]