import sqlite3


def main() -> None:
    connection = sqlite3.connect('dbs/customer.db')
    cursor = connection.cursor()

    items = cursor.execute("SELECT ROWID, * FROM customers LIMIT 2")
    for item in items:
        print(item)

    connection.commit()
    connection.close()


if __name__ == '__main__':
    main()
