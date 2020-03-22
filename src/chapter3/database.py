import sqlite3


def show_all() -> None:
    connection = sqlite3.connect('dbs/customer.db')
    cursor = connection.cursor()

    cursor.execute("SELECT ROWID, * FROM customers")
    items = cursor.fetchall()

    for item in items:
        print(item)

    connection.commit()
    connection.close()


def add_one(first: str, last: str, email: str) -> None:
    connection = sqlite3.connect('dbs/customer.db')
    cursor = connection.cursor()

    cursor.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))

    connection.commit()
    connection.close()
