
class Person:

    def __init__(self, name, lastName, birthday, phoneNumber, email, adress):
        self.name = name
        self.lastName = lastName
        self.birthday = birthday
        self.phoneNumber = phoneNumber
        self.email = email
        self.adress = adress

    def completeName(self):
        return f'{self.name} {self.lastName}'
