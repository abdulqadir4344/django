from django.shortcuts import render 
from django.http import HttpResponse
from datetime import datetime
from training.models import Contact
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'index.html')

def contact(request):
    if request.method == "POST":
       name = request.POST.get('name')
       email = request.POST.get('email')
       phone = request.POST.get('phone')
       address = request.POST.get('address')
       desc = request.POST.get('desc')
       print(name,email,phone,address,desc)
       contact = Contact(name=name,email=email,phone=phone,address=address,desc=desc,date=datetime.today())
       contact.save()
       messages.success(request, 'your detailes has been submitted !')

    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

 