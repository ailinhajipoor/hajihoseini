from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def pride(request):
    return HttpResponse("pride")


def lam(request):
    return HttpResponse("lamburgini")


def say_home(request):
    return HttpResponse(""" 
    <html><head><head><body><pre>/ \</pre><pre>| |</p><pre>| |</pre>
    <input type='button' value='cleck me'/>
    </body>
    
    
    </html>
    
    """)
