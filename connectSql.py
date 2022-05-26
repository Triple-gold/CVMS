import sqlite3


def Connection():
    conn: Connection = sqlite3.connect('DataBase/CVMS.db')
    c = conn.cursor()
    if conn:
        print("連線成功!")
        return conn
