from django.http import HttpResponse
from django.shortcuts import render
from service.models import Service
def aboutus(request):
    data={
         'title':'Edgecut'
    }
    return render(request,"about.html",data)

def user_registration(request):
    return render(request,"Contact.html")
def saveEnquiry(request):
    n=''
    if request.method=="POST":
        name=request.POST.get('name')
        name=request.POST.get('email')
        name=request.POST.get('phone')
        name=request.POST.get('message')
        data=Service(title=name,description=email,date=phone,status=message)
        en.save()
        n='data inserted'

    return render(request,"Contact.html",{'n':n})

def login(request):
    return render(request,"blog.html")
def login(request):
    return render(request,"blog.html")
def saveEnquiry1(request):
    n=''
    if request.method=="POST":
        name=request.POST.get('email')
        name=request.POST.get('password')
        data=Service(title=email,description=password)
        en.save()
        n='data inserted'

    return render(request,"blod.html",{'n':n})


def task_creation(request):
    return render(request,"furniture.html")

def list(request):
    return render(request,"index.html")

def details(request):
    return render(request,"Home.html")

def update(request):
    return render(request,"title.html")

def task_deletion(request):
    return render(request,"des.html")

    