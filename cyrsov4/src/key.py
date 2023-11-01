import os


def get_key():
    env_var = os.environ
    env_var[
        'YT_API_KEY'] = 'v3.r.137919263.2e22fa9bb853f205db171302e1df412c4a786323.4246fea0db40dc88277ced580949608429ebe4fd'
    return os.getenv('YT_API_KEY')
