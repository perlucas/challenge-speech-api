class User:
    def __init__(self, id: str, username: str):
        self.__id = id
        self.__username = username

    def get_id(self):
        return self.__id

    def get_username(self):
        return self.__username
        