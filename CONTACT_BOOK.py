class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self):
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        self.contacts[name] = {"phone": phone, "email": email, "address": address}
        print("Contact added successfully!")

    def view_contacts(self):
        for name, details in self.contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}")

    def search_contact(self):
        search_term = input("Enter name or phone number: ")
        for name, details in self.contacts.items():
            if name == search_term or details["phone"] == search_term:
                print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
                return
        print("Contact not found!")

    def update_contact(self):
        name = input("Enter name: ")
        if name in self.contacts:
            phone = input("Enter new phone number (press enter to skip): ")
            email = input("Enter new email (press enter to skip): ")
            address = input("Enter new address (press enter to skip): ")
            if phone:
                self.contacts[name]["phone"] = phone
            if email:
                self.contacts[name]["email"] = email
            if address:
                self.contacts[name]["address"] = address
            print("Contact updated successfully!")
        else:
            print("Contact not found!")

    def delete_contact(self):
        name = input("Enter name: ")
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

def main():
    contact_book = ContactBook()
    while True:
        print("\n1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            contact_book.add_contact()
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            contact_book.search_contact()
        elif choice == "4":
            contact_book.update_contact()
        elif choice == "5":
            contact_book.delete_contact()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
