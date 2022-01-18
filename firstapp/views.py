from django.shortcuts import render
from django.http import HttpResponse
from .models import Curriculum
def index1(request):
    return HttpResponse('<u>Hello</u>')
def index2(request):
    return HttpResponse('<u>Hi</u>')
def main(request):
    return HttpResponse('<u>Main</u>')
# Create your views here.
def insert(request):
# 1-linux 입력
    Curriculum.objects.create(name='linux')
# 2-python 입력
    c = Curriculum(name='python')
    c.save()
# 3-html/css/js 입력
    Curriculum(name='python').save()
# 4-django 입력
    Curriculum(name='django').save()
    return HttpResponse('데이터 입력 완료')
def show(request):
    curriculum = Curriculum.objects.all()
    return render(
        request, 'firstapp/show.html',
        { 'data': curriculum }
    )