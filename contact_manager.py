import json
from pathlib import Path

from contact import Contact


class ContactManager:
    def __init__(self, db_path: str) -> None:
        self._fp = Path(db_path)
        self.contacts: list[Contact] = self.load_data()

    def add_contact(self, contact: Contact) -> None:
        target_index = self.get_contact_index(contact.phone_number)
        if target_index != -1:
            print("Contact Already exist! Aborting...")
            return
        self.contacts.append(contact)
        self.save_data()

    def remove_contact(self, phone_number: str) -> None:
        target_index = self.get_contact_index(phone_number)
        if target_index == -1:
            print("Contact not found! Aborting...")
            return
        self.contacts.pop(target_index)
        self.save_data()

    def get_contact_index(self, phone_number: str) -> int:
        for i, c in enumerate(self.contacts):
            if c.phone_number == phone_number:
                return i
        return -1

    def update_contact(self, phone_number: str, new_data: dict[str, str]) -> None:
        target_index = self.get_contact_index(phone_number)
        if target_index == -1:
            print("Contact not found! Aborting...")
            return

        old_data = self.contacts[target_index].to_dict()
        updated_data = {**old_data, **new_data}  # Thanks chatgpt ;)
        if (
            updated_data["phone_number"] != phone_number
            and self.get_contact_index(updated_data["phone_number"]) != -1
        ):
            print("Phone number already exists! Aborting...")
            return
        self.contacts[target_index] = Contact.from_dict(updated_data)

        self.save_data()

    def clear(self) -> None:
        self.contacts.clear()
        self.save_data()

    def save_data(self) -> None:
        with open(self._fp, mode="w") as file:
            data = [contact.to_dict() for contact in self.contacts]
            json.dump(data, file)

    def load_data(self) -> list[Contact]:
        if not self._fp.exists():
            return []

        with open(self._fp) as file:
            try:
                json_data = json.load(file)
                return [Contact.from_dict(obj) for obj in json_data]
            except Exception:
                return []
