from django.shortcuts import render
from django.http import HttpResponse
from pandas import pandas as pd

# Create your views here.


def index(request):
    df = pd.read_csv("C:\\Users\\Shohel\\Desktop\\weather.csv")
    context = {
        "data": df.to_json()
    }
    return render(request, 'uishow/index.html', context)
