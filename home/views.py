# coding=utf-8
import datetime

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from overseas.home.models import User
from overseas.home.models import News
from overseas.home.models import Resource
from overseas.home.models import Project

def main(request):
    user = request.session.get('user', None)
    news = News.objects.all().order_by('-id')[0:2]
    
    sunday = getsunday()
    print sunday
    saturday = getsaturday()
    print saturday
    att = []
    attention = Project.objects.filter(state='A').order_by('-id')
    for a in attention:
        if a.start_time > sunday:
            att.append(a)
    
    return render_to_response('home.html', {'user': user, 
                                            'news': news,
                                            'attention': att,
                                            })
    

        
def about(request):
    return HttpResponseRedirect("/home/")

def resource(request):
    user = request.session.get('user', None)
    if not user:
        return HttpResponseRedirect("/")
    else:
        resource_list = Resource.objects.all()
        return render_to_response('resource.html', {'resource': resource_list,
                                                    'user': user,
                                                    })
        
def news(request, n_id):
    if n_id:
        news = News.objects.get(id=n_id)
    else:
        news = ''
    user = request.session.get('user', None)
    news_list = News.objects.all().order_by('-id')
    return render_to_response('news.html', {'news': news,
                                            'news_list': news_list,
                                            'user': user,
                                            })
    
def attention(request, p_id):
    pass

#本周第一天，周日
def getsunday():
    today = datetime.datetime.now()
    w = today.weekday()
    sunday = today - datetime.timedelta(days=w+1)
    return sunday

#本周最后一天，周六
def getsaturday():
    today = datetime.datetime.now()
    w = today.weekday()
    saturday = today + datetime.timedelta(days=5-w)
    return saturday