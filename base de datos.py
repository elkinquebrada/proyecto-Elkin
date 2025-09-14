import sqlite3
import psycopg2 # type: ignore

# Clase
class DatabaseConnection:
    def __init__(self, db_name):
        #Atrubutos
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect(self):
        #Manejo de errores
        raise NotImplementedError("Subclasses must implement connect()")

    def execute_query(self, query, params=()):
        if not self.conn:
            raise Exception("Database not connected.")
        self.cursor.execute(query, params)
        self.conn.commit()
        return self.cursor

    def fetch_all(self, query, params=()):
        result = self.execute_query(query, params)
        return result.fetchall()

    def close(self):
        if self.conn:
            self.conn.close()
            print("Database connection closed.")

# Herencia de la clase DatabaseConnection para usarla como base para crear SQLiteConnection
class SQLiteConnection(DatabaseConnection):
    def __init__(self, db_name=":memory:"):
        super().__init__(db_name)

    def connect(self):  # Polimorfismo
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        print(f"Connected to SQLite database: {self.db_name}")

# Herencia de la clase DatabaseConnection para usarla como base para crear PostgresConnection
class PostgresConnection(DatabaseConnection):
    def __init__(self, db_name, user, password, host="localhost", port=5432):
        #Se usa super para hacer el llamado del constructor DatabaseConnection
        super().__init__(db_name)
        #Se agregan valores necesarios para el uso correcto de una base de datos como postgresql
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def connect(self):  # Polimorfismo
        self.conn = psycopg2.connect(
            dbname = self.db_name,
            user = self.user,
            password = self.password,
            host = self.host,
            port = self.port
        )
        self.cursor = self.conn.cursor()
        print(f"Connected to PostgreSQL database: {self.db_name}")