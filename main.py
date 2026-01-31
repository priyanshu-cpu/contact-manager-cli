print("--------- Contact Manager App ----------")

next_id = 1
contacts = []


def view_all_contact():
    if not contacts:
        print("No contacts available!")
        return

    else:
        for index, contact in enumerate(contacts, start=1):
            print(
                f"{index}. {contact['name']} {contact['phone_no']} (ID: {contact['id']}) "
            )


def add_contact():
    global next_id

    name = input("Enter contact name:\n")
    phone = input("Enter phone number:\n")

    if not name or not phone:
        print("Name and phone can not be empty!")
        return

    contact = {"id": next_id, "name": name, "phone_no": phone}
    contacts.append(contact)
    next_id += 1
    print("Contact added successfully.")


def update_contact():
    if not contacts:
        print("No contact avialable to update!")
        return

    view_all_contact()

    try:
        serial = int(input("Enter serial number to update contact:\n"))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    if serial < 1 or serial > len(contacts):
        print("Invalid serial number!")
        return

    contact = contacts[serial - 1]

    print("What do you want to update?")
    print("1. Name")
    print("2. phone number")

    user_input = input("Enter your choice:\n")
    if user_input == "1":
        new_name = input("Enter new name:\n").strip()
        if new_name:
            contact["name"] = new_name
            print("Name updated successfully!")
        else:
            print("Name can not be empty!")
    elif user_input == "2":
        new_phone = input("Enter new phone number:\n").strip()
        if new_phone:
            contact["phone_no"] = new_phone
            print("Phone number updated successfully!")
        else:
            print("Phone number can not be empty")
    else:
        print("Invalid choice!")


def delete_contact():
    if not contacts:
        print("No contacts available to delete!")
        return

    view_all_contact()

    try:
        del_input = int(input("Enter serial number to delete contact:\n"))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    if del_input < 1 or del_input > len(contacts):
        print("Invalid serial number!")
        return

    deleted = contacts.pop(del_input - 1)
    print(f"Contact '{deleted['name']}' deleted successfully.")


def search_contact():
    if not contacts:
        print("No contacts avaiable to search!")
        return

    print("1. Search by name")
    print("2. search by phone number")
    search_input = input("Enter your choice:\n")
    found = False

    if search_input == "1":
        search_name_input = input("Enter name to search:\n").strip().lower()
        for contact in contacts:
            if search_name_input in contact["name"].lower():
                print(
                    f"{contact['name']} - {contact['phone_no']} (ID: {contact['id']})"
                )
                found = True

    elif search_input == "2":
        search_phone_input = input("Enter phone number to search:\n").strip().lower()
        for contact in contacts:
            if search_phone_input in contact["phone_no"]:
                print(
                    f"{contact['name']} - {contact['phone_no']} (ID: {contact['id']})"
                )

    else:
        print("Invalid choice!")
        return

    if not found:
        print("No matching contact found.")


def main():
    while True:
        print("\n-----------------")
        print("1. Add contact")
        print("2. View all contact")
        print("3. Search contact")
        print("4. Update contact")
        print("5. Delete contact")
        print("'quit' or 'exit' to Exit.")
        user_choice = input("Enter your choice:\n")

        if user_choice in ["quit", "exit"]:
            break
        elif user_choice == "1":
            print("fill the details to add contact:\n")
            add_contact()
        elif user_choice == "2":
            view_all_contact()
        elif user_choice == "3":
            search_contact()
        elif user_choice == "4":
            update_contact()
        elif user_choice == "5":
            delete_contact()
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
