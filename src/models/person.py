class Person:

    def __init__(self, name: str, phoneNumber: str, lastName: str = None,
                 birthday=None,  email: str = None, address: str = None):
        self.name = name
        self.lastName = lastName
        self.birthday = birthday
        self.phoneNumber = phoneNumber
        self.email = email
        self.address = address

    def completeName(self):
        return f'{self.name} {self.lastName}'

    def savePerson(self):
        return

    def findPerson(self):
        return
