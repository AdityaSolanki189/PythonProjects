from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib import messages

def index(requests):
    return render(requests, 'index.html')


def about(requests):
    return render(requests, 'about.html')
  

def contact(requests):
    if requests.method == "POST":
        name = requests.POST.get('name')
        email = requests.POST.get('email')
        phone = requests.POST.get('phone')
        desc = requests.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(requests, 'Thanks for Contacting Us. Your message has been sent.')
    return render(requests, 'contact.html')