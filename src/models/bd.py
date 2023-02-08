import sqlite3


class Database():
    def __init__(self):
        return

    def createTable(self):
        self.conn = sqlite3.connect("contact-book.db")
        cursor = self.conn.cursor()
        cursor.execute(
            """
            CREATE TABLE contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            lastName TEXT NOT NULL,
            email TEXT NOT NULL,
            phoneNumber TEXT,
            address TEXT,
            birthday DATE NOT NULL
            
        );
        """
        )
        print('Tabela criada com sucesso!')
        self.conn.close()


bd = Database()
bd.createTable()
