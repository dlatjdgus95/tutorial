from django.shortcuts import render
from .models import Shop, Jeju
# Create your views here.
def shop(request):
    shop_list = Shop.objects.all()
    
    return render(
        request,
        'thirdapp/shop.html',
        {'shop_list': shop_list}
)
def jeju(request):
    jeju_olle_list = Jeju.objects.all()

    return render(
        request,
        'thirdapp/jeju_olle.html',
        {'jeju_olle_list' : jeju_olle_list}
    )