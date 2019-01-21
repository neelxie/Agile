users = []


class User:
    """class Users"""

    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def user_to_dict(self):
        """class Users"""

        return{
            "username": self.username,
            "password": self.password,
            "role": self.role
        }

    def save_users(self, user):
        users.append(user)

    def user_login(self, username, password):
        for user in users:
            if user["username"] == username and user["password"] == password:
                return True
            return False

    @staticmethod
    def search_user(username):
        for user in users:
            if user["username"] == username:
                return user
            else:
                return username + ' was not found'
