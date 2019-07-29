from django.shortcuts import render, redirect
from templated_email import send_templated_mail
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
        messages.success(request, "Your message has been submitted, you will be contacted shortly")
        send_templated_mail(
        template_name='welcome',
        from_email=email,
        recipient_list=['michaelbasweti@gmail.com'],
        context={
            
            'full_name':name,
            'email':email,
            'phone':phone,
        },
        )
        return redirect('/contact')

