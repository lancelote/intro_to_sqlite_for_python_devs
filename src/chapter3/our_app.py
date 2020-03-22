import database


def main() -> None:
    database.add_one('Laura', 'Smith', 'laura@smith.com')
    database.show_all()


if __name__ == '__main__':
    main()
