from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .scraper import scrape_air_quality_data

def air_quality_data(request):
    data = scrape_air_quality_data()
    return JsonResponse(data)