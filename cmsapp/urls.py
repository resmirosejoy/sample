from unicodedata import name
from django import views
from django.urls import include, path
from.import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('homeuser/',views.homeuser,name='homeuser'),
    path('homeadmin/',views.homeadmin,name='homeadmin'),

    path('usercreate/',views.usercreate,name="usercreate"),
    path('login_function/',views.login_function,name="login_function"),
    path('logout/',views.logout,name="logout"),

#...............................................................................

    path("Home",views.Home,name="Home"),
    path("CoursePage",views.CoursePage,name="CoursePage"),
    path("StudentPage",views.StudentPage,name="StudentPage"),
    path("AddCourse",views.AddCourse,name="AddCourse"),
    path("AddStudent",views.AddStudent,name="AddStudent"),
    path("StudentDetails",views.StudentDetails,name="StudentDetails"),
    path('Tables',views.Tables,name='Tables'),

#................................................................................

    path('addStudent',views.addStudent,name='addStudent'),
#    path('add_student_details',views.add_student_details,name='add_student_details'),
    path('show_students',views.show_students,name='show_students'),
    
    path('editpage/',views.editpage,name='editpage'),
    path('edit_student_details/<int:pk>',views.edit_student_details,name='edit_student_details'),
#    path('delete_student/<int:pk>',views.delete_student,name='delete_student'),
    path('trialedit',views.trialedit,name='trialedit'),
    path('show_student',views.show_student,name='show_student'),
    
]
#/<int:pk>'