from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def about_me_view(request):
    if request.method == "GET":
        return HttpResponse("Меня зовут Максат.")

def love_authors_view(request):
    if request.method == "GET":
        return HttpResponse("Мои любимые писатели: \n\n Пушкин\nЛавкрафт\nДостоевский")

def live_time_view(request):
    if request.method == "GET":
        live_time = datetime.now()
        return HttpResponse(live_time)