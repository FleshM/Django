from django.shortcuts import render
from app1.models import Paragraph


def index_page(request):
    data = {
        'paragraphs': Paragraph.objects.all()
    }
    return render(request, 'index.html', context=data)


def demand_page(request):
    return render(request, 'demand.html')


def geography_page(request):
    return render(request, 'geography.html')

