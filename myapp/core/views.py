from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
   text = """<h1>our test of mind blowing home page</h1>"""
   return HttpResponse(text)
