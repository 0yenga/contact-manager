import json
import os

FILE_NAME = "contacts.json"


# Load contacts from JSON file
def load_contacts():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        return json.load(f)


# Save contacts to JSON file
def save_contacts(contacts):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=4, ensure_ascii=False)


# Add a new contact
def add_contact(contacts):
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully.\n")


# Display all contacts
def display_contacts(contacts):
    if not contacts:
        print("No contacts found.\n")
        return

    print("\nContact list:")
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['name']} | {c['phone']} | {c['email']}")
    print()


# Search for a contact
def search_contact(contacts):
    name = input("Enter name to search: ").lower()
    results = [c for c in contacts if name in c["name"].lower()]

    if results:
        print("\nResults:")
        for c in results:
            print(f"{c['name']} | {c['phone']} | {c['email']}")
    else:
        print("No contact found.")
    print()


# Delete a contact
def delete_contact(contacts):
    display_contacts(contacts)
    try:
        index = int(input("Enter contact number to delete: ")) - 1
        if 0 <= index < len(contacts):
            deleted = contacts.pop(index)
            save_contacts(contacts)
            print(f"{deleted['name']} deleted.\n")
        else:
            print("Invalid index.\n")
    except ValueError:
        print("Invalid input.\n")


# Main menu
def menu():
    contacts = load_contacts()

    while True:
        print("===== Contact Manager =====")
        print("1. Add a contact")
        print("2. Display contacts")
        print("3. Search a contact")
        print("4. Delete a contact")
        print("5. Exit")

        choice = input("Choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            display_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    menu()