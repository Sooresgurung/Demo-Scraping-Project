from django.shortcuts import render
from .fetchdata import get_data_url
from django.http import JsonResponse
from .models import ScrapData

# Create your views here.

def mero_lagani(request):
    get_data_url()
    return JsonResponse({"status":200,"success":"Successfully fetch the data"})

def show_mero_lagani(request):
    lagani_datas = ScrapData.objects.all()

    return render(request,'turnover.html',{"lagani_datas":lagani_datas})
