import sqlite3
from typing import List


class Database():

    def __init__(self, database: str = "contact-book.db"):
        self.database = database
        try:
            self.conn = sqlite3.connect(self.database)
            self.cursor = self.conn.cursor()
        except Exception as exception:
            print(exception)

    def testConn(self) -> None:
        try:
            self.cursor.execute("SELECT SQLITE_VERSION()")
            self.data = self.cursor.fetchone()
            print(f'SQLITE_VERSION: {str(self.data)}')
        except Exception as exception:
            print(exception)

    def createTable(self) -> None:
        try:
            self.cursor.execute(
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
        except Exception as exception:
            print(exception)
    """This function return if table exists."""

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

    """Add data into table.
        - tableName is the name of the table
        - columnNames is a list with column data
        - values is a list of values arranged in column data
    """

    def addIntoTable(self, tableName: str, columnNames: List[str],
                     values: List[str]) -> None:

        columnsTable = '('
        valuesList = '('
        # Organize the values into parentheses
        for column in columnNames:
            columnsTable += column + ','
        columnsTable = columnsTable[:-1] + ')'

        for value in values:
            valuesList += f"'{value}',"
        valuesList = valuesList[:-1] + ")"
        if(not self.tableExists(tableName)):
            raise ValueError("Table '" + tableName + "' not exists")

        code = f"""INSERT INTO {tableName}
                {columnsTable}
                VALUES {valuesList};"""
        try:
            self.cursor.execute(code)
            self.conn.commit()
        except Exception as exception:
            print(exception)

    """Search data with table name and id"""

    def findData(self, tableName: str, id: int):
        if(not self.tableExists(tableName)):
            raise ValueError("Table '" + tableName + "' not exists")
        data = self.cursor.execute(
            f"""
               SELECT * FROM {tableName} WHERE id={id};
            """
        )
        return data.fetchone()

    """Execute this function after data inserted to get last id"""

    def lastIdInserted(self, tableName: str) -> int:
        if(not self.tableExists(tableName)):
            raise ValueError("Table '" + tableName + "' not exists")

        data = self.cursor.execute(f"""
                SELECT id
                FROM {tableName}
                WHERE   ID = (SELECT MAX(ID)  FROM {tableName});
                """).fetchone()
        return int(data[0])

    """Execute function to count a registers table """

    def countTableReg(self, tableName: str):
        if(not self.tableExists(tableName)):
            raise ValueError("Table '" + tableName + "' not exists")

        data = self.cursor.execute(f"""
                SELECT COUNT(*) FROM {tableName}
                """)
        return data.fetchone()[0]

    def alterData(self, tableName: str, id: int,
                  columns: List[str], values: List[str]) -> bool:

        if(not self.tableExists(tableName)):
            raise ValueError("Table '" + tableName + "' not exists")
        strCode = ''
        for cont in range(len(columns)):
            strCode += f"{columns[cont]} = '{values[cont]}',"
        strCode = strCode[:-1]
        self.cursor.execute(f"""
                UPDATE {tableName}
                SET {strCode}
                WHERE id = {id};
                """)
        self.conn.commit()
        return True

    def deleteData(self, tableName: str, id: int):
        if(not self.tableExists(tableName)):
            raise ValueError("Table '" + tableName + "' not exists")
        self.cursor.execute(f"""
            DELETE FROM {tableName}
            WHERE id = {id};
                """)
        self.conn.commit()
        return True


# Tests
if __name__ == "__main__":
    bd = Database()

    # if(bd.deleteData("contacts", 4)):
    #    print("Deletado com Sucesso")

    # if(bd.alterData("contacts", 2, ["name", "lastName"], ["Meu", "Amor"])):
    #    print("Atualizado")

    # print(bd.lastIdInserted("contacts"))

    # bd.addIntoTable(tableName="contacts",
    #                columnNames=['name', 'lastName', 'email'],
    #                values=['Sergio', 'Felipe', 'teste'])
    # print(bd.countTableReg("contacts"))
    # print(bd.findData("contacts", 2))

    # bd.testConn()
    # bd.createTable()
    # if(bd.tableExists("testeDeTabela")):
    #    print("Tem")
    # else:
    #    print("Não tem")
