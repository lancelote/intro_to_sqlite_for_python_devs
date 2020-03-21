import sqlite3


def main() -> None:
    connection = sqlite3.connect('dbs/customer.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM customers')
    items = cursor.fetchall()

    for item in items:
        print(f'{item[0]} {item[1]} ({item[2]})')

    connection.commit()
    connection.close()


if __name__ == '__main__':
    main()
