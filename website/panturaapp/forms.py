from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contact
from django import forms

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields='__all__'
        labels = {
            "fullName": "","emailAdresse":"","subject":"","message":""
        }
          
        widgets={
                   'fullName':forms.TextInput(attrs={'class':'form-control mb-3 ','placeholder':'Nom & Prenom','style':'font-size:1.5vw;font-weight:bolder;background-color:#E4EFE7;opacity:100%;color:black;border:none; border-radius:6px'}),
                   'emailAdresse':forms.EmailInput(attrs={'class':'form-control mb-3','placeholder':'Email','style':'font-size:1.5vw;font-weight:bolder;color:black;background-color:#E4EFE7;opacity:100%;border:none; border-radius:6px'}),
                   'subject':forms.TextInput(attrs={'class':'form-control  mb-3','placeholder':'Sujet','style':'font-size:1.5vw;font-weight:bolder;color:black;background-color:#E4EFE7;opacity:100%;border:none; border-radius:6px'}),
                   'message':forms.Textarea(attrs={'class':'form-control  mb-3','placeholder':'Message','style':'font-size:1.5vw;font-weight:bolder;color:black;background-color:#E4EFE7;opacity:100%;border:none; border-radius:6px'}),
                   'nom d\'utilisateur':forms.Textarea(attrs={'class':'form-control  mb-3','placeholder':'Message','style':'font-size:1.5vw;font-weight:bolder;color:black;background-color:#E4EFE7;opacity:100%;border:none; border-radius:6px'}),
               }
               




class CreateAcount(UserCreationForm):
    password1 = forms.CharField( 
        
        widget=forms.PasswordInput(attrs={ 'type':'password', 'class':'form-control mb-3 w-75','style':'font-size:1.5vw;font-weight:bolder;opacity:100%;color:black;border:1px solid #99DB99 ; border-radius:6px' }),
    )
    password2 = forms.CharField(
         
         widget=forms.PasswordInput(attrs={ 'type':'password','class':'form-control mb-3 w-75','style':'font-size:1.5vw;font-weight:bolder;opacity:100%;color:black;border:1px solid #99DB99; border-radius:6px'  }),
    )
    class Meta:
        model=User
        fields=['username','email','password1','password2'] 
        

        labels = {
            'username':'Nom d\'utilisateur',
             'email':'Email',
             'password1':'Mot De Passe',
             'password2':'Confirmer Le Mot De Passe',
            

        } 
        widgets={
                   'username':forms.TextInput(attrs={'class':'form-control mb-3 w-75','style':'font-size:1.5vw;font-weight:bolder;opacity:100%;color:black;border:1px solid #99DB99; border-radius:6px'}),
                   'email':forms.EmailInput(attrs={'class':'form-control mb-3 w-75','style':'font-size:1.5vw;font-weight:bolder;color:black;opacity:100%;border:1px solid #99DB99; border-radius:6px'}),
                   
                   
               }
        


        

        