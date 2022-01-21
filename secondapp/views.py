from django.shortcuts import render ,redirect
from django.http import HttpResponse

from secondapp.forms import CourseForm
from .models import Course, Armyshop
# Create your views here.
def main(request):
    return HttpResponse('<u>Main</u>')
# Create your views here.
def insert(request):
    Course(name='데이터 분석',cnt=30).save()
    Course(name='데이터 수집',cnt=20).save()
    Course(name='웹개발',cnt=25).save()
    Course(name='인공지능',cnt=20).save()
    return HttpResponse('데이터 입력 완료')
def show(request):
    course = Course.objects.all()
    return render(
        request, 'secondapp/show.html',
        { 'data': course }
    )
def army_shop(request):
    prd = request.GET.get('prd','')
    a = Armyshop.objects.filter(name__contains=prd)

    return render(
        request, 
        'secondapp/army_shop.html',
        { 'data' : a}
    )
def army_shop2(request,year,month):
    shop = Armyshop.objects.filter(year = year, month=month)
    #result = ''
    #for i in shop:
    #    result += '%s %s %s<br>' % (i.year,i.month,i.name)
    result = ['%s %s %s<br>' % (i.year,i.month,i.name) for i in shop ]
    return HttpResponse(''.join(result))
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.forms.models import model_to_dict
@csrf_exempt
def ajaxGet(request):
    # QuerySet []
    c = Course.objects.all()

    data = []
    # model_to_dict - 조회된 데이터를 dict 형태로 변경
    for a in c :
        d = model_to_dict(a)
        data.append(d)

    return JsonResponse()
def ajaxPost(request):
     return JsonResponse()
def ajaxExam(request):
    return render(request,'secondapp/ajax_exam.html')
from secondapp.forms import CourseForm
def course_create(request):
    if request.method == 'POST':

        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.save()

            return redirect('firstapp:post')
        else:
            form = CourseForm()

    return render(request, 'secondapp/course_create.html',{'form' : form} )