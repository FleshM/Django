from django.shortcuts import render
from app1.models import Paragraph, DemandPage, GeographyPage, AnalyticsByYear, \
    SalaryByCity, VacanciesByCity, Years, Skills, SkillsPage


def index_page(request):
    data = {
        'paragraphs': Paragraph.objects.all()
    }
    return render(request, 'index.html', context=data)


def demand_page(request):
    data = {
        'paragraphs': DemandPage.objects.all(),
        'analytics': AnalyticsByYear.objects.all()
    }
    return render(request, 'demand.html', context=data)


def geography_page(request):
    data = {
        'paragraphs': GeographyPage.objects.all(),
        'salary_by_city': SalaryByCity.objects.all(),
        'vacancies_by_city': VacanciesByCity.objects.all(),
    }
    return render(request, 'geography.html', context=data)


def skills_page(request):
    data = {
        'paragraphs': SkillsPage.objects.all(),
        'skills': Skills.objects.all(),
        'years': Years.objects.all()
    }
    return render(request, 'skills.html', context=data)
