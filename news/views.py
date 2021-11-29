from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect

# Create your views here.
from news.models import news


def home(request):
    vartha=news.objects.all().order_by('-date')
    return render(request,"home.html",{'n':vartha})


def new(request):
    if request.method=="POST":
        image = request.FILES['image']
        user=request.user.id
        reporter = request.POST['reporter']
        category = request.POST['category']
        place = request.POST['place']
        description = request.POST['description']
        s=news(image=image,category=category,place=place,description=description,reporter=reporter,user_id=user)
        s.save()
        return redirect('/')
    return render(request,"news.html")

def detail(request,id):
    obj=news.objects.get(id=id)
    return render(request,"detailed.html",{'news':obj})

def search(request):
    ne=None
    query=None
    if 'q' in request.GET:
        query = request.GET.get('q')
        ne = news.objects.all().filter(Q(place__contains=query)|Q(category__contains=query))
    return render(request,"search.html",{'qr':query,'n':ne})

def new1(request):
    user = request.user.id
    print(user)
    obj=news.objects.filter(user_id=user).order_by('-date')
    return render(request,"mine.html",{'obj':obj})

def delete(request,id):
    ct = news.objects.get(id=id)
    ct.delete()
    return redirect('new1')
