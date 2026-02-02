import sqlite3


def init_db():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS contacts(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   phone TEXT NOT NULL UNIQUE,
                   email TEXT UNIQUE
                   )
"""
    )
    conn.commit()
    conn.close()


print("--------- Contact Manager App ----------")

next_id = 1
contacts = []


def view_all_contact():
    try:
        conn = sqlite3.connect("contacts.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id,name,phone,email FROM contacts")
        rows = cursor.fetchall()

        if not rows:
            print("No contacts available!")
            return

        for row in rows:
            contact_id, name, phone, email = row
            email_display = email if email else "N/A"
            print(f"ID: {contact_id} | {name} | {phone} | {email_display}")

    except sqlite3.Error as e:
        print("Failed to fetch contacts.")
        print("Error:", e)

    finally:
        conn.close()


def add_contact():
    name = input("Enter contact name:\n").strip()
    phone = input("Enter phone number:\n").strip()
    email = input("Enter email (optional):\n").strip()

    if not name or not phone:
        print("Name and phone can not be empty!")
        return

    try:
        conn = sqlite3.connect("contacts.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO contacts (name,phone,email) VALUES (?,?,?)",
            (name, phone, email if email else None),
        )
        conn.commit()
        conn.close()
    except sqlite3.IntegrityError:
        print("This email already exists!")

    finally:
        conn.close()


def update_contact():
    contact_id = input("Enter contact ID to update:\n").strip()

    if not contact_id.isdigit():
        print("Invalid ID!")
        return
    print("What do you want to update?")
    print("1. Name")
    print("2. Phone")
    print("3. Email")

    choice = input("Enter your choice:\n").strip()

    field_map = {"1": "name", "2": "phone", "3": "email"}

    if choice not in field_map:
        print("Invalid choice!")
        return
    new_value = input("Enter new value:\n").strip()

    if choice in {"1", "2"} and not new_value:
        print("This field cannot be empty!")
        return

    if choice == "3" and not new_value:
        new_value = None

    field = field_map[choice]

    try:
        conn = sqlite3.connect("contacts.db")
        cursor = conn.cursor()

        cursor.execute(
            f"UPDATE contacts SET {field} = ? WHERE id = ?", (new_value, contact_id)
        )

        conn.commit()

        if cursor.rowcount == 0:
            print("No contact found with this ID.")
        else:
            print("Contact updated successfully.")
    except sqlite3.IntegrityError:
        print("This email already exists.")

    except sqlite3.Error as e:
        print("Error", e)

    finally:
        conn.close()



def delete_contact():
    contact_id = input("Enter contact ID to delete:\n").strip()

    if not contact_id.isdigit():
        print("Invalid ID!")
        return

    try:
        conn = sqlite3.connect("contacts.db")
        cursor = conn.cursor()

        cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))

        conn.commit()

        if cursor.rowcount == 0:
            print("No contact found with this ID.")
        else:
            print("Contact deleted successfully.")

    except sqlite3.Error as e:
        print("Deletion failed.")
        print("Error:", e)

    finally:
        conn.close()


def search_contact():
    print("1. Search by name")
    print("2. search by phone number")
    print("3. search by email ")
    choice = input("Enter your choice:\n")
    if choice not in {"1", "2", "3"}:
        print("Invalid choice!")
        return

    keyword = input("Enter search value:\n").strip()
    if not keyword:
        print("Search value can not be empty!")
        return

    column_map = {"1": "name", "2": "phone", "3": "email"}

    column = column_map[choice]

    try:
        conn = sqlite3.connect("contacts.db")
        cursor = conn.cursor()

        cursor.execute(
            f"SELECT id,name,phone,email FROM contacts WHERE {column} LIKE ?",
            (f"%{keyword}%",),
        )

        rows = cursor.fetchall()

        if not rows:
            print("No matching contact found.")
            return

        for contact_id, name, phone, email in rows:
            email_display = email if email else "N/A"
            print(f"ID: {contact_id} | {name} | {phone} | {email_display}")
    except sqlite3.Error as e:
        print("Error", e)

    finally:
        conn.close()


def main():
    init_db()
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
