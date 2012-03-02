from django.db import models

class Pair(models.Model):
    title = models.CharField(max_length = 20)
    slug = models.CharField(max_length = 20)
    public = models.BooleanField(default = False)
    created = models.DateTimeField(auto_now_add = True)

class Member(models.Model):
    nick = models.CharField(max_length = 20)
    password = models.CharField(max_length = 60)
    isleft = models.BooleanField()
    locked = models.BooleanField(default = False)
    pair = models.ForeignKey(Pair)