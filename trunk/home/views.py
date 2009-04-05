# coding=utf-8
from django.shortcuts import render_to_response
from overseas.home.models import User

def main(request):
    user = request.session.get('user', None)
    if user:
        log_url = '/logout/'
        log_txt = '退出'
        return render_to_response('home.html', {'user': user, 
                                                'log_url': log_url,
                                                'log_txt': log_txt})
    
    else:
        log_url = '/'
        log_txt = '登录'
        return render_to_response('home.html', {'user': user, 
                                                'log_url': log_url,
                                                'log_txt': log_txt})
        
def about(request):
    pass