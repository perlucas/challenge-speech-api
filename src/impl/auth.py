from domain.user import User

default_user = User(id='1', username='tester')

def get_current_user(request_headers: dict):
    # TODO: implement basic username/password authentication
    return default_user