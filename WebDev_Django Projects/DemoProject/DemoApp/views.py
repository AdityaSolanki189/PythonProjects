from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hi(request):
    return HttpResponse('<h1>THIS IS MY HOMEPAGE!</h1>\n<h2>This is next line</h2>')
