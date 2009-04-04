# coding=utf-8
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from overseas.login.models import User

def login(request):
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    try:
        user = User.objects.get(name=username, password=password)
    except:
        return HttpResponseRedirect('/')
    
    request.session['user'] = user
    return HttpResponseRedirect('/home/')

def logout(request):
    try:
        del request.session['user']
    except KeyError:
        pass
    return HttpResponseRedirect("/home/")