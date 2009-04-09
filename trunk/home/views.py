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
    saturday = getsaturday()
    
    attention = []
    att = Project.objects.filter(state='A').order_by('-id')
    for a in att:
        if a.start_time >= sunday:
            attention.append(a)
    
    submit = []
    sub1 = Project.objects.filter(state='D').order_by('-start_time')
    for s in sub1:
        if s.end_time <= saturday and s.end_time >= sunday :
            submit.append(s)

    sub1 = Project.objects.filter(state='R').order_by('-start_time')
    for s in sub1:
        if s.end_time <= saturday and s.end_time >= sunday :
            submit.append(s)
    
    doing = []
    add1 = Project.objects.filter(state='D').order_by('-start_time')
    add2 = Project.objects.filter(state='R').order_by('-start_time')
    for p in add1:
        doing.append(p)
    for p in add2:
        doing.append(p)
    
    return render_to_response('home.html', {'user': user, 
                                            'news': news,
                                            'attention': attention,
                                            'submit': submit,
                                            'doing': doing,
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
    
def project(request, p_id):
    user = request.session.get('user', None)
    project = Project.objects.get(id = p_id)
    projects = Project.objects.all().order_by('-id')
    return render_to_response('project.html', {'project': project,
                                               'projects': projects,
                                                'user': user,
                                                })
        
def attention(request, p_id):
    pass

#本周第一天，周日
def getsunday():
    today = datetime.datetime.now()
    w = today.weekday()
    sunday = today - datetime.timedelta(days=w+1)
    tmp = sunday.strftime('%Y%m%d')
    sunday = datetime.datetime(int(tmp[:4]), int(tmp[4:6]), int(tmp[6:]))
    return sunday

#本周最后一天，周六
def getsaturday():
    today = datetime.datetime.now()
    w = today.weekday()
    saturday = today + datetime.timedelta(days=5-w)
    tmp = saturday.strftime('%Y%m%d')
    saturday = datetime.datetime(int(tmp[:4]), int(tmp[4:6]), int(tmp[6:]))
    return saturday