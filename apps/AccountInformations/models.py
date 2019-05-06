# _*_ encoding:utf-8 _*_
from django.db import models
from datetime import datetime
# Create your models here.


class UserAccountInformations(models.Model):
    province_abbr = models.CharField(verbose_name=u"省份简称", max_length=50, null=True, blank=True)
    department_abbr = models.CharField(verbose_name=u"部门简称", max_length=50, null=True, blank=True)
    english_name = models.CharField(verbose_name=u"英文名", max_length=50, null=True, blank=True)
    chinese_name = models.CharField(verbose_name=u"中文名", max_length=50, null=True, blank=True)
    pinyin = models.CharField(verbose_name=u"中文拼音", max_length=100, null=True, blank=True)
    login_name = models.CharField(verbose_name=u"登录名", max_length=100, null=True, blank=True)
    login_password = models.CharField(verbose_name=u"登录密码", max_length=20, null=True, blank=True)
    staff_number = models.CharField(verbose_name=u"员工工号", max_length=20, null=True, blank=True)
    full_name = models.CharField(verbose_name=u"姓名", max_length=200, null=True, blank=True)
    email_address = models.EmailField(verbose_name=u"邮箱地址", null=True, blank=True)
    resigned = models.CharField(verbose_name=u"是否离职", choices=(("is_resigned", u"是"), ("not_resigned", u"否")), max_length=12, default="not_resigned")
    add_time = models.DateTimeField(verbose_name=u"创建日期", default=datetime.now)

    class Meta:
        verbose_name = u"用户账号信息"
        verbose_name_plural = verbose_name
        unique_together = ('english_name', 'chinese_name', 'login_name')

    def __str__(self):
        return self.chinese_name


class OtherAccountInformations(models.Model):
    description = models.CharField(verbose_name=u"账号描述", max_length=50, null=True, blank=True)
    login_name = models.CharField(verbose_name=u"登录名", max_length=100, null=True, blank=True)
    login_password = models.CharField(verbose_name=u"登录密码", max_length=20, null=True, blank=True)
    add_time = models.DateTimeField(verbose_name=u"创建日期", default=datetime.now)

    class Meta:
        verbose_name = u"其他账号信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.login_name


class EmailAddress(models.Model):
    description = models.CharField(verbose_name=u"邮箱描述", max_length=50, null=True, blank=True)
    email_address = models.EmailField(verbose_name=u"邮箱地址", null=True, blank=True)
    add_time = models.DateTimeField(verbose_name=u"创建日期", default=datetime.now)

    class Meta:
        verbose_name = u"其他邮箱"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.email_address






