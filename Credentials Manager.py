'''
This is a credential management application
which gives users the option to create and view a
username and password for a website. The passwords 
are encrypted.
'''

import os

# Global variable
credentials_file = "credentials.txt"


# Function to encrypt text
def encrypt_text(clear_text, shift=3):
    char_set = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\}]{[\"':;?/>.<, "
    return "".join([char_set[(char_set.find(c) + shift) % len(char_set)] for c in clear_text])


# Function to decrypt text
def decrypt_text(enc_text, shift=3):
    char_set = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\}]{[\"':;?/>.<, "
    return "".join([char_set[(char_set.find(c) - shift) % len(char_set)] for c in enc_text])


# Function to view stored credentials
def view_credentials(file_path):
    if not os.path.exists(file_path):
        print("No credentials found.")
        create_new = input("Would you like to create a new credential? (y/n): ")
        if create_new == 'y':
            create_credentials(file_path)
        return
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
        if not lines:
            print("No credentials found.")
            create_new = input("Would you like to create a new credential? (y/n): ")
            if create_new == 'y':
                create_credentials(file_path)
            return

        print("Stored Credentials:")
        for line in lines:
            site, username, enc_pwd = line.strip().split(',')
            print(f"Site: {site}, Username: {username}, Password: {decrypt_text(enc_pwd)}")
        print()


# Function to create new credentials
def create_credentials(file_path):
    site = input("\nEnter the website name: ")
    username = input("\nEnter your username: ")
    password = input("\nEnter the password: ") 
    enc_password = encrypt_text(password)
    
    with open(file_path, 'a') as file:
        file.write(f"{site},{username},{enc_password}\n")
    
    print(f"\n Your credentials have been stored. \n")

# Main program
def main():
    print("=======================")
    print("Apps2U Password Manager")
    print("======================= \n")
    
    choice = ''
    
    while choice != 'q':
        # Display menu
        print("[1] Enter 1 to create new credentials")
        print("[2] Enter 2 to view stored credentials")
        print("[3] Enter q to quit \n")
        
        # User choice
        choice = input("Make your choice: ") 
        
        # Response to user choice
        if choice == '1' :
            create_credentials(credentials_file)
        elif choice == '2':
            view_credentials(credentials_file)
        elif choice == 'q':
            print("Exiting the menu\n")
        else:
            print("\n Invalid option, please try again. \n")
    
    print("Quitting program")

if __name__ == "__main__":
    main()
