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
        


