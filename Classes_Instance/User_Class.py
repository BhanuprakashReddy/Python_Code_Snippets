
class User:
    """A sample user class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        print('Created User: Full Name: {} - Email: {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


user_1 = User('Bhanu', 'Prakash')