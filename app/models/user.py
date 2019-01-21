users = []


class User:
    def __int__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def save_users(self, user):
        users.append(user)

    @staticmethod
    def search_user(username):
    for user in users:
        for key in user:
            if user[key] == username:
                return user
            else:
                return username + ' was not found'
