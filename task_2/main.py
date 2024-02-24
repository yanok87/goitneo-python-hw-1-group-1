"""This module contains a CLI"""


def parse_input(user_input):
    """This function parses user input"""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    """This function adds a contact to phone book"""
    name, phone = args
    contacts[name] = phone
    print(contacts)
    return "Contact added."


def contact(args, contacts):
    """This function returns contact's phone number"""
    name = args[0]
    return contacts[name]


def all_contacts(contacts):
    """This function returns phone book"""
    phone_book = []
    for name, number in contacts.items():
        phone_book.append(f"{name} {number}")
    return phone_book


def main():
    """This function interacts with user and creates a phone book"""
    contacts = {}

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "good bye"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(contacts)
            print(add_contact(args, contacts))
        elif command == "change":
            add_contact(args, contacts)
        elif command == "phone":
            print(contact(args, contacts))
        elif command == "all":
            print(contacts, "contacts")
            all = all_contacts(contacts)
            for i in all:
                print(i)
        else:
            print("Invalid command.")


if __name__ == "__main__":

    main()
