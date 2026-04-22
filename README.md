# Contact Manager

A command-line contact management application written in Python.

## Features

- Add a contact
- Display all contacts
- Search a contact by name
- Delete a contact
- Automatic saving using a JSON file

## Requirements

- Python 3.x
- No external libraries required

## Installation

1. Clone the repository:
```bash
git clone https://github.com/0yenga/contact-manager.git
cd contact-manager
```

2. Run the program:
```bash
python main.py
```
===== Contact Manager =====

Add a contact
Display contacts
Search a contact
Delete a contact
Exit  

Contacts are saved automatically to `contacts.json` after each operation.

## Project Structure

contact_manager/
│── main.py          # Main program
│── contacts.json    # Local data storage
│── README.md

## Data Format

Each contact is stored in JSON format:

```json
{
    "name": "John Doe",
    "phone": "123456789",
    "email": "john@example.com"
}
```

## Concepts Used

- File I/O with JSON
- Lists and dictionaries
- Function-based structure
- Error handling

## Author

ADJAMBO Espoir Oyénga — Computer Engineering Student
Nizhny Novgorod State Technical University, Russia
[GitHub Profile](https://github.com/0yenga)
