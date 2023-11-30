from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    heading = " <html> <body> <h1>Welcome to Django First Project! 😘🥳🥳🥳</h1> <h2>M. Hamza Javed</h2> </body> </html> "
    return HttpResponse(heading)
