class User:

    def __init__(self, username, password, db):
        self.username = username
        self.password = password
        self.db = db
        self.valid_user = self.authenticate_self()
        self.email = 'kovacst.elod@gmail.com'

    def authenticate_self(self):
        query = 'SELECT user_name ' \
                'FROM users ' \
                'WHERE user_name = \'{}\' AND user_password = \'{}\''.format(self.username, self.password)
        return len(self.db.find_all(query)) > 0

    def is_valid(self):
        return self.valid_user

    def get_email(self):
        return self.email
