from bd import Database


class Person:
    database = Database()
    tableName = "contacts"
    headerColumns = ['name',
                     'lastName',
                     'birthday',
                     'phoneNumber',
                     'email',
                     'address']
    id = 0

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

    def dataToList(self):
        listValues = []
        listValues.append(self.name)
        listValues.append(self.lastName)
        listValues.append(self.birthday)
        listValues.append(self.phoneNumber)
        listValues.append(self.email)
        listValues.append(self.address)
        return listValues

    def save(self):
        self.database.addIntoTable(
            self.tableName, self.headerColumns, self.dataToList())
        self.id = self.database.lastIdInserted(self.tableName)
        return True

    def find(self):
        data = self.database.findData(self.tableName, self.id)
        self.id = data[0]
        self.name = data[1]
        self.lastName = data[2]
        self.email = data[3]
        self.phoneNumber = data[4]
        self.address = data[5]
        self.birthday = data[6]
        return True

    def delete(self):
        self.database.deleteData(self.tableName, self.id)
        return True

    def alter(self):
        self.database.alterData(self.tableName,
                                self.id,
                                self.headerColumns,
                                self.dataToList())
        return True


if __name__ == "__main__":
    pessoa = Person("Cida", "4654654")
    pessoa.id = 2
    pessoa.find()
