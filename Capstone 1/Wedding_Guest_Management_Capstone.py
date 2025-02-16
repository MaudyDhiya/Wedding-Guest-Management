from tabulate import tabulate
import sys
import random

print("\t \t WELCOME TO WEDDING RACHEL & MARIO\n")

list_user = [
    {"username": "ariana", "password": "123ariana"},
    {"username": "charlie", "password": "charlie321"},
    {"username": "maudy", "password": "maudy123"}
]

list_guest = [
    {"guest_id": 1, "name": "Maudy", "email": "maudy@gmail.com", "status": "hadir", "invitation_code": "inv-123"},
    {"guest_id": 2, "name": "Dhiya", "email": "dhiya@gmail.com", "status": "tidak hadir", "invitation_code": "-"},
    {"guest_id": 3, "name": "Ulhaq", "email": "ulhaq@gmail.com", "status": "tidak hadir", "invitation_code": "-"},
    {"guest_id": 4, "name": "Cici", "email": "cici@gmail.com", "status": "hadir", "invitation_code": "inv-345"},
    {"guest_id": 5, "name": "Paramita", "email": "paramita@gmail.com", "status": "hadir", "invitation_code": "inv-321"}
]

def show_menu1():
    print('''\n          1. Show List Guest
          2. Add Guest Data
          3. Edit Guest Data
          4. Delete Guest Data
          5. Exit Program
    ''')

def list_of_guest():
    print("\n\t\t\t List of Guest on Wedding Rachel & Mario")
    print(tabulate(list_guest, headers='keys', tablefmt="fancy_grid"))

def add_guest():
    try:
        guest_id = int(input("What's your guest ID (must be a number): ").strip())
        if any(guest["guest_id"] == guest_id for guest in list_guest):
            print("Error: Guest ID already exists! Please enter a different ID.")
            return
        
        name = input("What's your name: ").strip()
        email = input("Input your email: ").strip()
        
        status = input("You able to attend this event? (hadir/tidak hadir): ").strip().lower()
        if status not in ["hadir", "tidak hadir"]:
            raise ValueError("Invalid status! Use 'hadir' or 'tidak hadir'")

        invitation_code = f"inv-{random.randint(100, 999)}" if status == "hadir" else "-"

        list_guest.append({"guest_id": guest_id, "name": name, "email": email, "status": status, "invitation_code": invitation_code})
        print("\nNew guest added successfully!")
        print(f"Invitation Code: {invitation_code}" if invitation_code else "No invitation code assigned.")
    except ValueError as e:
        print(f"Error: {e}")

def edit_guest():
    try:
        guest_id = int(input("Enter the guest ID to edit: ").strip())
        guest = next((g for g in list_guest if g["guest_id"] == guest_id), None)
        
        if guest:
            print("\nCurrent guest details:")
            print(tabulate([guest], headers="keys", tablefmt="grid"))

            new_name = input("Enter new name (press Enter to keep current): ").strip() or guest["name"]
            new_email = input("Enter new email (press Enter to keep current): ").strip() or guest["email"]
            
            new_status = input("Enter new status (hadir/tidak hadir, press Enter to keep current): ").strip().lower()
            if new_status in ["hadir", "tidak hadir", ""]:
                guest["status"] = new_status or guest["status"]
            else:
                raise ValueError("Status must be 'hadir' or 'tidak hadir'")
            
            if guest["status"] == "hadir" and not guest["invitation_code"]:
                guest["invitation_code"] = f"inv-{random.randint(100, 999)}"
            elif guest["status"] == "tidak hadir":
                guest["invitation_code"] = "-"

            guest["name"] = new_name
            guest["email"] = new_email

            print("\nGuest details updated successfully!")
            print(f"New Invitation Code: {guest['invitation_code']}" if guest["invitation_code"] else "No invitation code assigned.")
        else:
            print("Error: Guest ID not found! Please try again.")
    except ValueError as e:
        print(f"Error: {e}")

def delete_guest():
    try:
        guest_id = int(input("Enter the guest ID to delete: ").strip())
        guest = next((g for g in list_guest if g["guest_id"] == guest_id), None)
        
        if guest:
            list_guest.remove(guest)
            print(f"Guest with ID {guest_id} successfully deleted!")
        else:
            print("Error: Guest ID not found! Please try again.")
    except ValueError:
        print("Error: Guest ID must be a number! Please try again.")

def show_menu2():
    while True:
        print("\n Attendance Menu:")
        print("1. Attendance Check")
        print("2. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            attendance_check()
        elif choice == "2":
            print("Exiting attendance system. Thank you!")
            sys.exit()
        else:
            print("Invalid input! Please enter 1 or 2.")

def attendance_check():
    print("Attendance Check:")
    
    invitation_code = input("Enter your invitation code: ").strip()

    for guest in list_guest:
        if guest["invitation_code"] == invitation_code:
            print("Code is Valid! Your guest details:")
            print()
            print(f" Name: {guest['name']}")
            print(f" Email: {guest['email']}")
            print(f" Status: {guest['status']}")
            print()
            print(" \t Welcome to the Wedding! 🎊")
            return
    
    print("\n Invalid code! Please check and try again.")

def main():
    while True:
        show_menu1()
        try:
            menu = int(input("Choose the action: "))
            if menu == 1:
                list_of_guest()
            elif menu == 2:
                add_guest()
            elif menu == 3:
                edit_guest()
            elif menu == 4:
                delete_guest()
            elif menu == 5:
                print("Program finish! Thank you.")
                sys.exit()
            else:
                print("Invalid input! Please enter a number between 1-5.")
        except ValueError:
            print("Error: Please enter a valid number (1-5)!")

def login():
    print("Login First!\n")
    
    while True:
        username = input("Username: ")
        password = input("Password: ")
        print()

        user_found = next((user for user in list_user if user['username'] == username and user['password'] == password), None)

        if user_found:
            print("Login successful!\n")
            
            while True:
                print("Please choose your role:")
                print("1. Admin")
                print("2. Staff")

                role = input("Type number of your role: ").strip()
                print()

                if role == "1":
                    print("You are logged in as Admin!")
                    main()
                elif role == "2":
                    print("You are logged in as Staff")
                    show_menu2()
                else:
                    print("Invalid choice. Please enter 1 or 2.")
        else:
            print("Username or Password is Incorrect! Please try again.\n")

login()