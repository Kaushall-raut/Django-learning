from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail

@receiver(post_save,sender=User)

def send_welcome_email(sender,instance,created,**kwargs):
    if created:
        print(f"New user created : {instance.username} ")
        subject="welcome to django mail services"
        message=f"Hello {instance.username}"
        from_email="kaushalraut.code@gmail.com"
        recipient_list=[instance.email]

    send_mail(subject,message,from_email,recipient_list,fail_silently=True)
    print("Mail sent successfully")