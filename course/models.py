from django.db import models


class Grade(models.Model):
    title = models.CharField(max_length=30)

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
# -----------------------------------
class Course(models.Model):
    title_persion = models.CharField(max_length=30)
    title_en = models.CharField(max_length=30)
    picture = models.ImageField()
    link = models.TextField()
    # video = models.FileField()
    video_preview = models.FileField(blank=True, null=True)
    kind_course = models.ForeignKey(
        Kind, blank=True, null=True, related_name="course", on_delete=models.CASCADE)
    grade = models.ForeignKey(
        Grade, blank=True, null=True, related_name="course", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title_persion)
# ----------------------------------------------------------------------------------------------------------------------------
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ForeignKey(
        Course, blank=True, null=True, related_name="teacher", on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='teachers')
    text = models.TextField()
    school = models.TextField()
    reshte = models.TextField()

    def __str__(self):
        return str(self.name)
# ----------------------------------------------------------------------------------------------------------------------------
class giude(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return str(self.phone)
# ----------------------------------------------------------------------------------------------------------------------------
class soal(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return str(self.question)
