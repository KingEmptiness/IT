# _*_ encoding:utf-8 _*_
from django.db import models
from datetime import datetime
from ckeditor_uploader.fields import RichTextUploadingField
from tinymce import models as tinymce_models
from mdeditor.fields import MDTextField
import tinymce

# Create your models here.


class ITTest(models.Model):
    name = models.CharField(verbose_name=u"姓名", max_length=50, null=True, blank=True)
    email = models.EmailField(verbose_name=u"邮箱", null=True, blank=True)
    content = MDTextField(verbose_name=u"富文本")
    add_time = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"测试"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name