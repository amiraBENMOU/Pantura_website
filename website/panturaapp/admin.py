from django.contrib import admin
from .models import Contact


# Register your models here.

class AdminContact(admin.ModelAdmin):
    model=Contact
    list_display = ('fullName', 'emailAdresse','subject','message')

admin.site.register(Contact,AdminContact)


# Register your models here.
