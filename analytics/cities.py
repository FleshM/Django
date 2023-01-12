import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

salary_by_year = {}
vacancies_by_year = {}
salary_by_city = {}
vacancies_by_city = {}

class Vacancy:
    def __init__(self, vac):
        self.name = vac['name']
        self.salary = vac['salary']
        self.year = int(vac['published_at'].split('-')[0])
        self.city = vac['area_name']
        self.required = vac['required']

        if self.required == '+':
            if pd.notna(self.salary):
                if self.year in salary_by_year:
                    salary_by_year[self.year] += self.salary
                else:
                    salary_by_year[self.year] = self.salary

                if self.year in vacancies_by_year:
                    vacancies_by_year[self.year] += 1
                else:
                    vacancies_by_year[self.year] = 1

                if self.city in salary_by_city:
                    salary_by_city[self.city] += self.salary
                else:
                    salary_by_city[self.city] = self.salary

                if self.city in vacancies_by_city:
                    vacancies_by_city[self.city] += 1
                else:
                    vacancies_by_city[self.city] = 1


df = pd.read_csv("../../../Desktop/Python/Pleshivtsev/analytics/vacancies.csv")

for index, row in df.iterrows():
    Vacancy(row)

for year in vacancies_by_year:
    salary_by_year[year] = int(salary_by_year[year] / vacancies_by_year[year])

salary_by_city = {city: salary_by_city[city] / vacancies_by_city[city] for city in salary_by_city}

vac_amount = sum(vacancies_by_city.values())
vacancies_by_city = {city: round(vacancies_by_city[city] / vac_amount, 4) for city in vacancies_by_city}

salary_by_city = {city: int(salary_by_city[city]) for city in salary_by_city if vacancies_by_city[city] > 0.01}
vacancies_by_city = {city: vacancies_by_city[city] for city in vacancies_by_city if vacancies_by_city[city] > 0.01}

salary_by_city = dict(sorted(salary_by_city.items(), key=lambda x: x[1], reverse=True))
vacancies_by_city = dict(sorted(vacancies_by_city.items(), key=lambda x: x[1], reverse=True))

salary_by_city = dict(list(salary_by_city.items())[:10])
vacancies_by_city = dict(list(vacancies_by_city.items())[:10])


print(f'Уровень зарплат по городам (в порядке убывания): {salary_by_city}')
print(f'Доля вакансий по городам (в порядке убывания): {vacancies_by_city}')

width = 0.35
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)

salary_by_city = dict(sorted(salary_by_city.items(), key=lambda x: x[1]))
cities = list(salary_by_city.keys())
for i in range(len(cities)):
    cities[i] = cities[i].replace(' ', '\n')
    cities[i] = cities[i].replace('-', '-\n')

x = np.arange(len(cities))

ax1.barh(x, salary_by_city.values(), width * 2)

ax1.set_title('Уровень зарплат по городам')
ax1.set_yticks(x, cities, fontsize=6)
ax1.grid(axis='x', linestyle='-')

vacancies_by_city = dict(sorted(vacancies_by_city.items(), key=lambda x: x[1]))
cities = list(vacancies_by_city.keys())
cities.append('Другие')
vacancies = list(vacancies_by_city.values())
vacancies.append(1 - sum(vacancies))

ax2.set_title('Доля вакансий по городам')
ax2.pie(vacancies, labels=cities, textprops={'fontsize': 6})
ax2.axis('equal')

fig.set_size_inches(10, 5)
fig.tight_layout()
plt.savefig('cities.png', dpi=300)
