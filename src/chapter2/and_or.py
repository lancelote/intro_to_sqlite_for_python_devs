import sqlite3


def main() -> None:
    connection = sqlite3.connect('dbs/customer.db')
    cursor = connection.cursor()

    cursor.execute("SELECT ROWID, * FROM customers WHERE last_name = 'Brown' AND ROWID = 3")
    connection.commit()

    cursor.execute("SELECT ROWID, * FROM customers")
    items = cursor.fetchall()
    for item in items:
        print(item)

    connection.close()


if __name__ == '__main__':
    main()
