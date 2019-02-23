from django.db import models

# Create your models here.
'''This is where all the models that we create for the todo application are kept'''

class TodoItem(models.Model):
    title = models.CharField(max_length=256, null=True, blank=True)# initialized to empty
    completed = models.BooleanField(blank=True, default=False) # keep track of completed fields
    url = models.CharField(max_length=256, null=True, blank=True) # url for tasks url
    order = models.IntegerField(null=True, blank=True) # ranking orders of the tasks