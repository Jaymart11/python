def add_contact(contacts, contact):
    """Add a new contact to the list"""

    has_empty = any(not val.strip() for val in contact.values())
    if has_empty:
        print("Error: Contact description cannot be empty!")
        return
    
    contacts.append(contact)
    print(f"Added contact: '{contact['name']} - {contact['phone']}'")

def view_contacts(contacts):
    """Display all contacts with their status"""
    if not contacts:
        print("No contacts  in the list!")
        return
    
    print(contacts)
    print("\nAll Contacts:")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']} - {contact['email']}")

def search_contacts(contacts, keyword):
    """Search all contacts with their status"""
    index = next(
    (i for i, d in enumerate(contacts) 
     if 'name' in d and keyword in d['name']),
    None)

    print(f"{index + 1}. {contacts[index]['name']} - {contacts[index]['phone']} - {contacts[index]['email']}")

def update_contact(contacts):
    """Mark a contact as completed"""
    view_contacts(contacts)
    if not contacts:
        return
    
    try:
        contact_num = int(input("\nEnter the number to update: "))
        name = input(f"Update contact name [Current - {contacts[contact_num - 1]["name"]}: ") or contacts[contact_num - 1]["name"]
        phone = input(f"Update contact phone [Current - {contacts[contact_num - 1]["phone"]}: ") or contacts[contact_num - 1]["phone"]
        email = input(f"Update contact email [Current - {contacts[contact_num - 1]["email"]}: ") or contacts[contact_num - 1]["email"]

        if 1 <= contact_num <= len(contacts):
            contacts[contact_num-1] = {"name": name, "phone": phone, "email":email}
            print(f"Updated to {contacts[contact_num - 1]['name']} - {contacts[contact_num - 1]['phone']} - {contacts[contact_num - 1]['email']}")
        else:
            print("Invalid contact number!")
    except ValueError:
        print("Please enter a valid number!")

def remove_contact(contacts):
    """Remove a contact from the list"""
    view_contacts(contacts)
    if not contacts:
        return
    
    try:
        contact_num = int(input("\nEnter contact number to remove: "))
        if 1 <= contact_num <= len(contacts):
            removed = contacts.pop(contact_num-1)
            print(f"Removed contact: {removed['name']} - {removed['phone']} - {removed['email']}")
        else:
            print("Invalid contact number!")
    except ValueError:
        print("Please enter a valid number!")

def save_contact(contacts):
    try:
        save = open("contact_list.txt", "a")
        [save.write(f"{contact['name']} - {contact['phone']} - {contact['email']}  \n") for contact in contacts]
        save.close()
    except ValueError:
        print("Error", ValueError)
        exit()

def load_contact(contacts):
    try:
        load = open("contact_list.txt")
        contact_list = load.read()
        lines = contact_list.strip().split('\n')

        for line in lines:
            parts = [part.strip() for part in line.split(' - ')]
            print(parts)
            row_dict = dict(name = parts[0], phone = parts[1], email = parts[2])
            contacts.append(row_dict)
        
        load.close()
    except ValueError:
        print("Error", ValueError)
        exit()

def main():
    contacts = []
    
    while True:
        print("\nContact Book Manager:")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contacts")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Save Contact")
        print("7. Load Contact")
        print("8. Exit")
        
        try:
            choice = int(input("Enter your choice (1-8): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1-8.")
            continue
        
        match choice:
            case 1:
                name = input("Enter contact name: ")
                phone = input("Enter contact phone: ")
                email = input("Enter contact email: ")
                add_contact(contacts, {"name": name, "phone": phone, "email":email})
            case 2:
                view_contacts(contacts)
            case 3:
                keyword = input("Search contact name: ")
                search_contacts(contacts, keyword)
            case 4:
                update_contact(contacts)
            case 5:
                remove_contact(contacts)
            case 6:
                save_contact(contacts)
            case 7:
                load_contact(contacts)
            case 8:
                print("Goodbye!")
                break
            case _:
                print("Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()