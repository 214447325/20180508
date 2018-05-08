# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class LaWeb(models.Model):
    # 浼佷笟鐨勬爣棰�
    laTitle = models.CharField(max_length=10)
    # 钖祫
    laMoney = models.CharField(max_length=10)
    # 鑱屼綅
    laPosition = models.CharField(max_length=20)
    # 浼佷笟绫诲瀷
    laType = models.CharField(max_length=30)
    # 鍙戝竷鏃堕棿
    laReleaseTime = models.CharField(max_length=20)