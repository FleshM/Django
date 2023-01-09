from django.shortcuts import render
from app1.models import Profession


def index_page(request):
    data = {
        'profession': Profession.objects.get(id=1)
    }
    return render(request, 'index.html', context=data)
