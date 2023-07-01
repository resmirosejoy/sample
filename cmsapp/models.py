from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class CourseModel(models.Model):
    Course_Name=models.CharField(max_length=70)
    Course_Fees=models.IntegerField()

    # def __str__(self):
    #     return self.Course_Name

class StudentModel(models.Model):
    Course=models.ForeignKey(CourseModel,on_delete=models.CASCADE,null=True)
    Std_Name=models.CharField(max_length=100, null=True)
    Std_Address=models.CharField(max_length=200, null=True)
    Std_Age=models.IntegerField(null=True)
    Join_Date=models.DateField(auto_now_add=True)

    # def __str__(self):
    #     return self.Std_Name

class TeacherModel(models.Model):
    teacher=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    Course=models.ForeignKey(CourseModel,on_delete=models.CASCADE,null=True)
    phone_number=models.IntegerField(null=True)
    address=models.CharField(max_length=200, null=True)
    gender=models.CharField(max_length=70, null=True)
    age=models.IntegerField(null=True)
    image = models.ImageField(upload_to="image/", null=True)
    