from django.shortcuts import render,redirect
from .models import HireCorporate
from django.contrib import messages


def hire_corporate(request):
    if request.method == 'POST':
        service = request.POST['service']
        applicant_name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        application_description = request.POST['message']

        application = HireCorporate(service=service,applicant_name=applicant_name,application_description=application_description,
                        email=email,phone=phone)
        application.save()
        messages.success(request, "Your application has been submitted, you will be contacted shortly")
        return redirect('/services')