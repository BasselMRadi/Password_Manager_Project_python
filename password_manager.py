from cryptography.fernet import Fernet
import os

# Generate encryption key
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Load the encryption key
def load_key():
    if not os.path.exists("key.key"):
        write_key()
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    return key

key = load_key()
fr = Fernet(key)

# Add a new account and password
def add():
    name = input("Account Name: ")
    password = input("Password: ")
    encrypted_password = fr.encrypt(password.encode()).decode()

    with open("password.txt", "a") as f:
        f.write(f"{name}|{encrypted_password}\n")

# View stored accounts and passwords
def view():
    if not os.path.exists("password.txt"):
        print("No passwords stored yet.")
        return
    with open("password.txt", "r") as f:
        for line in f.readlines():
            name, encrypted_password = line.rstrip().split("|")
            decrypted_password = fr.decrypt(encrypted_password.encode()).decode()
            hidden_password = '*' * len(decrypted_password)
            print(f"User: {name}, Password: {'*' * len(decrypted_password)}")
           

# Main loop
while True:
    mode = input("Would you like to add or view passwords, press q to quit? (add, view): ")
    if mode == "q":
        break
    elif mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid mode!")
