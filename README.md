# Contact Manager (Python CLI)

A lightweight command-line contact manager written in Python. Contacts are stored in a JSON file and can be added, updated, removed, and viewed from a simple CLI menu.

## About

This project was built as a learning exercise to practice:

- Python object-oriented programming
- File handling
- JSON data storage
- Basic CLI application design

It is intended for educational purposes and is not meant for production use.

## Features

- Add new contacts
- Prevent duplicate phone numbers
- Update existing contacts
- Remove contacts
- View all saved contacts
- Persistent storage using JSON
- Simple command-line interface

## Contact Format

Each contact contains:

- **Name**
- **Phone number**
- **Email**

Example stored contact:

```json
{
  "name": "John Doe",
  "phone_number": "123456789",
  "email": "john@example.com"
}
```

## Running the Program

1. Clone the repository:

```bash
git clone https://github.com/std-enigma/contact-manager.git
```

2. Navigate into the project folder:

```bash
cd contact-manager
```

3. Run the program:

```bash
python main.py
```

## Example Menu

```
1. Add contact
2. Remove contact
3. Update contact
4. Show contacts
5. Exit
```

## Future Improvements

Some ideas for extending the project:

- Search contacts
- Sort contacts
- Export contacts
- Add validation for emails and phone numbers
- Build a GUI version
