import json

# File to store contacts
CONTACTS_FILE = 'contacts.json'

def load_contacts():
    try:
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    save_contacts(contacts)
    print(f"Contact for {name} added successfully.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        for name, details in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            print("="*20)

def search_contact(contacts):
    search_term = input("Enter name or phone number to search: ")
    found_contacts = {name: details for name, details in contacts.items() if search_term in name or search_term in details['phone']}
    if not found_contacts:
        print("No contacts found.")
    else:
        for name, details in found_contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            print("="*20)

def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print(f"Updating contact for {name}:")
        phone = input(f"Enter new phone number (current: {contacts[name]['phone']}): ") or contacts[name]['phone']
        email = input(f"Enter new email (current: {contacts[name]['email']}): ") or contacts[name]['email']
        address = input(f"Enter new address (current: {contacts[name]['address']}): ") or contacts[name]['address']
        
        contacts[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }
        save_contacts(contacts)
        print(f"Contact for {name} updated successfully.")
    else:
        print(f"No contact found for {name}.")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact for {name} deleted successfully.")
    else:
        print(f"No contact found for {name}.")

def main():
    contacts = load_contacts()
    
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting the Contact Management System.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()


