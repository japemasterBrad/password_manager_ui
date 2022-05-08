from sqlite3 import *

# INIT DB
conn = connect("passwords.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS passwords ("
            "service VARCHAR(25) NOT NULL,"
            "username VARCHAR(50) NOT NULL,"
            "password VARCHAR(50) NOT NULL"
            ")")
conn.commit()
conn.close()


def add_new_entry(service, username, password):
    conn = connect("passwords.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO passwords (service, username, password)"
                "VALUES ((?), (?), (?))", [service, username, password]
                )
    conn.commit()
    conn.close()


def remove_entry():
    conn = connect("passwords.db")
    cur = conn.cursor()
    cur.execute(
                "DROP FROM passwords,"
                ""
                )
    conn.commit()
    conn.close()


def copy_to_clipboard():
    pass
