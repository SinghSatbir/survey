from django.contrib.auth.models import User
from django.db import models
import datetime

# Create your models here.


class Survey(models.Model):
    owner=models.ForeignKey(to=User,on_delete=models.CASCADE)
    survey_title=models.CharField(max_length=30)
    survey_topic=models.CharField(max_length=30)
    survey_description=models.CharField(max_length=255)
    expiry_date=models.DateTimeField()
    added_date=models.DateTimeField(auto_now_add=True)
    number_of_questions=models.IntegerField()

class Questions(models.Model):
    survey_uid=models.ForeignKey(to=Survey,on_delete=models.CASCADE)
    question_text=models.CharField(max_length=255)
    mandatory=models.BooleanField()
    update_date=models.DateTimeField()

class Answer(models.Model):
    question_id=models.ForeignKey(to=Questions,on_delete=models.CASCADE)
    user_id=models.ForeignKey(to=User,on_delete=models.CASCADE)
    ANSWER_CHOICES = (
        ('Y', 'yes'),
        ('N', 'no'),
    )
    answer = models.CharField(max_length=1, choices=ANSWER_CHOICES)



