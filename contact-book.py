#Main Menu
def display_menu():
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Exit")
def add_contact(contact_book):
    name = input("enteer your nmae")
    phone = input("enter phone")
    email = input("enetre emeil")
    address = input("enter address")
    if name in contact_book:
        print("Contact already exists!")
    else:
        contact_book[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        print("Contact added successfully!")
def view_contact(contact_book):
    contact_name = input()
    if contact_name not in contact_book:
        print("Contact not found!")
    else:
        print(f"Name: {contact_name}")
        for key, value in contact_book[contact_name].items():
            print(f"{key.capitalize()}: {value}")
def edit_contact(contact_book):
    name_to_edit = input()
    if name_to_edit in contact_book:
        new_phone = input()
        if new_phone != "":
            contact_book[name_to_edit]["phone"] = new_phone
        new_email = input()
        if new_email != '':
            contact_book[name_to_edit]["email"] = new_email
        new_address = input()
        if new_address != "":
            contact_book[name_to_edit]['address'] = new_address

        print('Contact updated successfully!')
    else:
        print("Contact not found!")

def delete_contact(contact_book):
    delete_contact_name = input()
    if delete_contact_name in contact_book:
        del contact_book[delete_contact_name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

def list_all_contacts(contact_book):
    if not contact_book:
        print('No contacts available.')
    else:
        for name, details in contact_book.items():
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            print()

contact_book = {}

while True:
    display_menu()
    user_input = input()
    if user_input == "1":
        add_contact(contact_book)
    elif user_input == "2":
        view_contact(contact_book)
    elif user_input == "3":
        edit_contact(contact_book)
    elif user_input == "4":
        delete_contact(contact_book)
    elif user_input == "5":
        list_all_contacts(contact_book)
    elif user_input == "6":
        break
    else:
        print("invalid syntaxx")
        
   
   











