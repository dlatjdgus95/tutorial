from django.shortcuts import render
from django.http import HttpResponse
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
    