import shelve

def open_contact_book():
    # Open the contact book database
    contact_book = shelve.open('contact_book.db')
    return contact_book

def close_contact_book(contact_book):
    # Close the contact book database
    contact_book.close()

def add_contact(contact_book):
    # Add a new contact to the contact book
    name = input("Enter the name of the contact: ")
    phone_number = input("Enter the phone number of the contact: ")
    email = input("Enter the email of the contact: ")
    address = input("Enter the address of the contact: ")

    contact = {
        'name': name,
        'phone_number': phone_number,
        'email': email,
        'address': address
    }

    contact_book[name] = contact

def view_contact_list(contact_book):
    # Display a list of all saved contacts with names and phone numbers
    print("Contact List:")
    for name, contact in contact_book.items():
        print(f"{name}: {contact['phone_number']}")

def search_contact(contact_book):
    # Implement a search function to find contacts by name or phone number
    search_query = input("Enter the name or phone number of the contact to search: ")
    found_contacts = []
    for name, contact in contact_book.items():
        if search_query in name or search_query in contact['phone_number']:
            found_contacts.append((name, contact))
    return found_contacts

def update_contact(contact_book):
    # Enable users to update contact details
    search_results = search_contact(contact_book)
    if len(search_results) == 0:
        print("No contacts found.")
        return

    for i, (name, contact) in enumerate(search_results):
        print(f"{i+1}. {name}: {contact['phone_number']}")

    choice = int(input("Enter the number of the contact to update: ")) - 1
    updated_contact = search_results[choice]

    name = updated_contact[0]
    contact = updated_contact[1]

    new_phone_number = input(f"Enter the new phone number for {name}: ")
    new_email = input(f"Enter the new email for {name}: ")
    new_address = input(f"Enter the new address for {name}: ")

    contact['phone_number'] = new_phone_number
    contact['email'] = new_email
    contact['address'] = new_address

def delete_contact(contact_book):
    # Provide an option to delete a contact
    search_results = search_contact(contact_book)
    if len(search_results) == 0:
        print("No contacts found.")
        return

    for i, (name, contact) in enumerate(search_results):
        print(f"{i+1}. {name}: {contact['phone_number']}")

    choice = int(input("Enter the number of the contact to delete: ")) - 1
    del contact_book[search_results[choice][0]]

def main():
    # Open the contact book database
    contact_book = open_contact_book()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_contact(contact_book)
        elif choice == 2:
            view_contact_list(contact_book)
        elif choice == 3:
            search_results = search_contact(contact_book)
            if len(search_results) == 0:
                print("No contacts found.")
            else:
                for name, contact in search_results:
                    print(f"{name}: {contact['phone_number']}")
        elif choice == 4:
        