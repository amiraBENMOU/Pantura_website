
from django.urls import path
from .import views
from django.contrib.auth import views as auth_views


app_name = "panturaapp"
urlpatterns=[
    #views. is to import a functction from views.py 
    path('',views.index,name="home"),
    path('contactUs',views.contactUs,name="contactUs"),
    path('Produit',views.produit,name="Produit"),
    #path('SignIn',views.sign__in,name="SignIn"),
    #path('LogIn',views.log__in,name="LogIn"),
    path('LogOut',views.logout_page,name="LogOut"),
    path('LogIn', auth_views.LoginView.as_view(template_name="panturaapp/login.html", redirect_authenticated_user=True), name='LogIn'),
    path('SignIn', auth_views.LoginView.as_view(template_name="panturaapp/sign in.html", redirect_authenticated_user=True), name='SignIn'),
]