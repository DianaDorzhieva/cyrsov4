from Vacanci import Super_Job, Hh, JsonSave

user_info = "1 - вывод вакансий, 2 - вывод вакансий в сортированном виде от увелечения зп,3 - вывод вакансий в сортированном виде от уменьшения зп, 4 - вывод топ зп"


def create_user_vacanci_Sj():
    print("Добрый день, введите интересующую вакансию")
    user_name = input()
    print("Добрый день, введите страницу поиска")
    user_page = input()
    print("Добрый день, введите количество вакансий")
    user_per_page = input()
    user_vacanci = Super_Job(user_name, user_page, user_per_page).get_vacancies()
    return user_vacanci


def create_user_vacanci_Hh():
    print("Добрый день, введите интересующую вакансию")
    user_name = input()
    print("Добрый день, введите страницу поиска")
    user_page = input()
    print("Добрый день, введите количество вакансий")
    user_per_page = input()
    user_vacanci = Hh(user_name, user_page, user_per_page).get_vacancies()
    return user_vacanci


def create_user_JsonSave(vac_hh):
    user_js = JsonSave("Hand_Hunter")
    user_js.write_data(vac_hh)
    all_vakanci = user_js.get_all_vacanci()
    return all_vakanci


def create_user_JsonSave_SJ(vac_sj):
    user_js = JsonSave("Super_Job")
    user_js.write_data(vac_sj)
    all_vakanci = user_js.get_all_vacanci()
    return all_vakanci


def user_print(JsonSave):
    for i in JsonSave:
        print(i)


def choose_prof(user_JsonSave):
    print(user_info)
    choice_user_pay = input()
    if int(choice_user_pay) == 1:
        user = user_print(user_JsonSave)
    elif int(choice_user_pay) == 2:
        user_JsonSave = sorted(user_JsonSave)
        user = user_print(user_JsonSave)
    elif int(choice_user_pay) == 3:
        user_JsonSave = sorted(user_JsonSave, reverse=True)
        user = user_print(user_JsonSave)
    elif int(choice_user_pay) == 4:
        user_JsonSave = sorted(user_JsonSave, reverse=True)
        count_top = input(f"Введите количество топ проффесий из {len(user_JsonSave)}")
        for i in range(int(count_top)):
            print(user_JsonSave[i])
    else:
        print("нет такого функционала")
