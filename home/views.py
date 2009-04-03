# coding=utf-8
from django.shortcuts import render_to_response
from overseas.login.models import User

def main(request):
    user = request.session.get('user', None)
    return render_to_response('home.html', {'user': user})