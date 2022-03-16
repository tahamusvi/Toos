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
