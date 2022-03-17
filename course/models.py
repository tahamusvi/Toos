from django.db import models


class Grade(models.Model):
    title = models.CharField(max_length=100,blank=True, null=True)
    picture = models.ImageField(upload_to ='grade/')
    # code = models.IntegerField()

    def __str__(self):
        return self.title
# -----------------------------------
class Package(models.Model):
    title = models.CharField(max_length=100,blank=True, null=True)
    picture = models.ImageField(upload_to ='package/')
    # path = models.CharField(max_length=100,blank=True, null=True)
    code = models.IntegerField(unique=True)
    def __str__(self):
        return self.title

    def path(self):
        title = self.title
        temp = ""

        for i in title:
            if(i==' '):
               temp += '-'
            else:
                temp += i

        return f'پکیج-های-آموزشی-{temp}'
    def show_title(self):
        return f'پکیج های {self.title}'
# -----------------------------------
class Kind(models.Model):
    title = models.CharField(max_length=100,blank=True, null=True)
    picture = models.ImageField(upload_to ='kind/')
    code = models.IntegerField(unique=True)
    package = models.ForeignKey(
        Package, blank=True, null=True, related_name="kind", on_delete=models.CASCADE)


    def package_title(self):
        return self.package.show_title()

    def __str__(self):
        return self.title

# ----------------------------------------------------------------------------------------------------------------------------
class News(models.Model):
    title = models.CharField(max_length=100,blank=True, null=True)
    text = models.TextField()
    kind = models.ForeignKey(
        Kind, blank=True, null=True, related_name="news", on_delete=models.CASCADE)
    grade = models.ForeignKey(
        Grade, blank=True, null=True, related_name="news", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
# ----------------------------------------------------------------------------------------------------------------------------
class OnlineClass(models.Model):
    title = models.CharField(max_length=100,blank=True, null=True)
    link = models.TextField()
    #Filter for Users



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
    title = models.CharField(max_length=100,blank=True, null=True)
    text = models.TextField()
    video = models.FileField()
    def __str__(self):
        return str(self.title)
# ----------------------------------------------------------------------------------------------------------------------------
from datetime import datetime
class Course(models.Model):
    title_persion = models.CharField(max_length=30)
    title_en = models.CharField(max_length=30)
    # price = models.IntegerField()
    picture = models.ImageField()
    kind = models.ForeignKey(
        Kind, blank=True, null=True, related_name="course", on_delete=models.CASCADE)
    grade = models.ForeignKey(
        Grade, blank=True, null=True, related_name="course", on_delete=models.CASCADE)
    # Saaat
    time = models.TimeField(blank=True, default=datetime.now)
    price = models.IntegerField()
    teacher = models.ForeignKey(
        Teacher, blank=True, null=True, related_name="course", on_delete=models.CASCADE)
    code = models.IntegerField(unique=True)
    Text = models.TextField()
    video_preview = models.FileField(blank=True, null=True)
    sessions = models.ManyToManyField(Session_coruse, related_name="course")
    is_new = models.BooleanField(default=True)


    def count_session(self):
        return self.sessions.all().count()

    def teacher_name(self):
        return str(self.teacher.name)

    def path(self):
        title = self.title_persion
        temp = ""

        for i in title:
            if(i==' '):
               temp += '-'
            else:
                temp += i

        title1 = self.kind.package.path()
        return  f'دوره-{temp}' + '/' + title1

    def __str__(self):
        return str(self.title_persion)
# ----------------------------------------------------------------------------------------------------------------------------
from django.conf import settings
class Course_buyer(models.Model):
    Course = models.ForeignKey(
        Course, blank=True, null=True, related_name="buyers", on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, blank=True, null=True, related_name="buyers", on_delete=models.CASCADE)
