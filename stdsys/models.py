from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Grade(models.Model):
    gname = models.CharField(max_length=2)
    def __str__(self):
        return self.gname

class Banji(models.Model):
    bname = models.CharField(max_length=1)
    def __str__(self):
        return self.bname

class Major(models.Model):
    mname = models.CharField(max_length=10)
    def __str__(self):
        return self.mname


class Tag(models.Model):
    tname = models.CharField(max_length=100)
    tcolor = models.CharField(
        max_length=20,
        default='waring'
        )
    tdisplay = models.BooleanField(
        default=True,
    )
    def __str__(self):
        return self.tname

class Student(models.Model):
    sname = models.CharField(max_length=10)
    sclass = models.CharField(max_length=15)
    sid = models.CharField(max_length=12)
    ssex = models.CharField(max_length=1)
    smajor = models.CharField(
        max_length=10,
        blank = True,
        null = True,
        )
    sgrade = models.CharField(
        max_length=2,
        blank = True,
        null = True,
        )
    sbanji = models.CharField(
        max_length=1,
        blank = True,
        null = True,
        )
    tag = models.ManyToManyField(Tag)
    def __str__(self):
        return self.sname

class Event(models.Model):
    student = models.ForeignKey('stdsys.Student', on_delete=models.CASCADE, related_name='event')
    detail = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=100)
    def __str__(self):
        return self.detail

