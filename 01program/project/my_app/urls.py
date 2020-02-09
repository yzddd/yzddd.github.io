#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : urls.py
@Author: yzddd
@Date  : 2020/2/7 13:38
'''
from django.urls import path
from . import views

urlpatterns = [
    path(r'',views.index),
    path('<int:num>/',views.detail,name='detail'),  # 记得查看正则。可以输入多个数字字幕
    path('grades/',views.grades),
    path('students/',views.students)

]
