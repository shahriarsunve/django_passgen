from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request,'generator/home.html')

def password(request):
    charecters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('Uppercase'):
        charecters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('Number'):
        charecters.extend(list('0123456789'))
    if request.GET.get('Special'):
        charecters.extend(list('*&%$#@'))

    length =int(request.GET.get('length',12))

    thepass = ''
    for x in range(length):
        thepass+= random.choice(charecters)

    return render(request,'generator/password.html',{'password':thepass})

def about(request):
    return render(request,'generator/about.html')
