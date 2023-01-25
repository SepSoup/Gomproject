from django.shortcuts import render
from .models import User, Object
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse

def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print("not none")
            return HttpResponseRedirect(reverse("found"))
            
        else:
            print("none")
            return render(request, "backend/Entrance.html")
    else:
        print("don't even try")
        return render(request, "backend/Entrance.html")

def foundreg(request):
    if request.method == 'POST':

        title = request.POST['firstinput']
        description = request.POST['secondinput']

        temp = Object(name=title, 
        details=description, 
        found=True, 
        user=User.objects.get(id=request.user.id))

        temp.save()
        return HttpResponseRedirect(reverse('info', kwargs={"obj_id":temp.id}))

    else:
        return render(request, "backend/RigesterFoundPage.html")

def found(request):
    objects = Object.objects.filter(found=True).reverse()
            
    return render(request, "backend/FoundPage.html", {
        "objects":objects
    })

def lostreg(request):
    if request.method == 'POST':
        title = request.POST['firstinput']
        description = request.POST['secondinput']

        temp = Object(name=title, 
        details=description, 
        found=False, 
        user=User.objects.get(id=request.user.id))

        temp.save()
        return HttpResponseRedirect(reverse('info', kwargs={"obj_id":temp.id}))

    else:
        return render(request, "backend/RigesterLostPage.html")

def lost(request):
    objects = Object.objects.filter(found=False).reverse()

    return render(request, "backend/LostPage.html", {
        "objects":objects
    })

def info(request, obj_id):
    obj = Object.objects.get(id=obj_id)

    return render(request, "backend/Found&Lost_Info_Page.html", {
        "title":obj.name,
        "description":obj.details
    })