import sqlite3


def main() -> None:
    connection = sqlite3.connect('dbs/customer.db')
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO customers VALUES ('John', 'Elder', 'john@codemy.com')
    """)
    connection.commit()
    connection.close()


if __name__ == '__main__':
    main()
