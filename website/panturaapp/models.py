 # -*- coding: utf-8 -*- 
from django.db import models


# Create your models here.
class Contact(models.Model):
     fullName=models.CharField('Nom & Prenom',max_length=200,null=False)
     emailAdresse=models.CharField('Email',max_length=200,null=False)
     subject=models.CharField('Sujet',max_length=200,null=False)
     message=models.TextField('Message',null=False)

     def __str__(self):
                  return self.fullName+' '+self.emailAdresse+' '+self.subject+' '+self.message


      #Second class



class SeConnecter(models.Model):
     Email=models.CharField('Email',max_length=200,null=False)
     MotDePasse=models.CharField('Mot de passe',max_length=200,null=False)
 

     def __str__(self):
                  return self.Email+' '+self.MotDePasse

#class User(models.Model):
  # UserName=models.CharField('Nom d '+ u'\u0301'+'utilisateure',max_length=200,null=False)
  # Email=models.CharField('Email',max_length=200,null=False)
   #Pssword=models.CharField('Mot De Passe',max_length=200,null=False)
   #ConfirmPassword=models.CharField('Confirmer Le Mot De Passe',null=False)
   #def __str__(self):
                 # return self.UserName+' '+self.Email+' '+self.Pssword+' '+self.ConfirmPassword
   
    