# coding=utf-8
import datetime

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from overseas.home.models import User
from overseas.home.models import News
from overseas.home.models import Resource
from overseas.home.models import Project
from overseas.home.models import RFP

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
    return HttpResponse('''页面正在建设中...<br>\
                         <a href="/home/">返回主页</a>''')

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
    sunday = getsunday()
    saturday = getsaturday()
    user = request.session.get('user', None)
    projects = []
    project = ''
    title = ''
    add = False
    if p_id == 'attention':
        projects = Project.objects.filter(state='A').order_by('-id')
        title = '本周关注项目'
        add = True
    elif p_id == 'submit':
        title = '本周提交项目'
        sub1 = Project.objects.filter(state='D').order_by('-start_time')
        for s in sub1:
            if s.end_time <= saturday and s.end_time >= sunday :
                projects.append(s)

        sub1 = Project.objects.filter(state='R').order_by('-start_time')
        for s in sub1:
            if s.end_time <= saturday and s.end_time >= sunday :
                projects.append(s)
    elif p_id == 'ing':
        title = '正在进行的项目'
        add1 = Project.objects.filter(state='D').order_by('-start_time')
        add2 = Project.objects.filter(state='R').order_by('-start_time')
        for p in add1:
            projects.append(p)
        for p in add2:
            projects.append(p)
    elif p_id == 'all':
        title = '所有项目'
        projects = Project.objects.all().order_by('-id')
    else:
        title = '所有项目'
        project = Project.objects.get(id = p_id)
        state = project.get_state_display()
        type = project.get_type_display()
        projects = Project.objects.all().order_by('-id')
        return render_to_response('project.html', {'project': project,
                                                   'state': state,
                                                   'type': type,
                                                   'projects': projects,
                                                    'user': user,
                                                    'title': title,
                                                    })
    return render_to_response('project.html', {'projects': projects,
                                                    'user': user,
                                                    'title': title,
                                                    'add': add,
                                                    })
        
def download(request, f_id):
    user = request.session.get('user', None)
    if not user:
        return HttpResponseRedirect('/')
    if f_id:
        rfp = RFP.objects.get(id = f_id)
        return HttpResponseRedirect(rfp.zip_file.url)
    else:
        rfp = RFP.objects.all().order_by('-date_upload')
        return render_to_response('download.html', {'user': user,
                                                   'rfp': rfp,
                                                    })

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