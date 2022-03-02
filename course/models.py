from django.db import models


class Grade(models.Model):
    title = models.CharField(max_length=30)
    code = models.IntegerField()

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
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='teachers')
    text = models.TextField()
    school = models.TextField()
    reshte = models.TextField()

    def __str__(self):
        return str(self.name)
# ----------------------------------------------------------------------------------------------------------------------------
class Course(models.Model):
    title_persion = models.CharField(max_length=30)
    title_en = models.CharField(max_length=30)
    id_course = models.IntegerField()
    picture = models.ImageField()
    kind_course = models.ForeignKey(
        Kind, blank=True, null=True, related_name="course", on_delete=models.CASCADE)
    grade = models.ForeignKey(
        Grade, blank=True, null=True, related_name="course", on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, blank=True, null=True, related_name="course", on_delete=models.CASCADE)

    # link = models.TextField()
    # video_preview = models.FileField(blank=True, null=True)

    def __str__(self):
        return str(self.title_persion)
# ----------------------------------------------------------------------------------------------------------------------------
class Session_coruse(models.Model):
    video = models.FileField()
    text = models.TextField()
    course = models.ForeignKey(
        Course, blank=True, null=True, related_name="course", on_delete=models.CASCADE)
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
