import datetime
from django.db import models
from django.utils import timezone

"""
In this file we will set our models, basically what data we are expecting/need and the same will be reflected into the db. 

We divide them by Class and then using the models.Model, and then we set the variables which will be fields in the database (with specifying the data type of the field)

Each class creates a table in the database

we also create relationship between different classes by using a foreignkey

Every time we make changes to models,
- Change your models (in models.py).
- Run python manage.py makemigrations to create migrations for those changes
 -Run python manage.py migrate to apply those changes to the database. 
"""

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
