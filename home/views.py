from django.shortcuts import render, redirect
from .models import Favorite, Contactame
from django.contrib import messages

# Create your views here.
def Home(request):
    favorite = Favorite.objects.all().filter(is_available=True) 
        
    return render(request, 'pages/home.html', {
        'favorite': favorite,
    })


def register_contact(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    
    contact = Contactame.objects.create(name=name, email=email, phone=phone, message=message)
    
    messages.success(request, message="Me has contactado con exito!!! Te respondere a la brevedad. 😃")
    
    return redirect('/')