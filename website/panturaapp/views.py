from django.shortcuts import render,redirect
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse, request 
from django.utils.translation import gettext as _
from django.utils.translation import get_language,activate,gettext
from django.contrib import messages
from .forms import ContactForm,CreateAcount
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required



# Create your views here.
def new_func():
               return redirect('')

#@login_required(login_url='panturaapp:LogIn')
def index(request):
    return render(request,'panturaapp/index.html')

def contactUs(request):
    form_class = ContactForm
    # if request is not post, initialize an empty form
    form = form_class(request.POST or None)
    if request.method == 'None':
        return render (request,'panturaapp/Contact_us.html')        
   
    if request.method == 'POST': 
                    fullName=request.POST['fullName']
                    emailAdresse=request.POST['emailAdresse']
                    #subject=request.POST['subject']
                    message=request.POST['message']
                 
                    send_mail(
                                'NOUS CONTACTER (Pntura WEBSITE) from '+ fullName, 
                                message,#messageEmail
                                'email'+ emailAdresse, # from emailadresse 
                                ['amiraexol59@gmail.com'],
                        )
                    contactForm=ContactForm(request.POST)
                    if  contactForm.is_valid():
                        contactForm.save()
                        return render (request,'panturaapp/Contact_us.html',{'fullName':fullName})

    return render (request,'panturaapp/Contact_us.html',{'form':form})                           
def produit(request):
    return render(request,'panturaapp/produit.html')

def log__in(request):
       if request.method == 'POST':
             username= request.POST.get('username')
             password=request.POST.get('password')
             user = authenticate(request, username=username, password=password)  
             if  user is not None:
                                   login(request,user)
                                   return redirect('panturaapp:home') 
             else:
                 messages.add_message(request, messages.error, 'nom d\'utilisateur ou mot de passe incorrect')
                # messages.success(request,'nom d\'utilisateur ou mot de passe incorrect')
                 return redirect('panturaapp:LogIn') 
                 
             
                    
       else: 
             return render (request,'panturaapp/login.html',{})        

def sign__in(request):
          form=CreateAcount()
          if request.method == "POST":
              form=CreateAcount(request.POST)
              if form.is_valid():
                  form.save()   
                  user = form.cleaned_data.get('username')
                  messages.success(request,''+user +' votre compte  était bien créé veuillez vous reconnecter')
                  return redirect ('panturaapp:LogIn')   
              else:
                 messages.error(request,' adresse email ou mot de passe incorrect.veuillez réessayer')
                 return redirect('panturaapp:SignIn')
                     
              
          return render(request,'panturaapp/sign in.html',{'form':form})     

def logout_page(request):
    logout(request)
    return redirect('panturaapp:LogIn')             
                   