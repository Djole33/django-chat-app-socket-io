from django.urls import path
from . import views

urlpatterns = [
   path('rooms/', views.index, name="index"),
   path('rooms/<slug:slug>/', views.chatroom, name="chatroom"),
]
