import database


def main() -> None:
    database.add_many([
        ('Brenda', 'Smitherton', 'brenda@smitherton.com'),
        ('Joshua', 'Raintree', 'joshua@raintree.com'),
    ])
    database.show_all()


if __name__ == '__main__':
    main()
