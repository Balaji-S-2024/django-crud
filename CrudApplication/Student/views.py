from django.shortcuts import render, redirect
from .models import Student
from django.contrib import messages

# Create your views here.
def index(request):
    students = Student.objects.all()
    context = { "students" : students}
    return render(request, 'index.html', context=context)

def insert(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        print(name, age, email, gender)
        query = Student(stu_name = name, stu_email = email, stu_age = age, stu_gender = gender)
        query.save()
        messages.info(request, "Data Inserted !")
        return redirect("/")
    return render(request, 'index.html')

def update(request, stu_id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        stu = Student.objects.get(stu_id = stu_id)
        stu.stu_name = name
        stu.stu_age = age
        stu.stu_email = email
        stu.stu_gender = gender
        stu.save()
        messages.warning(request,"Data Updated !")
        return redirect("/")
    student = Student.objects.get(stu_id = stu_id)
    context = {'student' : student}
    return render(request, "update.html", context=context)

def delete(request, stu_id):
    student = Student.objects.get(stu_id = stu_id)
    student.delete()
    messages.error(request,"Data deleted !")
    return redirect("/")
    