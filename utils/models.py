from django.db import models
from course.models import *

# ----------------------------------------------------------------------------------------------------------------------------
class WeekPlan(models.Model):
    title = models.CharField(max_length=100,blank=True, null=True)
    picture = models.ImageField()
    kind = models.ForeignKey(
        Kind, blank=True, null=True, related_name="plan", on_delete=models.CASCADE)
    grade = models.ForeignKey(
        Grade, blank=True, null=True, related_name="plan", on_delete=models.CASCADE)
    def __str__(self):
        return self.title
# ----------------------------------------------------------------------------------------------------------------------------
class TimeFromKonkur(models.Model):
    title = models.CharField(max_length=100,blank=True, null=True)
    days = models.IntegerField()
    code = models.IntegerField(unique=True)
    
    def __str__(self):
        return self.title
# ----------------------------------------------------------------------------------------------------------------------------
class Cover(models.Model):
    title = models.CharField(max_length=100,blank=True, null=True)
    picture = models.ImageField(upload_to ='covers/')

    def __str__(self):
        return self.title
# ----------------------------------------------------------------------------------------------------------------------------
class giude(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return str(self.phone)
# ----------------------------------------------------------------------------------------------------------------------------
class Question(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return str(self.question)
# ----------------------------------------------------------------------------------------------------------------------------
