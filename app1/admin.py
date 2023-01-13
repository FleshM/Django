from django.contrib import admin
from app1.models import DemandPage, GeographyPage, Paragraph, AnalyticsByYear, \
    SalaryByCity, VacanciesByCity, Skills, Years, SkillsPage, VacanciesPage


class SkillsAdmin(admin.ModelAdmin):
    list_display = ('year', 'title', 'count')


admin.site.register(Paragraph)
admin.site.register(DemandPage)
admin.site.register(AnalyticsByYear)
admin.site.register(GeographyPage)
admin.site.register(SalaryByCity)
admin.site.register(VacanciesByCity)
admin.site.register(Years)
admin.site.register(Skills, SkillsAdmin)
admin.site.register(SkillsPage)
admin.site.register(VacanciesPage)
