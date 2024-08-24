# Contact Book Program

class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone_number, email):
        contact = Contact(name, phone_number, email)
        self.contacts.append(contact)
        print(f"Contact {name} added successfully!")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact {name} deleted successfully!")
                return
        print(f"Contact {name} not found!")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                print(f"Name: {contact.name}")
                print(f"Phone Number: {contact.phone_number}")
                print(f"Email: {contact.email}")
                return
        print(f"Contact {name} not found!")

    def display_contacts(self):
        if not self.contacts:
            print("No contacts in the book!")
        else:
            for contact in self.contacts:
                print(f"Name: {contact.name}")
                print(f"Phone Number: {contact.phone_number}")
                print(f"Email: {contact.email}")
                print("------------------------")

def main():
    contact_book = ContactBook()

    while True:
        print("Contact Book Menu:")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. Display Contacts")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            contact_book.add_contact(name, phone_number, email)

        elif choice == "2":
            name = input("Enter name: ")
            contact_book.delete_contact(name)

        elif choice == "3":
            name = input("Enter name: ")
            contact_book.search_contact(name)

        elif choice == "4":
            contact_book.display_contacts()

        elif choice == "5":
            print("Exiting the contact book!")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()