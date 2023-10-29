import requests      # Для запросов по API
import json          # Для обработки полученных результатов
from utils import get_key
from abc import ABC, abstractmethod

class Vacancies(ABC):
    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass

class Hh(Vacancies):
    """ Класс для работы с Хэнд Хантер"""

    def __init__(self,name,page,per_page):
        self.hh = 'https://api.hh.ru/vacancies'
        self.name = name
        self.page = page
        self.per_page = per_page


    def get_info(self):
        info = requests.get(self.hh, params={'text': self.name, 'page': self.page, 'per_page': self.per_page}).json()['items']
        return info

    def get_vacancies(self):
        info = self.get_info()
        all_vacancies = []
        try:
            for vacanci in info:
                if vacanci['salary']:
                    salary_from = vacanci['salary']['from'] if vacanci['salary']['from'] else 0
                    salary_to = vacanci['salary']['to'] if vacanci['salary']['to'] else 0
                else:
                    salary_from = 0
                    salary_to = 0
                if vacanci['snippet']['requirement']:
                    description_vacanci = vacanci['snippet']['requirement'] if vacanci['snippet']['requirement'] else f"Нет описания вакансии"
                all_vacancies.append({
                    'name': vacanci['name'],
                    'url': vacanci['alternate_url'],
                    'salary from': salary_from,
                    'salary to': salary_to,
                    'adress': vacanci['area']['name'],
                    'description': description_vacanci
                    })
        except KeyError:
            print("По данным критериям нет вакансий")
        if all_vacancies == []:
            print("Нет такой вакансии")
        return all_vacancies



class Super_Job(Vacancies):
        def __init__(self, name, page, per_page):
            self.name = name
            self.page = page
            self.per_page = per_page
            self.sj = 'https://api.superjob.ru/2.0/vacancies'

        def get_info(self):
            key = get_key()
            try:
                info = requests.get(self.sj, headers={'X-Api-App-Id': key}, params={'keyword': self.name, 'page': self.page, 'count': self.per_page}).json()['objects']
            except KeyError:
                print("По данным кретериям не нашлось вакансий")
            return info

        def get_vacancies(self):
            all_vacancies = []
            try:
                info = self.get_info()
                for vacanci in info:
                    for vacanci in info:
                        if vacanci['payment_from']:
                            salary_from = vacanci['payment_from'] if vacanci['payment_from'] else 0
                            salary_to = vacanci['payment_to'] if vacanci['payment_to'] else 0
                        else:
                            salary_from = 0
                            salary_to = 0
                    all_vacancies.append({
                        'name': vacanci['profession'],
                        'url': vacanci['client']['url'],
                        'salary from': salary_from,
                        'salary to': salary_to,
                        'adress': vacanci['address'],
                        'description': vacanci['candidat']
                    })
            except KeyError:
                print("По данным кретериям не нашлось вакансий")
            if all_vacancies == []:
                print("нет такой вакансии")
            return all_vacancies

class Vanancy:
    def __init__(self, name, url, salary_from, salary_to, adress, description):
        self.name = name
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        """Проверка для случая, когда зп указана только в ячейке до. 
            Понадобится для последующей сортировки"""
        if self.salary_from < self.salary_to:
            self.salary_from = self.salary_to
        self.adress = adress
        self.description = description


    def __str__(self):
        if self.salary_from == 0:
            self.salary_from = "Зарплата не указана"
        return f"Вакансия : {self.name}\nСайт : {self.url}\nЗарплата : {self.salary_from}"


    def __repr__(self):
        return self.name

    def __lt__(self, other):
        return self.salary_from < other.salary_from

    def __gt__(self, other):
        return self.salary_from > other.salary_from


class JsonSave:
    def __init__(self, filename):
        self.filename = filename

    def write_data(self, data):
        with open(f"{self.filename}.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def write_all_data(self, data):
        with open(f"{self.filename}.json", "a+", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def get_all_vacanci(self):
        with open(f"{self.filename}.json", encoding="utf-8") as f:
            data = json.load(f)
        all_vacanci = []
        for vacanci in data:
            all_vacanci.append(Vanancy(vacanci['name'],
                                       vacanci['url'],
                                       vacanci['salary from'],
                                       vacanci['salary to'],
                                       vacanci['adress'],
                                       vacanci['description']))
        return all_vacanci

def create_user_vacanci_Hh():
    print("Добрый день, введите интересующую вакансию")
    user_name = input()
    print("Добрый день, введите страницу поиска")
    user_page = input()
    print("Добрый день, введите количество вакансий")
    user_per_page = input()
    user_vacanci = Hh(user_name,user_page, user_per_page).get_vacancies()
    return user_vacanci

def create_user_vacanci_Sj():
    print("Добрый день, введите интересующую вакансию")
    user_name = input()
    print("Добрый день, введите страницу поиска")
    user_page = input()
    print("Добрый день, введите количество вакансий")
    user_per_page = input()
    user_vacanci = Super_Job(user_name,user_page, user_per_page).get_vacancies()
    return user_vacanci

def create_user_JsonSave():
    user_js = JsonSave("Hand_Hunter")
    user_js.write_data(vac_hh)
    all_vakanci = user_js.get_all_vacanci()
    return all_vakanci

def create_user_JsonSave_SJ():
    user_js = JsonSave("Super_Job")
    user_js.write_data(vac_sj)
    all_vakanci = user_js.get_all_vacanci()
    return all_vakanci

user_info = "1 - вывод вакансий, 2 - вывод вакансий в сортированном виде от увелечения зп,3 - вывод вакансий в сортированном виде от уменьшения зп, 4 - вывод топ зп"

while True:
    print("Выбирите платформу для поиска вакансии: Hh - 1, SJ - 2, обе - 3, выход - 4")
    choice_user = input()
    if int(choice_user) == 1:
        vac_hh = create_user_vacanci_Hh()
        user_JsonSave = create_user_JsonSave()
        print(user_info)
        choice_user_pay = input()
        if int(choice_user_pay) == 1:
            for i in user_JsonSave:
                print(i)
        elif int(choice_user_pay) == 2:
            user_JsonSave = sorted(user_JsonSave)
            for i in user_JsonSave:
                print(i)
        elif int(choice_user_pay) == 3:
            user_JsonSave = sorted(user_JsonSave, reverse=True)
            for i in user_JsonSave:
                print(i)
        elif int(choice_user_pay) == 4:
            user_JsonSave = sorted(user_JsonSave, reverse=True)
            count_top = input(f"Введите количество топ проффесий из {len(user_JsonSave)}")
            for i in range(int(count_top)):
                print(user_JsonSave[i])
        else:
            print("нет такого функционала")

    elif int(choice_user) == 2:
        vac_sj = create_user_vacanci_Sj()
        user_JsonSave = create_user_JsonSave_SJ()
        print(user_info)
        choice_user_pay = input()
        if int(choice_user_pay) == 1:
            for i in user_JsonSave:
                print(i)
        elif int(choice_user_pay) == 2:
            user_JsonSave = sorted(user_JsonSave)
            for i in user_JsonSave:
                print(i)
        elif int(choice_user_pay) == 3:
            user_JsonSave = sorted(user_JsonSave, reverse=True)
            for i in user_JsonSave:
                print(i)
        elif int(choice_user_pay) == 4:
            user_JsonSave = sorted(user_JsonSave, reverse=True)
            count_top = input(f"Введите количество топ проффесий из {len(user_JsonSave)}")
            for i in range(int(count_top)):
                print(user_JsonSave[i])
        else:
            print("нет такого функционала")

    elif int(choice_user) == 3:
        print("Данные для Hh")
        vac_hh = create_user_vacanci_Hh()
        print("Данные для Sj")
        vac_sj = create_user_vacanci_Sj()
        user_JsonSave1 = create_user_JsonSave()
        user_JsonSave2 = create_user_JsonSave_SJ()
        all_JsonSave = user_JsonSave1 + user_JsonSave2
        print(user_info)
        choice_user_pay = input()
        if int(choice_user_pay) == 1:
            for i in all_JsonSave:
                print(i)
        elif int(choice_user_pay) == 2:
            user_JsonSave = sorted(all_JsonSave)
            for i in user_JsonSave:
                print(i)
        elif int(choice_user_pay) == 3:
            user_JsonSave = sorted(all_JsonSave, reverse=True)
            for i in user_JsonSave:
                print(i)
        elif int(choice_user_pay) == 4:
            user_JsonSave = sorted(all_JsonSave, reverse=True)
            count_top = input(f"Введите количество топ проффесий из {len(user_JsonSave)}")
            for i in range(int(count_top)):
                print(user_JsonSave[i])
        else:
            print("нет такого функционала")

    elif int(choice_user) == 4:
        break
    else:
        print("Нет такого функционала")













