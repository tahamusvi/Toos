from django.db import models
from datetime import datetime
from django.utils import timezone

class Grade(models.Model):
    title = models.CharField(max_length=100,blank=True, null=True)
    picture = models.ImageField(upload_to ='grade/')

    def __str__(self):
        return self.title
# -----------------------------------
class Package(models.Model):
    title = models.CharField(max_length=100,blank=True, null=True)
    icon = models.CharField(max_length=100,blank=True, null=True)
    picture = models.ImageField(upload_to ='package/')
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
# class session

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
    text = models.TextField(blank=True, null=True)
    link = models.CharField(max_length=300,blank=True, null=True)
    time = models.TimeField(blank=True)
    # , default=timezone.now()
    video = models.FileField(blank=True, null=True)
    is_free = models.BooleanField(default=False)
    def __str__(self):
        return str(self.title)
# ----------------------------------------------------------------------------------------------------------------------------
class Course(models.Model):
    title_persion = models.CharField(max_length=30)
    title_en = models.CharField(max_length=30,blank=True, null=True)
    picture = models.ImageField()
    kind = models.ForeignKey(
        Kind, blank=True, null=True, related_name="course", on_delete=models.CASCADE)
    grade = models.ForeignKey(
        Grade, blank=True, null=True, related_name="course", on_delete=models.CASCADE)
    # time = models.TimeField(blank=True, default=datetime.now)
    # time = models.DateTimeField(blank=True, default=datetime.now)
    time_1 = models.CharField(max_length=30)
    price = models.IntegerField()
    teacher = models.ForeignKey(
        Teacher, blank=True, null=True, related_name="course", on_delete=models.CASCADE)
    code = models.IntegerField(unique=True)
    is_online = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.now)
    Text = models.TextField()
    video_preview = models.FileField(blank=True, null=True)
    sessions = models.ManyToManyField(Session_coruse, related_name="course")
    is_new = models.BooleanField(default=True)


    def time(self):
        temp = self.time_1[0]+self.time_1[1] + ':' + self.time_1[2]+self.time_1[3]+ ':' + self.time_1[4]+self.time_1[5]
        return temp
    def count_user(self):
        return self.user.all().count()

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
class OnlineClass(models.Model):
    title = models.CharField(max_length=100,blank=True, null=True)
    link = models.TextField()
    next_class = models.CharField(max_length=200,blank=True, null=True)
    course = models.ForeignKey(
        Course, blank=True, null=True, related_name="onlineClass", on_delete=models.CASCADE)
    #Date
    day = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()


    def date(self):
        return f'{self.year}/{self.month}/{self.day}'

    def __str__(self):
        return self.course.title_persion + " " + self.title
# ----------------------------------------------------------------------------------------------------------------------------
from django.conf import settings
class Course_buyer(models.Model):
    Course = models.ForeignKey(
        Course, blank=True, null=True, related_name="buyers", on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, blank=True, null=True, related_name="buyers", on_delete=models.CASCADE)
