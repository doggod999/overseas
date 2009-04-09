from django.contrib import admin

from overseas.home.models import News
from overseas.home.models import User
from overseas.home.models import Project
from overseas.home.models import ProjectSource
from overseas.home.models import Resource
from overseas.home.models import RFP

admin.site.register(News)
admin.site.register(User)
admin.site.register(Project)
admin.site.register(ProjectSource)
admin.site.register(Resource)
admin.site.register(RFP)