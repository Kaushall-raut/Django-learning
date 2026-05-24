from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from .models import Blog


@receiver(pre_save,sender=Blog)

def before_blog_save(sender,instance,**kwargs):
    print(f"About to save blog:{instance.title} ")

@receiver(post_save,sender=Blog)

def after_blog_send(sender,instance,created,**kwargs):
    if created:
        print(f"New blog created :{instance.title}")
    else:
        print(f"Blog updated : {instance.title}")