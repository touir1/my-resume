from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("""
        <h1>Welcome to my website ! </h1>
        <p>it's only a test of HttpResponse from the views.py file</p>
        <b>It's from the home :D</b>
    """)