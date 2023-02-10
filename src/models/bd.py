import sqlite3


class Database():
    database = "contact-book.db"

    def __init__(self):
        return

    def testConn(self):
        try:
            self.conn = sqlite3.connect(self.database)
            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT SQLITE_VERSION()")
            self.data = self.cursor.fetchone()
            print(f'SQLITE_VERSION: {str(self.data)}')
            self.cursor.close()
            self.conn.close()
        except Exception as exception:
            print(exception)

    def createTable(self):
        try:
            self.conn = sqlite3.connect(self.database)
            self.cursor = self.conn.cursor()
            tabela = self.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                lastName TEXT NOT NULL,
                email TEXT NOT NULL,
                phoneNumber TEXT,
                address TEXT,
                birthday DATE
            );
            """
            ).fetchall()
            print(tabela)
            self.cursor.close()
            self.conn.close()
        except Exception as exception:
            print(exception)

    def tableExists(self, tableName):
        tableList = []
        try:
            self.conn = sqlite3.connect(self.database)
            self.cursor = self.conn.cursor()
            tables = self.cursor.execute(
                """SELECT name FROM sqlite_master WHERE type='table';"""
            ).fetchall()
            self.cursor.close()
            self.conn.close()
            # Sort names in list
            for table in tables:
                for name in table:
                    tableList.append(name)
            # check table in list
            if (tableName in tableList):
                return True
            else:
                return False
        except Exception as exception:
            print(exception)

    def addIntoTable(self, tableName, columnNames, values):

        columnsTable = '('
        valuesList = '('
        # Organize the values into parentheses
        for column in columnNames:
            columnsTable += column + ','
        columnsTable = columnsTable[:-1] + ')'

        for value in values:
            valuesList += value + ","
        valuesList = valuesList[:-1] + ")"


# Tests
if __name__ == "__main__":
    bd = Database()
    # bd.testConn()
    # bd.createTable()
    if(bd.tableExists("testeDeTabela")):
        print("Tem")
    else:
        print("Não tem")

    # bd.addIntoTable(tableName="contacts",
    #                columnNames=['name', 'lastName', 'email'],
    #                values=['Severino', 'Ribeiro', 'teste'])
