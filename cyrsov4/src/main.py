from utils import create_user_vacanci_Sj, \
    create_user_JsonSave, create_user_JsonSave_SJ, \
    create_user_vacanci_Hh, choose_prof

while True:
    print("Выбирите платформу для поиска вакансии: Hh - 1, SJ - 2, обе - 3, выход - 4")
    choice_user = input()
    while True:
        if int(choice_user) == 1:
            vac_hh = create_user_vacanci_Hh()
            if vac_hh != []:
                user_JsonSave = create_user_JsonSave(vac_hh)
                user_info = choose_prof(user_JsonSave)
            else:
                break

        elif int(choice_user) == 2:
            vac_sj = create_user_vacanci_Sj()
            if vac_sj != []:
                user_JsonSave = create_user_JsonSave_SJ(vac_sj)
                user_info = choose_prof(user_JsonSave)
            else:
                break

        elif int(choice_user) == 3:
            print("Данные для Hh")
            vac_hh = create_user_vacanci_Hh()
            print("Данные для Sj")
            vac_sj = create_user_vacanci_Sj()
            if vac_sj != [] and vac_hh != []:
                user_JsonSave1 = create_user_JsonSave(vac_hh)
                user_JsonSave2 = create_user_JsonSave_SJ(vac_sj)
                all_JsonSave = user_JsonSave1 + user_JsonSave2
                user_info = choose_prof(all_JsonSave)
            else:
                break
        elif int(choice_user) == 4:
            break
        else:
            print("Нет такого функционала")
