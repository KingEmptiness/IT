# -*- coding: utf-8 -*-
__author__ = 'Cory'
__date__ = '2018/9/14 23:01'

import xadmin
from .models import ITTest


class ITTestAdmin(object):
    list_display = ['name', 'email', 'content', 'add_time']
    search_fields =  ['name', 'email']
    list_filter =  ['name', 'email', 'content', 'add_time']
    add_form_template = 'ITtestapp/model_form.html'


xadmin.site.register(ITTest, ITTestAdmin)