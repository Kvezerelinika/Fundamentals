import json

FILE_NAME = "contacts.json"
contacts = []

def load_contacts():
    global contacts

    try:
        with open(FILE_NAME, "r") as file:
            contacts = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        contacts = []

def save_contacts():
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

def generate_id():
    if not contacts:
        return 1
    return max(contact["id"] for contact in contacts) + 1

def show_contacts():
    if not contacts:
        print("Contact book is empty!")
        return
    
    for contact in contacts:
        print(f"""
ID: {contact["id"]},              
Name: {contact["name"]},
Phone Number: {contact["phone_number"]},
Email: {contact["email"]}              
""")

def add_contact():
    name = input("Please type name: ")
    phone_number = input("Please type phone number: ")
    email = input("Please type email: ")

    contact = {
        "id": generate_id(),
        "name": name,
        "phone_number": phone_number,
        "email": email
    }

    contacts.append(contact)
    save_contacts()
    print("The contact has been saved!")

def edit_contact():
    if not contacts:
        print("Contact book is empty!")
        return
    
    show_contacts()

    contact_id = input("Please type ID to edit: ")
    if not contact_id.isdigit():
        print("Invalid ID")
        return
    
    contact_id = int(contact_id)

    for contact in contacts:
        if contact["id"] == contact_id:
            field = input("What do you want to edit: name, phone_number or email ").lower()

            if field in ("name", "phone_number", "email"):
                contact[field] = input(f"Please type new {field}: ")
                save_contacts()
                print("Contact updated!")
                return
            else:
                print("Wrong input!")
                return
            
    print("Contact not found!")

def remove_contact():
    if not contacts:
        print("There is no contact to remove!")
        return
    
    show_contacts()

    contact_id = input("Please type ID to remove: ")
    if not contact_id.isdigit():
        print("Invalid ID")
        return
    
    contact_id = int(contact_id)

    for contact in contacts:
        if contact["id"] == contact_id:
            contacts.remove(contact)
            save_contacts()
            print("Contact has been removed!")
            return
    print("Contact has not been found!")

def main():
    load_contacts()

    while True:
        print("""
1. Add contact
2. Edit contact
3. Remove contact
4. View contacts
5. Exit
""")
        choice = input("Please type your choice: ").strip()
        if not choice.isdigit():
            print("Please type a number!")
            continue

        choice = int(choice)

        if choice == 1:
            add_contact()
        elif choice == 2:
            edit_contact()
        elif choice == 3:
            remove_contact()
        elif choice == 4:
            show_contacts()
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Wrong number of input!")

main()