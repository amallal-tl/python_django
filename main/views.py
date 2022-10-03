from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
	return HttpResponse("<h1>This is the first response</h1>")

def index2(response):
	return HttpResponse("<h1>This is the second response</h1>")
