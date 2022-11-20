from django.urls import path
from .import views

urlpatterns = [
    path('',views.id1),
    path('resume/',views.id2)
]