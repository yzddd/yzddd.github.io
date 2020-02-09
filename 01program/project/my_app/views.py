from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse("yzd is a good man")
def detail(request,num):
    return HttpResponse("detail-%s"%num)

from .models import Grades,Students
def grades(request):
    # 去模版里取数据
    gradesList = Grades.objects.all()
    # 将数据传递给模板，模板在渲染页面，将渲染好的页面返回给浏览器
    return render(request,'my_app/grades.html',{"grades":gradesList})

def students(request):
    # 去模版里取数据
    studentsList = Students.objects.all()
    # 将数据传递给模板，模板在渲染页面，将渲染好的页面返回给浏览器
    return render(request,'my_app/students.html',{"students":studentsList})
