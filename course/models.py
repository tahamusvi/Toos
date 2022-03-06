from django.db import models


class Grade(models.Model):
    title = models.CharField(max_length=30)
    # code = models.IntegerField()

    def __str__(self):
        return self.title
# -----------------------------------
class Cover(models.Model):
    title = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to ='covers/')

    def __str__(self):
        return self.title
# -----------------------------------
class Kind(models.Model):
    title = models.CharField(max_length=30)
    picture = models.ImageField()
    code = models.IntegerField()

    def __str__(self):
        return self.title
# ----------------------------------------------------------------------------------------------------------------------------
class Plan_weeks(models.Model):
    title = models.TextField()
    picture = models.ImageField()
    kind = models.ForeignKey(
        Kind, blank=True, null=True, related_name="plan", on_delete=models.CASCADE)
    grade = models.ForeignKey(
        Grade, blank=True, null=True, related_name="plan", on_delete=models.CASCADE)
    def __str__(self):
        return self.title
# ----------------------------------------------------------------------------------------------------------------------------
class News(models.Model):
    title = models.TextField()
    text = models.TextField()
    kind = models.ForeignKey(
        Kind, blank=True, null=True, related_name="news", on_delete=models.CASCADE)
    grade = models.ForeignKey(
        Grade, blank=True, null=True, related_name="news", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# ----------------------------------------------------------------------------------------------------------------------------
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='teachers')
    lesson = models.TextField()
    school = models.TextField()
    reshte_text = models.TextField()
    kind = models.ForeignKey(
        Kind, blank=True, null=True, related_name="teacher", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)
# ----------------------------------------------------------------------------------------------------------------------------
class Session_coruse(models.Model):
    text = models.TextField()
    video = models.FileField()
    def __str__(self):
        return str(self.text)
# ----------------------------------------------------------------------------------------------------------------------------
class Course(models.Model):
    title_persion = models.CharField(max_length=30)
    title_en = models.CharField(max_length=30)
    price = models.IntegerField()
    picture = models.ImageField()
    kind = models.ForeignKey(
        Kind, blank=True, null=True, related_name="course", on_delete=models.CASCADE)
    grade = models.ForeignKey(
        Grade, blank=True, null=True, related_name="course", on_delete=models.CASCADE)
    #Saaat
    price = models.IntegerField()
    teacher = models.ForeignKey(Teacher, blank=True, null=True, related_name="course", on_delete=models.CASCADE)

    link = models.TextField()
    video_preview = models.FileField(blank=True, null=True)
    sessions = models.ManyToManyField(Session_coruse, related_name="course")
    is_new = models.BooleanField(default=True)



    def __str__(self):
        return str(self.title_persion)
# ----------------------------------------------------------------------------------------------------------------------------
from django.conf import settings
class Course_buyer(models.Model):
    Course = models.ForeignKey(
        Course, blank=True, null=True, related_name="buyers", on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, blank=True, null=True, related_name="buyers", on_delete=models.CASCADE)
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
