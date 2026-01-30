print("--------- Contact Manager App ----------")

next_id = 1
contacts = []

def view_all_contact():
    if not contacts:
        print("No contacts available!")
    else:
        for index,contact in enumerate(contacts,start=1):
            print(f"{index}. {contact['name']} {contact['phone_no']} ")

def add_contact():
    global next_id
    try:
        name_input = input("Enter contact name:\n")
        phone_input = input("Enter phone number:\n")
    except (ValueError, IndexError):
        print("Invalid input!")
    contact = {"id" : next_id,"name" : name_input,"phone_no" : phone_input}
    next_id+=1
    contacts.append(contact)

def update_contact():
    view_all_contact()
    try:
        update_input = int(input("Enter serieal number to update contact:\n"))
    except (ValueError,IndexError):
        print("Invalid value!")

    print("What do you want to update?")
    print("1. Name")
    print("2. phone_no.")
    
    user_input = int(input("Enter your choice:\n"))
    if user_input == 1:
        contacts[update_input-1]['name'] = input("Enter new name:\n")
    elif user_input == 2:
        contacts[update_input-1]['phone_no'] = input("Enter new phone number:\n")
    else:
        print("Wrong input!")
def delete_contact():
    global next_id
    view_all_contact()
    try:
        del_input = int(input("Enter serial number to delete contact:\n"))
    except (ValueError,IndexError):
        print("wrong input")
    if del_input:
        contacts.pop(del_input-1)
    
def search_contact():
    print("1. Search by name")
    print("2. search by phone number")
    search_input = int(input("Enter your choice:\n"))

    if search_input == 1:
        search_name_input = input("Enter name to search:\n")
        for contact in contacts:
            if search_name_input in contact["name"]:
                print("Contact available")
            else:
                print("No contacts with this name!")
    elif search_input ==2:
        search_phone_input = input("Enter phone number to search:\n")
        for contact in contacts:
            if search_phone_input in contact["phone_no"]:
                print("Contact avalaible")
                print(f"{contact['name'] : {contact['phone_no']}}")
            else:
                print("No contact with this phone")

def main():
    while True:
        print("-----------------")
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
