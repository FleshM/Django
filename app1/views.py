from django.shortcuts import render


def index_page(request):
    return render(request, 'index.html')


def demand_page(request):
    return render(request, 'demand.html')


def geography_page(request):
    return render(request, 'geography.html')

