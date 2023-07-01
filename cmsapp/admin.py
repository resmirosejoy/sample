from django.contrib import admin
from cmsapp.models import CourseModel,StudentModel,TeacherModel
# Register your models here.


@admin.register(CourseModel)
class CourseDetailAdmin(admin.ModelAdmin):
    list_display=('id','Course_Name','Course_Fees')

@admin.register(StudentModel)
class StudentDetailAdmin(admin.ModelAdmin):
    list_display=('id','Course','Std_Name','Std_Address','Std_Age','Join_Date')

@admin.register(TeacherModel)
class TeacherDetailAdmin(admin.ModelAdmin):
    list_display=('id','teacher','Course','phone_number','address','gender','age','image')

