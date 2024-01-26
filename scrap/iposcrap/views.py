from django.shortcuts import render
# from .models import ScrapIpo
from .ipofetch import get_data_ipo
from django.http import JsonResponse
from .models import ScrapIpo

# Create your views here.

def ipo_fetch(request):
    get_data_ipo()
    return JsonResponse({"status":200,"success":"Successfully fetch the data"})

def show_upcoming_ipo(request):
    ipo_datas = ScrapIpo.objects.all()

    return render(request,'ipo.html',{"ipo_datas":ipo_datas})
