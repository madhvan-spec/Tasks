# Create a contact book using dictionaries (add, search, update, delete contacts)

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print(f"Contact '{name}' added.\n")


def search_contact(contacts):
    query = input("Enter name to search: ").lower()
    results = {name: phone for name, phone in contacts.items() if query in name.lower()}

    if results:
        print("\n--- Search Results ---")
        for name, phone in results.items():
            print(f"{name}: {phone}")
        print()
    else:
        print("No matching contacts found.\n")


def update_contact(contacts):
    name = input("Enter name to update: ")
    if name in contacts:
        phone = input("Enter new phone number: ")
        contacts[name] = phone
        print(f"Contact '{name}' updated.\n")
    else:
        print("Contact not found.\n")


def delete_contact(contacts):
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.\n")
    else:
        print("Contact not found.\n")


def display_contacts(contacts):
    if contacts:
        print("\n--- Contact List ---")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
        print()
    else:
        print("\nContact book is empty.\n")


def start_menu():
    contacts = {}

    while True:
        print("=== Contact Book ===")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Display All Contacts")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            search_contact(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            display_contacts(contacts)
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")



start_menu()