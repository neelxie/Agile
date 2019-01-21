users = []


class User:
    """class User"""

    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def user_to_dict(self):
        """returns user as dictionary"""

        user={
            "username": self.username,
            "password": self.password,
            "role": self.role
        }
        return users.append(user)
  
    def user_login(self, username, password):
        """method for user login"""
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
