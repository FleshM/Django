import pandas as pd

skills_by_year = {year: {} for year in range(2015, 2023)}

class Vacancy:
    def __init__(self, vac):
        self.name = vac['name']
        self.year = int(vac['published_at'].split('-')[0])
        self.required = vac['required']

        if self.required == '+':
            if pd.notna(vac['key_skills']):
                self.key_skills = str(vac['key_skills']).split('\n')
                for skill in self.key_skills:
                    if skill in skills_by_year[self.year]:
                        skills_by_year[self.year][skill] += 1
                    else:
                        skills_by_year[self.year][skill] = 1


df = pd.read_csv("vacancies.csv")
for index, row in df.iterrows():
    Vacancy(row)

for year in skills_by_year.keys():
    skills_by_year[year] = dict(sorted(skills_by_year[year].items(), key=lambda x: x[1], reverse=True))
    skills_by_year[year] = dict(list(skills_by_year[year].items())[:10])

print(skills_by_year)