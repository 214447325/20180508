# -*- coding: utf-8 -*-
from django.db import models
# 爬取QQ评论信息
# Create your models here.
class QQItem(models.Model):
    # QQ用户
    qqName = models.CharField(max_length=20)

    # 评论内容
    qqContent = models.TextField()

    # 评论时间
    qqTime = models.CharField(max_length=15)

    # 获得点赞得数量
    qqCount = models.IntegerField()