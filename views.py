from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
import random
import smtplib as s
from requests import request
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render(request, 'pass_generator/home.html')

def about(request):
    return render(request, 'pass_generator/about.html')

def password(request):
    
    a=str(request.GET["a"])
    b=str(request.GET["b"])
    c=str(request.GET["c"])

    
    characters = list(a)
    number = list(b)
    crt=list(c)
    length = int(request.GET.get('length', 6))

    if request.GET.get('uppercase'):
        characters.extend([x.upper() for x in characters])
    def saveCriteria(request):
      return render(request, "home.html", context)
     
     
      

    gen_pas = ''

    for x in range(length):
        gen_pas += random.choice(characters+number+crt)

    return render(request, 'pass_generator/password.html', {'password': gen_pas})
    #return render(request, 'pass_generator/password.html', {'vote': i})



def sec(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')

        data = {
                'email': email, 
                'email1':'RANDOM PASSWORD GENERATOR',
                'message': message
        }
        message = '''
        Your Password Is:{}

        From: {}

        '''.format(data['message'],data['email1'])
        send_mail(data['message'],message,'',[email])
    
    return render(request, 'pass_generator/sec.html', {})



