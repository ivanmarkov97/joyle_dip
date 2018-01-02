from django.db import models
from django.utils import timezone 
# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=80, default='')
    leader = models.IntegerField(blank=True)
    create_date = models.DateField(default=timezone.now())

    def __str__(self):
        return (self.name + " " +
                self.leader + " " +
                str(self.create_date)
               )

class Chat(models.Model):
    name = models.CharField(max_length=80, default='')
    group = models.IntegerField(blank=True)
    def __str__(self):
        return (self.name)

class Message(models.Model):
    sender = models.IntegerField()
    date = models.DateField(default=timezone.now())
    text = models.TextField(default='')
    status = models.IntegerField(default=0)
    chat = models.IntegerField()

    def __str__(self):
        return ("message " + self.text)
