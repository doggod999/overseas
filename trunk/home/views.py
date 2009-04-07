# coding=utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from overseas.home.models import User
from overseas.home.models import News
from overseas.home.models import Resource

def main(request):
    user = request.session.get('user', None)
    log_url = '/'
    log_txt = '登录'
    if user:
        log_url = '/logout/'
        log_txt = '退出'
    
    news = News.objects.all().order_by('-id')[0:2]
    
    return render_to_response('home.html', {'user': user, 
                                            'log_url': log_url,
                                            'log_txt': log_txt,
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
        return HttpResponse(news.title)
    return HttpResponse('页面正在建设中...')