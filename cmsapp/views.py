from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import *


# Create your views here.


def home(request):
    return render(request,'home.html')

def signup(request):
    return render(request,'signup.html')

def loginpage(request):
    return render(request,'login.html')        

@login_required(login_url='login_function')
def homeuser(request):
    return render(request,'homeUser.html')   

def homeadmin(request):
    return render(request,'homeAdmin.html') 



#......Msg Passing and Check Username and Password....
def usercreate(request):
    if request.method=='POST':

        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        Phone=request.POST['Phone']
        Address=request.POST['Address']
        Gender=request.POST['Gender']
        Age=request.POST['Age']
        select=request.POST['select']
        course=CourseModel.objects.get(id=select)

        image=request.FILES.get('file')

        if image==None:
            image="image/img.jpeg"
        

        if password==cpassword:  #  password matching......
            if User.objects.filter(username=username).exists(): #check Username Already Exists..
                messages.info(request, 'This username already exists!!!!!!')
                #print("Username already Taken..")
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'This email already exists!!!!!!')
                return redirect('signup')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password,email=email)
                user.save()

                data=User.objects.get(id=user.id)
                teacher_data=TeacherModel(phone_number=Phone,address=Address,gender=Gender,age=Age,image=image,Course=course,teacher=data)
                teacher_data.save()
                messages.success(request,'Welcome...'+ data.first_name)
                return redirect('loginpage')

                #messages.info(request, 'SuccessFully completed.......')
                #print("Successed...")
        else:
            messages.info(request, 'Password doesnt match!!!!!!!')
            print("Password is not Matching.. ") 
            return redirect('signup')   
        return redirect('loginpage')
    else:
        return render(request,'signup.html')

#User login functionality view

def login_function(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_staff:
                auth.login(request,user)
                return redirect('homeadmin')
            else:
                auth.login(request,user)
                return redirect('homeuser')
        else:
            message.info(request, 'Invalid username or password. Try again.')
            return redirect('loginpage')

    #messages.info(request, 'Oops, something went wrong.')
    return redirect('loginpage')
            

#User logout functionality view
def logout(request):
	auth.logout(request)
	return redirect('home')


#..............................................................................................................................

def Home(request):
    return render(request,'homeAdmin.html')


def CoursePage(request):
    return render(request,'addcourse.html')


def AddCourse(request):
    if request.method == 'POST':
        coursename=request.POST['coursename']
        coursefees=request.POST['coursefees']
        data = CourseModel(Course_Name=coursename,Course_Fees=coursefees)
        data.save()
        # messages.info(request, 'New User Added')
        return redirect('Home')


def StudentPage(request):
    courses=CourseModel.objects.all()
    context={'courses':courses}
    return render(request,'addstudent.html',context)


def AddStudent(request):
    if request.method=='POST':
        stdname=request.POST['stdname']
        stdaddress=request.POST['stdaddress']
        stdage=request.POST['stdage']
        # joindate=request.POST['joindate']
        select=request.POST['select']
        course=CourseModel.objects.get(id=select)
        data = StudentModel(Std_Name=stdname,Std_Address=stdaddress,Std_Age=stdage,Course=course)
        data.save()
        return redirect('Home')


def StudentDetails(request):
    student_detail = StudentModel.objects.all()
    return render(request,'studentdetail.html',{'student':student_detail})


def Tables(request):
        course=CourseModel.objects.all()
        student=StudentModel.objects.all()
        return render(request,'table.html',{'cdata':course,'sdata':student})


#..........................................................................................................................................

def addStudent(request):
    courses=CourseModel.objects.all()
    context={'courses':courses}
    return render(request,'signup.html',context)


def show_student(request):
    products=TeacherModel.objects.all()
    return render(request,'showTable1.html',{'product':products})        
        
def show_students(request):
    products=TeacherModel.objects.get(teacher=request.user)
    return render(request,'showTable.html',{'product':products})

def trialedit(request):
    return render(request,'trialedit.html')

def editpage(request):
    products=TeacherModel.objects.get(teacher=request.user)
    courses=CourseModel.objects.all()
    return render(request,'trialedit.html',{'products':products,'courses':courses})



def edit_student_details(request,pk):
    if request.method=='POST':
        products = TeacherModel.objects.get(id=pk)

        products = TeacherModel.objects.get(id=pk)
        old=products.image
        new=request.FILES.get('file')
        if old !=None and new==None:
            products.image=old
        else:
            products.image=new

        products.first_name = request.POST.get('first_name')
        products.last_name = request.POST.get('last_name')
        products.email = request.POST.get('email')
        products.phone_number = request.POST.get('phone_number')
        products.address = request.POST.get('address')
        products.gender = request.POST.get('gender')
        products.age = request.POST.get('age')
        products.course = request.POST.get('course')
        products.save()
        return redirect('show_students')
    return render(request, 'trialedit.html',)



#def delete_student(request,pk):
#    product=TeacherModel.objects.get(id=pk)
#    product.delete()
#    return redirect('show_students')