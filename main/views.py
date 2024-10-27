from django.shortcuts import render
from .models import ChatRoom

# Create your views here.

def index(request):
    chatrooms = ChatRoom.objects.all()
    return render(request, 'main/index.html', {'chatrooms': chatrooms})

def chatroom(request, slug):
    chatroom = ChatRoom.objects.get(slug=slug)
    return render(request, 'main/chatroom.html', {'chatroom': chatroom})
