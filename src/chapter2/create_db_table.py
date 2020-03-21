import sqlite3


def main() -> None:
    connection = sqlite3.connect('dbs/customer.db')
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE customers (
            first_name TEXT,
            last_name TEXT,
            email_address TEXT
        )
    """)
    connection.commit()
    connection.close()


if __name__ == '__main__':
    main()
