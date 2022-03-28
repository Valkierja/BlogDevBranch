import imp
from re import T
from django.contrib import admin

# Register your models here.
from blogDevBranchAPP.models import *

admin.site.register(NormalArticleTopic)
admin.site.register(NormalArticleTopicEntry)
