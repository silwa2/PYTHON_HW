class OwnException(Exception):
    pass


class LevelError(OwnException):
    def __init__(self, user_level, admin_level):
        self.user_level = user_level
        self.admin_level = admin_level

    def __str__(self):
        return f'''Доступ закрыт!
Ваш уровень доступа({self.user_level}) должен быть ниже уровеня доступа администратора({self.admin_level})'''


class NotAllowedError(OwnException):
    def __init__(self, name, u_id):
        self.name = name
        self.u_id = u_id

    def __str__(self):
        return f'''Доступ закрыт!
Пользователь {self.name}/{self.u_id} не найден.'''

class AdminNotFoundError(OwnException):
    def __str__(self):
        return '''Доступ закрыт!
Администратор не найден!'''