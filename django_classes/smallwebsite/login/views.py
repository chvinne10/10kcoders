from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student
# Create your views here.

def login(request):
    if request.method=='POST':
        name=request.POST.get('student_name')
        age=request.POST.get('age')
        Student.objects.create(student_name=name,age=age)
        return redirect('home')        
    return render(request, 'login.html')
def home(request):
    data=Student.objects.all()
    return render(request,'home.html',{'data':data})
def update(request,id):
    data=Student.objects.get(id=id)
    if request.method=='POST':
        data.student_name=request.POST.get('student_name')
        data.age=request.POST.get('age')
        data.save()
        return redirect('home')
    return render(request,'update.html',{'data':data})
def delete(request):
   
    try:
        if request.method == 'POST':
            id=request.POST.get('id')
            obj = Student.objects.get(id=id)
            obj.delete()
            return redirect('home')

        return render(request, 'delete.html')
    except Student.DoesNotExist:
        return HttpResponse("enetr valid id")

    
   