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
    orcl = orcl_register(username,password)
    postgre = postgres_register(username, password)
    if orcl:
        print("User is in Oracle Database.")
    if postgre:
        print("User is in Postgres Database.")
    if not(orcl) and not(postgre):
        print("User is Not Found.")

def orcl_register(user, pas):  
    try:
        username = "system"
        password = "Abcd44231345"
        dsn = "localhost:1521/FirstORCL"
        connection = cx_Oracle.connect(username + "/" + password + "@" + dsn)
        cursor = connection.cursor()
        query = "SELECT COUNT(*) FROM users WHERE username = :username AND password = :password"
        cursor.execute(query, (user, pas))
        result = cursor.fetchone()[0]
        cursor.close()
        connection.close()
        return result == 1
    except cx_Oracle.DatabaseError as e:
            error, = e.args
            print("Oracle Database Error:", error)
    
    

def postgres_register(user, pas):
    try:
        conn_params = {
            'dbname': 'FirstPostgreSQL',
            'user': 'postgres',
            'password': '44231345',
            'host': 'localhost',
            'port': '5432',  # Default PostgreSQL port
        }
        connection = psycopg2.connect(**conn_params)
        cursor = connection.cursor()
        query = "SELECT COUNT(*) FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (user, pas))
        result = cursor.fetchone()[0]
        cursor.close()
        connection.close()
        return result == 1
    except psycopg2.Error as e:
        print("Error connecting to the PostgreSQL database:", e)
        return False




if __name__ == "__main__":
    main()
