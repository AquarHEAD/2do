from django.db import models
from members.models import Member

class Todo(models.Model):
    note = models.CharField(max_length = 50)
    created = models.DateTimeField(auto_now_add = True)
    done = models.DateTimeField(blank = True, null = True)
    owner = models.ForeignKey(Member)