import sqlite3


def main() -> None:
    connection = sqlite3.connect('dbs/customer.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM customers WHERE last_name = 'Elder'")
    items = cursor.fetchall()

    for item in items:
        print(item)

    connection.commit()
    connection.close()


if __name__ == '__main__':
    main()
