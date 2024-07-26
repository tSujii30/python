class Contact:
    def __init__(self, name, phone, email):
        # Initialize a new contact with name, phone, and email attributes
        self.name = name
        self.phone = phone
        self.email = email

class ContactManager:
    def __init__(self):
        # Initialize the contact manager with an empty list of contacts
        self.contacts = []

    def add_contact(self, contact):
        # Add a contact to the contact list
        self.contacts.append(contact)
        print("Contact added.")

    def edit_contact(self, index, name, phone, email):
        # Edit the contact at the specified index with new details
        if 0 <= index < len(self.contacts):
            self.contacts[index].name = name
            self.contacts[index].phone = phone
            self.contacts[index].email = email
            print("Contact edited.")
        else:
            print("Contact not found.")

    def delete_contact(self, index):
        # Delete the contact at the specified index
        if 0 <= index < len(self.contacts):
            del self.contacts[index]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    def search_contact(self, name):
        # Search for contacts that match the given name (case-insensitive)
        found_contacts = [contact for contact in self.contacts if name.lower() in contact.name.lower()]
        if found_contacts:
            for contact in found_contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")
        else:
            print("No contacts found.")

    def display_contacts(self):
        # Display all contacts in the contact list
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")

def main():
    # Create an instance of ContactManager
    contact_manager = ContactManager()

    while True:
        # Display menu options for the user
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. Edit Contact")
        print("3. Delete Contact")
        print("4. Search Contact")
        print("5. Display Contacts")
        print("6. Exit")

        # Get user's choice
        choice = input("Enter your choice: ")

        if choice == '1':
            # Add a new contact
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            contact = Contact(name, phone, email)
            contact_manager.add_contact(contact)
        elif choice == '2':
            # Edit an existing contact
            index = int(input("Enter contact index to edit: "))
            name = input("Enter new name: ")
            phone = input("Enter new phone: ")
            email = input("Enter new email: ")
            contact_manager.edit_contact(index, name, phone, email)
        elif choice == '3':
            # Delete a contact
            index = int(input("Enter contact index to delete: "))
            contact_manager.delete_contact(index)
        elif choice == '4':
            # Search for contacts by name
            name = input("Enter name to search: ")
            contact_manager.search_contact(name)
        elif choice == '5':
            # Display all contacts
            contact_manager.display_contacts()
        elif choice == '6':
            # Exit the program
            print("Exiting...")
            break
        else:
            # Handle invalid choices
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Run the main function if this script is executed
    main()
