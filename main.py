from contact import Contact
from contact_manager import ContactManager

DB_PATH = "contacts.json"


def main() -> None:
    contact_manager = ContactManager(DB_PATH)
    while True:
        print("""\n1 - Add contact
2 - Remove contact
3 - Update contact
4 - Read contacts
5 - Clear contacts
6 - Exit
        """)

        feedback = input("Enter an option: ")

        match feedback:
            case "1":
                print("\nAdding...")
                name = input("Enter contact's name: ")
                phone_number = input("Enter contact's phone number: ")
                email = input("Enter contact's email: ")
                contact = Contact(name, phone_number, email)
                contact_manager.add_contact(contact)

            case "2":
                print("\nRemoving...")
                phone_number = input("Enter phone number as ID: ")
                contact_manager.remove_contact(phone_number)

            case "3":
                print("\nUpdating...")
                phone_number = input("Enter phone number as ID: ")

                new_name = input("Enter updated name (leave empty to keep): ")
                new_phone_number = input(
                    "Enter updated phone number (leave empty to keep): "
                )
                new_email = input("Enter updated email (leave empty to keep): ")

                updated_data = {}

                if new_name:
                    updated_data["name"] = new_name
                if new_phone_number:
                    updated_data["phone_number"] = new_phone_number
                if new_email:
                    updated_data["email"] = new_email

                contact_manager.update_contact(phone_number, updated_data)

            case "4":
                print("\nReading contacts...")
                if not contact_manager.contacts:
                    print("Nothing to display! Aborting...")
                else:
                    for contact in contact_manager.contacts:
                        print(contact)

            case "5":
                print("\nClearing contacts...")
                contact_manager.clear()

            case "6":
                print("Exiting...")
                break
            case _:
                print("\nInvalid input! Please enter a valid option...")


if __name__ == "__main__":
    main()
