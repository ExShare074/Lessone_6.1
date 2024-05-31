#Разработай систему управления учетными записями пользователей для небольшой компании. Компания разделяет сотрудников
#на обычных работников и администраторов. У каждого сотрудника есть уникальный идентификатор (ID), имя и
#уровень доступа. Администраторы, помимо обычных данных пользователей, имеют дополнительный
#уровень доступа и могут добавлять или удалять пользователя из системы.
class User():
    def __init__(self, user_id, name, access_level='user'):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = access_level

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, 'admin')
        self.__users_list = []

    def add_user(self, user):
        self.__users_list.append(user)
        print(f'Пользователь {user.get_name()} добавлен.')

    def remove_user(self, user):
        self.__users_list.remove(user)
        print(f'Пользователь {user.get_name()} удален.')

    def get_users_list(self):
        return self.__users_list


# Пример использования
user1 = User(1, 'Андрей')
user2 = User(2, 'Владимир')
admin = Admin(3, 'Admin')

admin.add_user(user1)
admin.add_user(user2)

print(admin.get_users_list())

admin.remove_user(user1)

print(admin.get_users_list())
