import bcrypt
from pathlib import Path

USERS_FILE = Path(__file__).parent / "DATA" / "users.txt"

def hash_password(password):
    password_bytes = password.encode('utf-8')
    generate_salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, generate_salt)
    return hashed.decode('utf-8')

def register_user(username, password):
    with open(USERS_FILE, "a") as f:
        f.write(f"{username},{hash_password(password)}\n")
    print(f"User '{username}' registered successfully.")

if __name__== "__main__":
    while True:
        choice = input("Enter: (1) Register a new user or (2) Login: or (3) Exit: ")
        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            register_user(username, password)
        elif choice == "2":
            pass
            registered_password = input("Enter the password: ")
        elif choice == "3":
            print("Exiting the program.")
            break

