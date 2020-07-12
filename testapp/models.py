from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course_table(models.Model):
    Course_Name=models.CharField(max_length=250)
    Faculty=models.CharField(max_length=250)
    class_date=models.DateField( )
    class_time=models.TimeField()
    Fee=models.FloatField()
    Duration=models.IntegerField()


class Student_register(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number=models.IntegerField()
    def __str__(self):
        return self.user.username

class EnrollCourse(models.Model):
    Course_Name = models.CharField(max_length=250)
    contact_number = models.IntegerField()
class StudentEnrollCourse(models.Model):
    Name = models.CharField(max_length=250)
    phone= models.IntegerField()



