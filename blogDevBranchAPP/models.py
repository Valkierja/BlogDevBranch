from operator import mod
from pydoc_data.topics import topics
from re import T
import re
from tabnanny import verbose
from django.db import models

# Create your models here.
class NormalArticleTopic(models.Model):
    # 普通文章类
    title = models.CharField(max_length=256)
    date_var = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # 强转字符串时返回标题text
        #Django默认使用该方法渲染为类的简单表示
        return self.title
    
  
class NormalArticleTopicEntry(models.Model):
    # TODO:maybe change on_delete ; -1 means "was there but deleted"
    # TODO:https://stackoverflow.com/questions/38388423/what-does-on-delete-do-on-django-models
    topics = models.ForeignKey(NormalArticleTopic, on_delete=models.SET("DELETED")) 
 
    # TODO:markdown text
    text = models.TextField()
    date_var = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries' # name for plural items

    def __str__(self):
        # 'str' object has no attribute 'len'
        if (len(self.text) > 64):
            return self.text[:64]+ "..."
        return self.text
         




