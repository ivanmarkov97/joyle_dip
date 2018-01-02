from django.db import models
from django.utils import timezone 

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=80, default='')
    deadline = models.DateField(blank=True)
    create_date = models.DateField(default=timezone.now())

    def __str__(self):
        return (self.name #+ " " +
                #str(self.deadline) + " " +
                #str(self.create_date)
               )

class Task(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField(default='')
    create_date = models.DateField(default=timezone.now())
    deadline = models.DateField(null=True)
    position = models.IntegerField(default=0)
    level = models.IntegerField(default=0)
    parent = models.IntegerField(blank=True)
    has_child = models.BooleanField(default=False)
    project = models.ForeignKey("Project", null=True)

    def __str__(self):
        return (self.name + " " +
                self.description + " " +
                str(self.create_date) + " " +
                str(self.deadline) + " " +
                str(self.position) + " " +
                str(self.level) + " " +
                str(self.parent) + " " +
                str(self.has_child) + " " +
                str(self.project)
               )
