import sqlite3


def main() -> None:
    connection = sqlite3.connect('dbs/customer.db')
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE customers SET first_name = 'John'
        WHERE ROWID = 1
    """)
    connection.commit()

    cursor.execute("SELECT * FROM customers")
    items = cursor.fetchall()
    for item in items:
        print(item)

    connection.close()


if __name__ == '__main__':
    main()
