# Contact Manager CLI (Python + SQLite)

A command-line based Contact Manager application built with Python, using SQLite for persistent storage.  
The app supports full CRUD operations with proper input validation and database-level constraints.

---

## Features

- Add new contacts (name, phone number, optional email)
- View all saved contacts
- Search contacts by:
  - Name (partial match)
  - Phone number (partial match)
  - Email
- Update existing contacts using contact ID
- Delete contacts using contact ID
- Persistent storage using SQLite (`contacts.db`)
- Database-level email uniqueness constraint
- Graceful error handling (invalid input, duplicate email, invalid ID)

---

## Tech Stack

- Python 3
- SQLite3 (built-in Python module)

---

## Database Design

**Table: `contacts`**
- `id` – Integer, Primary Key, Auto-increment
- `name` – Text, Required
- `phone` – Text, Required
- `email` – Text, Optional, Unique

---

## How to Run

1. Clone the repository
2. Navigate to the project directory
3. Run the application:

```bash
python main.py
