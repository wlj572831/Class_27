from django.db import models


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=32)  # 出版社名称
