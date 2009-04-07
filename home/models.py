# coding=utf-8
from django.db import models

# 用户
class User(models.Model):
    name = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    true_name = models.CharField(max_length=10)
    is_admin = models.BooleanField(default=False)
    email = models.EmailField()
    
    def __unicode__(self):
        return self.true_name
    
#新闻
class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    post_time = models.DateTimeField(auto_now_add=True)
    last_modify_time = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=20)
    image = models.ImageField(upload_to='photo/news/%Y%m', blank=True)
    
    def __unicode__(self):
        return self.title
    
#项目
class Project(models.Model):
    STATE_CHOICES = (('A', '关注中'),
                     ('D', '进行中'),
                     ('R', '重提交'),
                     ('S', '成功'),
                     ('P', '失败申诉中'),
                     ('F', '失败'))
    TYPE_CHOICES = (('A', 'API'),
                     ('U', 'UI'),
                     ('H', 'API+UI'))
    
    state = models.CharField(max_length=1, choices=STATE_CHOICES)
    name = models.CharField(max_length=255)
    source = models.ForeignKey('ProjectSource')
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    description = models.TextField(blank=True)
    fund = models.FloatField(null=True, blank=True)
    duty_person = models.ForeignKey('User')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    
    def __unicode__(self):
        return self.name
    
    
#项目来源
class ProjectSource(models.Model):
    name = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.name
    
#资源信息
class Resource(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.name