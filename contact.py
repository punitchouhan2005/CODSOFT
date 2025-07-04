#creating list for contacts 
contacts = [] 

def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email/gmail: ")
    address = input("Enter home/office address: ")
    contact = {"name": name, "phone": phone, "email": email, "address": address}
    contacts.append(contact)
    print("Contact added successfully!\n")
#want to view all contacts 
def view_contacts():
    print("\n--- Contact List ---")
    if not contacts:
        print("No contacts found.")
        return
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} | {contact['phone']} | {contact['email']} | {contact['address']}")
    print()
#want to search contacts
def search_contact():
    print("\n--- Search Contact ---")
    keyword = input("Enter name or phone to search: ").lower()
    found = False
    for contact in contacts:
        if keyword in contact["name"].lower() or keyword in contact["phone"]:
            print(f"Found: {contact['name']} | {contact['phone']} | {contact['email']} | {contact['address']}")
            found = True
    if not found:
        print("Contact not found.\n")
#want to update contacts
def update_contact():
    print("\n--- Update Contact ---")
    name = input("Enter the name of the contact to update: ").lower()
    for contact in contacts:
        if contact["name"].lower() == name:
            print("Leave blank to keep existing value.")
            contact["name"] = input("Enter new name: ") or contact["name"]
            contact["phone"] = input("Enter new phone: ") or contact["phone"]
            contact["email"] = input("Enter new email: ") or contact["email"]
            contact["address"] = input("Enter new address: ") or contact["address"]
            print("Contact updated successfully!\n")
            return
    print("Contact not found.\n")
#want to delete contacts
def delete_contact():
    print("\n--- Delete Contact ---")
    name = input("Enter the name of the contact to delete: ").lower()
    for contact in contacts:
        if contact["name"].lower() == name:
            contacts.remove(contact)
            print("Contact deleted successfully!\n")
            return
    print("Contact not found.\n")

def show_menu():
    print("====== Options Available in Contact Book ======")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    print("================================")

while True:
    show_menu()
    choice = input("Choose an option (1-6): ")
    
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("EXITING YOUR CONTACK BOOK, Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number from 1 to 6\n")
