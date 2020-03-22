import sqlite3


def main() -> None:
    connection = sqlite3.connect('dbs/customer.db')
    cursor = connection.cursor()

    cursor.execute("DROP TABLE customers")
    connection.commit()

    connection.close()


if __name__ == '__main__':
    main()
