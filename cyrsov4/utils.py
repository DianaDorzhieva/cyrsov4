import os

def get_key():
    env_var = os.environ
    env_var['YT_API_KEY'] = 'v3.r.137919263.2e22fa9bb853f205db171302e1df412c4a786323.4246fea0db40dc88277ced580949608429ebe4fd'
    return os.getenv('YT_API_KEY')

def create_user_vacanci_Hh():
    print("Добрый день, введите интересующую вакансию")
    user_name = input()
    print("Добрый день, введите страницу поиска")
    user_page = input()
    print("Добрый день, введите количество вакансий")
    user_per_page = input()
    user_vacanci = Hh(user_name,user_page, user_per_page)
    return user_vacanci


def create_user_vacanci_Sj():
    print("Добрый день, введите интересующую вакансию")
    user_name = input()
    print("Добрый день, введите страницу поиска")
    user_page = input()
    print("Добрый день, введите количество вакансий")
    user_per_page = input()
    user_vacanci = Super_Job(user_name,user_page, user_per_page)
    return user_vacanci