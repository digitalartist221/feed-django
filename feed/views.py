from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from feed.models import Message

# Create your views here.


def index(request):
    
    if request.method == "POST":
        content = request.POST.get('content')
        user = request.user
        
        Message.objects.create(content=content, user=user)
    
    context = {
    }
    
    context["messages"] = Message.objects.order_by('created_at')
    
    return render(request, 'index.html', context=context)


def details(request, id):
    if request.method == "POST":
        content = request.POST.get('content')
        user = request.user
        
        Message.objects.create(content=content, user=user, response_to=Message.objects.get(id=id))
    
    
    context = {
    }
    context["message"]  = Message.objects.get(id=id)
    context["comments"]  = Message.objects.filter(response_to=id)
    return render(request, 'detail.html', context=context)