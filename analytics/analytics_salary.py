import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

salary_by_year = {}
vacancies_by_year = {}
p_name_salary_by_year = {}
p_name_vacancies_by_year = {}

class Vacancy:
    def __init__(self, vac):
        self.name = vac['name']
        self.salary = vac['salary']
        self.year = int(vac['published_at'].split('-')[0])
        self.required = vac['required']

        if pd.notna(self.salary):
            if self.year in salary_by_year:
                salary_by_year[self.year] += self.salary
            else:
                salary_by_year[self.year] = self.salary

            if self.year in vacancies_by_year:
                vacancies_by_year[self.year] += 1
            else:
                vacancies_by_year[self.year] = 1

            if self.required == '+':
                if self.year in p_name_salary_by_year:
                    p_name_salary_by_year[self.year] += self.salary
                else:
                    p_name_salary_by_year[self.year] = self.salary

                if self.year in p_name_vacancies_by_year:
                    p_name_vacancies_by_year[self.year] += 1
                else:
                    p_name_vacancies_by_year[self.year] = 1


def generate_image():
    labels = salary_by_year.keys()
    x = np.arange(len(labels))
    width = 0.35

    fig, ((ax1), (ax2), (ax3)) = plt.subplots(nrows=3, ncols=1)
    ax1.bar(x - width / 2, salary_by_year.values(), width, label='Средняя З/П')
    ax1.bar(x + width / 2, p_name_salary_by_year.values(), width, label='Средняя З/П - Web-разработчик')

    ax1.set_title('Уровень зарплат по годам')
    ax1.set_xticks(x, labels, rotation=90, fontsize=8)
    ax1.legend(fontsize=8)
    ax1.grid(axis='y', linestyle='-')

    ax2.bar(x, vacancies_by_year.values(), 2 * width, label='Количество вакансий')

    ax2.set_title('Количество вакансий по годам')
    ax2.set_xticks(x, labels, rotation=90, fontsize=8)
    ax2.legend(fontsize=8)
    ax2.grid(axis='y', linestyle='-')

    ax3.bar(x, p_name_vacancies_by_year.values(), 2 * width, label='Количество вакансий')

    ax3.set_title('Количество вакансий по годам - Web-разработчик')
    ax3.set_xticks(x, labels, rotation=90, fontsize=8)
    ax3.legend(fontsize=8)
    ax3.grid(axis='y', linestyle='-')

    fig.set_size_inches(7, 10)
    fig.tight_layout()

    plt.savefig('graph.png', dpi=300)


df = pd.read_csv("vacancies.csv")

for index, row in df.iterrows():
    Vacancy(row)

for year in vacancies_by_year:
    salary_by_year[year] = int(salary_by_year[year] / vacancies_by_year[year])
    p_name_salary_by_year[year] = int(p_name_salary_by_year[year] / p_name_vacancies_by_year[year])

print(f'Динамика уровня зарплат по годам: {salary_by_year}')
print(f'Динамика количества вакансий по годам: {vacancies_by_year}')
print(f'Динамика уровня зарплат по годам для выбранной профессии: {p_name_salary_by_year}')
print(f'Динамика количества вакансий по годам для выбранной профессии: {p_name_vacancies_by_year}')

generate_image()