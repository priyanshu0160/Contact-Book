class Contact:1
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name} - {self.phone} - {self.email}"


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        for contact in self.contacts:
            print(contact)

    def search_contact(self, name):
        found_contacts = [contact for contact in self.contacts if name.lower() in contact.name.lower()]
        if not found_contacts:
            print("No contacts found.")
        else:
            for contact in found_contacts:
                print(contact)

    def delete_contact(self, name):
        original_count = len(self.contacts)
        self.contacts = [contact for contact in self.contacts if name.lower() not in contact.name.lower()]
        if len(self.contacts) < original_count:
            print(f"Deleted contacts matching: {name}")
        else:
            print("No contacts found to delete.")


def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            contact = Contact(name, phone, email)
            contact_book.add_contact(contact)
            print("Contact added.")

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            name = input("Enter name to search: ")
            contact_book.search_contact(name)

        elif choice == '4':
            name = input("Enter name to delete: ")
            contact_book.delete_contact(name)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
