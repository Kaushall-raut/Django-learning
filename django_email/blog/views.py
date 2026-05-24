from django.shortcuts import render
from django.core.mail import send_mail,EmailMessage
from django.template.loader import render_to_string
from django.http import HttpResponse
# Create your views here.

#! sending simple plain text mail

# def send_test_email(request):
#     subject='Django email'
#     message='Sending mail in django'
#     from_email="kaushalraut.code@gmail.com"
#     recipient_list=["kaushalraut755@gmail.com"]

#     send_mail(subject, message, from_email, recipient_list)

#     return HttpResponse("mail sent successfully")

#! sending mail with template

def send_test_email(request):
    subject="welcome to my blog"
    message=render_to_string("mail.html",{"name":"Kaushal"})

    email=EmailMessage(
        subject,
        message,
        "kaushalraut.code@gmail.com",
        ["kaushalraut755@gmail.com"]
    )
    email.content_subtype="html" 
    email.send()
    return HttpResponse("mail send successfully")