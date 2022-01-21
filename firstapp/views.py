from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Curriculum
from .forms import CurriculumForm
def index1(request):
    return HttpResponse('<u>Hello</u>')
def index2(request):
    return HttpResponse('<u>Hi</u>')
def main(request):
    return HttpResponse('<u>Main</u>')
def home(request):
    return HttpResponse('<u>Home</u>')
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
def req_get(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET['c']
    result = '%s %s %s' % (a, b, c)
    return HttpResponse(result)
def req_post(request):
    if request.method == 'POST':
        a = request.POST.get('a')
        b = request.POST.get('b')
        c = request.POST['c']
        result = '%s %s %s' % (a, b, c)
        return HttpResponse(result)
    return render(request, 'firstapp/post.html')
def req_ajax4(request):
    return render(request, 'firstapp/ajax4.html')
def static(request):
    return render(request, 'firstapp/post.html')
def var(request):
    data = {
        'str': 'text', 'num': 10,
        'list': [1, 2, 3],
        'dict': {'a': 'aaa', 'b': 'bbb'}
    }
    return render(
        request, 'firstapp/var.html', data)
def tag(request):
    persons = [
        { 'num': 1, 'name': 'Park', 'score': 100 },
        { 'num': 2, 'name': 'Choi', 'score': 70 },
        { 'num': 3, 'name': 'Kim', 'score': 80 }
    ]   
    animals = ['Cat', 'Dog']
    context = {
        'persons': persons,
        'animals': animals
    }
    return render(
        request, 'firstapp/tag.html', context)
import datetime
def filter(request):
    context = {
        'title': 'Simple Python', 'num': 10,
        'price': 39800.5,
        'animals': ['삵', '칡', '타조', '낙타'],
        'covid': datetime.datetime(2020, 1, 8)
    }
    return render(request, 'firstapp/filter.html', context)

def custom_filter(request):
    context = { 'price': 39800.5 }
    return render(request, 'firstapp/custom_filter.html', context)

def template(request):
    return render(
        request, 'firstapp/template.html')
from .forms import NameForm
def form_basic(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid(): # 유효성 검사 결과가 True 이면
            your_name = form.cleaned_data['your_name']
            print(your_name)
            # 데이터베이스 저장, 이메일 발송 등
            return redirect('/first/form/basic/')
    else:
        form = NameForm()
    return render(
        request, 'firstapp/form_basic.html',
        { 'form': form }
    )
def form_model(request):
    if request.method == 'POST':
        form = CurriculumForm(request.POST)
        if form.is_valid():

            curriculum = form.save(commit=False)
            # (필요하다면) 데이터 추가 / 변경
            curriculum.save()
            
            return redirect('/first/form/model/')
    else:
        form = CurriculumForm()
    return render(
        request, 'firstapp/form_model.html',
        { 'form': form }
    )