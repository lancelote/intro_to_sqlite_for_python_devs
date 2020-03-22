import database


def main() -> None:
    database.delete_one(4)
    database.show_all()


if __name__ == '__main__':
    main()
