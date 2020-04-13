from django.db import models

class Article (models.Model):
    title = models.CharField(u'標題',max_length=256)
    content = models.TextField(u'內容')
    pub_date = models.DateTimeField(u'發表時間',auto_now_add=True,  editable=True)
    update_time = models.DateTimeField(u'更新時間',auto_now=True,null=True)

    def __str__(self):
        return self.title
# Create your models here.
