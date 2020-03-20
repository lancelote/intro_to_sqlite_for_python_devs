import sqlite3


def main() -> None:
    connection = sqlite3.connect('dbs/customer.db')
    cursor = connection.cursor()

    many_customers = [
        ('Wes', 'Brown', 'wes@brown.com'),
        ('Steph', 'Kuewa', 'steph@kuewa.com'),
        ('Dan', 'Pas', 'dan@pas.com'),
    ]

    cursor.executemany('INSERT INTO customers VALUES (?,?,?)', many_customers)

    connection.commit()
    connection.close()


if __name__ == '__main__':
    main()
