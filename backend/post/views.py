from django.shortcuts import render
from .models import Post
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse

def index(request):
    allposts = Post.objects.all().order_by('-timestamp')
    return render(request, 'index.html', {"allposts":allposts})


def tweek(request):
    if request.method == "POST":
        post = request.POST["post"]
        try:
            Post.objects.create(post = post)
            messages.add_message(request,messages.SUCCESS,'Tweek Sent')
        except:
            Post.objects.create(post = post)
            messages.add_message(request,messages.SUCCESS,'Tweek Sent')
        
        return HttpResponseRedirect('/')
    else:
        return render(request,"index.html")
