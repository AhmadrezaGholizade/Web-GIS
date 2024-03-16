# ---------- ORACLE --------------
# INSERT INTO users (user_id, username, password) VALUES (1, 'john_doe', 'john_password');
# INSERT INTO users (user_id, username, password) VALUES (2, 'jane_smith', 'jane_password');
# INSERT INTO users (user_id, username, password) VALUES (3, 'alex_jackson', 'alex_password');
# INSERT INTO users (user_id, username, password) VALUES (4, 'sarah_williams', 'sarah_password');
# INSERT INTO users (user_id, username, password) VALUES (5, 'michael_brown', 'michael_password');

# PostgreSQL
# INSERT INTO users (username, password) VALUES ('john_dalmini', 'P@ssw0rd1');
# INSERT INTO users (username, password) VALUES ('alice_smith', 'SecurePassword123');
# INSERT INTO users (username, password) VALUES ('bob_jones', 'ComplexPwd!2024');
# INSERT INTO users (username, password) VALUES ('emma_davis', 'Str0ngPa$$w0rd');
# INSERT INTO users (username, password) VALUES ('michael_wilson', 'MyP@ssw0rd123');

import cx_Oracle
import psycopg2

def main():
    username = input("Username: ")
    password = input("Password: ")
    orcl = ORCL(username = "system", password = "Abcd44231345", dsn = "localhost:1521/FirstORCL")
    orcl_user = orcl.search_user(username,password)
    orcl.close()
    postgre = PostgreSQL(dbname = 'FirstPostgreSQL',user = 'postgres',password = '44231345',host = 'localhost',port = '5432')
    postgre_user = postgre.search_user(username,password)
    postgre.close()
    if orcl_user:
        print("User is in Oracle Database.")
    if postgre_user:
        print("User is in Postgres Database.")
    if not(orcl_user) and not(postgre_user):
        print("User is Not Found.")

class ORCL(): 
    def __init__(self, username = None, password = None, dsn = None):
        try:
            username = "system"
            password = "Abcd44231345"
            dsn = "localhost:1521/FirstORCL"
            self.connection = cx_Oracle.connect(username + "/" + password + "@" + dsn)
            self.cursor = self.connection.cursor()
        except cx_Oracle.DatabaseError as e:
                error, = e.args
                print("Oracle Database Error:", error)
    def search_user(self, user, pas):
        try:
            query = "SELECT COUNT(*) FROM users WHERE username = :username AND password = :password"
            self.cursor.execute(query, (user, pas))
            result = self.cursor.fetchone()[0]
            return result == 1
        except cx_Oracle.DatabaseError as e:
                error, = e.args
                print("Oracle Database Error:", error)
    def close(self):
        try:
            self.cursor.close()
            self.connection.close()
        except cx_Oracle.DatabaseError as e:
                error, = e.args
                print("Oracle Database Error:", error)
        
    
    

class PostgreSQL():
    def __init__(self, dbname = None,user = None,password = None,host = None,port = None):
        try:
            self.connection = psycopg2.connect(dbname = dbname,user = user,password = password,host = host,port = port)
            self.cursor = self.connection.cursor()
        except psycopg2.Error as e:
            print("Error connecting to the PostgreSQL database:", e)
    def search_user(self, user, pas):
        try:
            query = "SELECT COUNT(*) FROM users WHERE username = %s AND password = %s"
            self.cursor.execute(query, (user, pas))
            result = self.cursor.fetchone()[0]
            return result == 1
        except psycopg2.Error as e:
            print("Error connecting to the PostgreSQL database:", e)
            return False
    def close(self):
        try:
            self.cursor.close()
            self.connection.close()
        except psycopg2.Error as e:
            print("Error connecting to the PostgreSQL database:", e)




if __name__ == "__main__":
    main()
