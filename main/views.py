from django.shortcuts import render, get_object_or_404
from .models import ChatRoom

# Create your views here.

def index(request):
    chatrooms = ChatRoom.objects.all()
    return render(request, 'main/index.html', {'chatrooms': chatrooms})

def chatroom(request, slug):
    chatroom = get_object_or_404(ChatRoom, slug=slug)
    return render(request, 'main/chatroom.html', {
        'chatroom': chatroom,
        'slug': slug,
        'main': {'slug': slug}
    })
