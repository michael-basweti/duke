from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def contact(request):
    if request.method == 'POST':
        name = request.POST['form-name']
        email = request.POST['form-email']
        phone = request.POST['form-phone']
        description = request.POST['form-text']

        application = Contact(name=name,description=description,
                        email=email,phone=phone)
        application.save()
        messages.success(request, "Your application has been submitted, you will be contacted shortly")
        return redirect('/contact')

