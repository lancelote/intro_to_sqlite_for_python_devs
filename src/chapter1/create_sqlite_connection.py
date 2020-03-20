import sqlite3


def main() -> None:
    sqlite3.connect('dbs/customer.db')


if __name__ == '__main__':
    main()
