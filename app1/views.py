import requests
import json
import pandas as pd
from django.shortcuts import render
from app1.models import Paragraph, DemandPage, GeographyPage, AnalyticsByYear, \
    SalaryByCity, VacanciesByCity, Years, Skills, SkillsPage, VacanciesPage


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


def vacancies_page(request):
    params = {
        'text': 'NAME:Веб',
        'per_page': 10,
        'professional_role': 96,
        'only_with_salary': True,
        'period': 3,
        'order_by': 'publication_time'
    }
    req = requests.get('https://api.hh.ru/vacancies', params)
    data = req.content.decode()
    req.close()
    data = json.loads(data)

    list_vacancies = []

    for vac in data['items']:
        name = vac['name']
        city = vac['area']['name']
        company = vac['employer']['name']

        if pd.notna(vac['salary']['from']) and pd.notna(vac['salary']['to']):
            salary = '{0:,} - {1:,} {2}'.format(
                vac['salary']['from'], vac['salary']['to'], vac['salary']['currency']).replace(',', ' ')
        elif pd.notna(vac['salary']['from']):
            salary = 'от {0:,} {1}'.format(vac['salary']['from'], vac['salary']['currency']).replace(',', ' ')
        else:
            salary = 'до {0:,} {1}'.format(vac['salary']['to'], vac['salary']['currency']).replace(',', ' ')

        published_at = vac['published_at'].split('T')
        date = published_at[0].split('-')
        date.reverse()
        date = '.'.join(date)
        time = published_at[1][0:5]
        vac_url = str(vac['alternate_url'])

        list_vacancies.append({
            'name': name,
            'city': city,
            'salary': salary,
            'company': company,
            'time': time,
            'date': date,
            'vac_url': vac_url
        })

    vacancies = {
        'paragraphs': VacanciesPage.objects.all(),
        'vacancies': list_vacancies
    }
    return render(request, 'vacancies.html', context=vacancies)
