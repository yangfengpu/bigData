from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth import views
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

def index(request):
    return HttpResponse("Hello, world. You're at the test index.")

def activities(request):
    return HttpResponse("Hello, act.")

def createActivity(request):
    if request.user.is_authenticated():
        # Do something for authenticated users.
        return HttpResponse("create activity")
    else:
        # Do something for anonymous users.
        return HttpResponse("login first for creating activity")

def updateActivity(request, act_id):
    return HttpResponse("update activity")

def activityDetail(request, act_id):
    tags = Tag.objects.order_by('tag')[:act_id]
    output = ', '.join([t.tag for t in tags])
    return HttpResponse(output)

def actions(request):
    return HttpResponse("actions")
@login_required(login_url='/accounts/login/')
def nouns(request):
    return render_to_response('nouns/all.html')#, {'poll': p})

def tags(request):
    return HttpResponse("tags")

def tag(request, tag_id):
    return HttpResponse("tag")

def auth(request, u, p):
    result = ""
    user = authenticate(username= u, password= p)
    if user is not None:
        # the password verified for the user
        if user.is_active:
            result = ("User is valid, active and authenticated")
        else:
            result = ("The password is valid, but the account has been disabled!")
    else:
        # the authentication system was unable to verify the username and password
        result = ("The username and password were incorrect.")
    return HttpResponse(result)

def change_password(request):
    template_response = views.password_change(request)
    # Do something with `template_response`
    return template_response

