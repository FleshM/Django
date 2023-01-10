import pandas as pd

names_list = ['web develop', 'веб разработчик', 'web разработчик', 'web programmer', 'web программист', 'веб программист', 'битрикс разработчик', 'bitrix разработчик', 'drupal разработчик', 'cms разработчик', 'wordpress разработчик', 'wp разработчик', 'joomla разработчик', 'drupal developer', 'cms developer', 'wordpress developer', 'wp developer', 'joomla developer']

df = pd.read_csv("vacancies_with_skills. csv")
currency_dates = pd.read_csv("currencies.csv")
currencies = list(currency_dates.columns)[1:len(list(currency_dates.columns))]

def format_name(name):
    flag = False
    for n in names_list:
        if n in name.lower().replace('-', ' '):
            flag = True
            break
    if flag:
        return '+'
    return '-'

def format_salary(date, salary_from, salary_to, currency):
    exchange_rate = 1 if currency == 'RUR' else 0
    if currency in currencies:
        date = f"{date[1]}/{date[0]}"
        exchange_rate = currency_dates.loc[currency_dates["date"] == date][currency].values[0]

    if pd.notna(salary_from) and pd.notna(salary_to):
        return 0.5 * (salary_from + salary_to) * exchange_rate
    elif pd.notna(salary_from):
        return salary_from * exchange_rate
    else:
        return salary_to * exchange_rate

salary = []
for index, row in df.iterrows():
    salary.append(format_salary(row["published_at"][0:7].split("-"), row["salary_from"], row["salary_to"], row["salary_currency"]))

df["required"] = df.apply(lambda r: format_name(r["name"]), axis=1)

df.insert(1, 'salary', salary)
df = df.drop(columns = ['salary_from', 'salary_to', 'salary_currency'])
df.to_csv("vacancies.csv", index=False)
