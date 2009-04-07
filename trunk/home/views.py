# coding=utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from overseas.home.models import User
from overseas.home.models import News
from overseas.home.models import Resource

def main(request):
    user = request.session.get('user', None)
    logined = islogined(request)
    news = News.objects.all().order_by('-id')[0:2]
    
    return render_to_response('home.html', {'logined': logined, 
                                            'news': news,})
    

        
def about(request):
    return HttpResponseRedirect("/")

def resource(request):
    user = request.session.get('user', None)
    if not user:
        return HttpResponseRedirect("/")
    else:
        resource_list = Resource.objects.all()
        return render_to_response('resource.html', {'resource': resource_list,
                                                    'user': user})
        
def news(request, n_id):
    if n_id:
        news = News.objects.get(id=n_id)
    else:
        news = ''
    logined = islogined(request)    
    news_list = News.objects.all().order_by('-id')
    return render_to_response('news.html', {'news': news,
                                            'news_list': news_list,
                                            'logined': logined,})
    
def islogined(request):
    user = request.session.get('user', None)
    if user:
        return True
    else:
        return False