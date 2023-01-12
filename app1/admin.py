from django.contrib import admin
from app1.models import DemandPage, GeographyPage, Paragraph, AnalyticsByYear, SalaryByCity, VacanciesByCity


admin.site.register(Paragraph)
admin.site.register(DemandPage)
admin.site.register(AnalyticsByYear)
admin.site.register(GeographyPage)
admin.site.register(SalaryByCity)
admin.site.register(VacanciesByCity)



