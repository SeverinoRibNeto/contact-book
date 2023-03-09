import sqlite3


class Person:
    # Declarations of variables to class Person
    tableName = "contacts"
    headerColumns = ['name',
                     'lastName',
                     'birthday',
                     'phoneNumber',
                     'email',
                     'address']
    id = 0
    # Method to inicializate

    def __init__(self, name: str = None, phoneNumber: str = None,
                 lastName: str = None, birthday=None,
                 email: str = None, address: str = None):
        self.name = name
        self.lastName = lastName
        self.birthday = birthday
        self.phoneNumber = phoneNumber
        self.email = email
        self.address = address
        self.database = "contact-book.db"
        # Create a connection with database and open it
        try:
            self.conn = sqlite3.connect(self.database)
            self.cursor = self.conn.cursor()
        except Exception as exception:
            print(exception)
    # Return name of Person

    def __str__(self):
        return f'{self.name}'

    # Transform values in list
    def dataToList(self):
        listValues = []
        listValues.append(self.name)
        listValues.append(self.lastName)
        listValues.append(self.birthday)
        listValues.append(self.phoneNumber)
        listValues.append(self.email)
        listValues.append(self.address)
        return listValues

    # Return if table exists into sys. True if exists
    def tableExists(self, tableName: str) -> bool:
        tableList = []
        try:
            tables = self.cursor.execute(
                """SELECT name FROM sqlite_master WHERE type='table';"""
            ).fetchall()
            # Sort names in list
            for table in tables:
                for name in table:
                    tableList.append(name)
            # check table in list
            if (tableName in tableList):
                return True
        except Exception as exception:
            print(exception)
        return False

    # Return the last id inserted into table
    def lastIdInserted(self, tableName: str) -> int:
        if(not self.tableExists(tableName)):
            raise ValueError("Table '" + tableName + "' not exists")

        data = self.cursor.execute(f"""
                SELECT id
                FROM {tableName}
                WHERE   ID = (SELECT MAX(ID)  FROM {tableName});
                """).fetchone()
        return int(data[0])

    # method to save person into database
    def save(self) -> bool:
        columnsTable = '('
        valuesList = '('
        # Organize the values into parentheses
        for column in self.headerColumns:
            columnsTable += column + ','
        columnsTable = columnsTable[:-1] + ')'

        for value in self.dataToList():
            valuesList += f"'{value}',"
        valuesList = valuesList[:-1] + ")"
        # test table exists
        if(not self.tableExists(self.tableName)):
            raise ValueError("Table '" + self.tableName + "' not exists")

        code = f"""INSERT INTO {self.tableName}
                {columnsTable}
                VALUES {valuesList};"""
        try:
            self.cursor.execute(code)
            self.conn.commit()
        except Exception as exception:
            print(exception)
        return True

    # Method to find person
    def find(self):
        if(not self.tableExists(self.tableName)):
            raise ValueError("Table '" + self.tableName + "' not exists")
        data = self.cursor.execute(
            f"""
               SELECT * FROM {self.tableName} WHERE id={id};
            """
        )
        data = data.fetchone()
        self.id = data[0]
        self.name = data[1]
        self.lastName = data[2]
        self.email = data[3]
        self.phoneNumber = data[4]
        self.address = data[5]
        self.birthday = data[6]
        return True

    # method to find by name. Return all persons same name
    def findByName(self, name):
        if(not self.tableExists(self.tableName)):
            raise ValueError("Table '" + self.tableName + "' not exists")
        data = self.cursor.execute(
            f"""
               SELECT * FROM {self.tableName} WHERE name='{name}';
            """
        ).fetchall()
        return data

    def dataToTupleList(self, data):
        newData = []
        return newData

    # Delete a person into database
    def delete(self):
        if(not self.tableExists(self.tableName)):
            raise ValueError("Table '" + self.tableName + "' not exists")
        self.cursor.execute(f"""
            DELETE FROM {self.tableName}
            WHERE id = {self.id};
                """)
        self.conn.commit()
        return True

    # alter person into database
    def alter(self):
        values = self.dataToList()
        if(not self.tableExists(self.tableName)):
            raise ValueError("Table '" + self.tableName + "' not exists")
        strCode = ''
        for cont in range(len(self.headerColumns)):
            strCode += f"{self.headerColumns[cont]} = '{values[cont]}',"
        strCode = strCode[:-1]
        self.cursor.execute(f"""
                UPDATE {self.tableName}
                SET {strCode}
                WHERE id = {self.id};
                """)
        self.conn.commit()
        return True


"""
if __name__ == "__main__":
    pessoa = Person("Cida", "4654654")
    pessoa.id = 2
    pessoa.find()
"""
