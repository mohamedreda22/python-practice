contacts = {
    "mohamed reda": "01155921429",
    "amal mohamed": "01155920025",
    "reda ismail": "01148195875"
}

print("Please Enter 'ADD' to add a new contact")
print("Please Enter 'SHOW' to show all the contacts")
print("Please Enter 'DELETE' to delete an existing contact")
print("Please Enter 'EXIT' to quit the program")

while True:
    command = input("\nEnter your command: ").upper()

    if command == "SHOW":
        if contacts:
            print("\nContacts list:")
            for name, number in contacts.items():
                print(f"{name}: {number}")
        else:
            print("\nNo contacts available.")

    elif command == "ADD":
        key = input("Enter the name of the contact you want to add: ")
        value = input("Enter the phone number of the contact you want to add: ")
        if key in contacts:
            print(f"\nContact '{key}' already exists!")
        else:
            contacts[key] = value
            print(f"\nContact '{key}' added successfully.")

    elif command == "DELETE":
        contact = input("Enter the name of the contact you want to delete: ")
        if contact in contacts:
            del contacts[contact]
            print(f"\nContact '{contact}' deleted successfully.")
        else:
            print(f"\nContact '{contact}' not found!")

    elif command == "EXIT":
        print("\nExiting the program. Goodbye!")
        break

    else:
        print("\nYou entered an invalid command! Please try again.")
