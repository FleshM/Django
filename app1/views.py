from django.shortcuts import render
from app1.models import Paragraph, DemandPage


def index_page(request):
    data = {
        'paragraphs': Paragraph.objects.all()
    }
    return render(request, 'index.html', context=data)


def demand_page(request):
    data = {
        'paragraphs': DemandPage.objects.all()
    }
    return render(request, 'demand.html', context=data)


def geography_page(request):
    return render(request, 'geography.html')

