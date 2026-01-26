from django.http import HttpResponse # type: ignore

# Create your views here.
def postId(request,id):
    return HttpResponse(f"user id {id}")