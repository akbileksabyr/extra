user_list = []

def create_user():
    print("Creating a new user:")
    name = input("Name: ")
    surname = input("Surname: ")
    age = input("Age: ")
    address = input("Address: ")
    email = input("Email: ")

    for user in user_list:
        if user['Email'] == email:
            print("User with this email already exists.")
            return

    password = input("Password (should be longer than 8 characters): ")
    while len(password) < 8:
        print("Password should be longer than 8 characters.")
        password = input("Password: ")

    user = {
        'Name': name,
        'Surname': surname,
        'Age': age,
        'Address': address,
        'Email': email,
        'Password': password
    }
    user_list.append(user)
    print("User created successfully.")

def show_users():
    print("List of users:")
    if not user_list:
        print("No users found.")
    else:
        for idx, user in enumerate(user_list, start=1):
            print(f"{idx}. Name: {user['Name']}, Surname: {user['Surname']}, Age: {user['Age']}, Address: {user['Address']}, Email: {user['Email']}")

def delete_user():
    email = input("Enter the email of the user to delete: ")
    for user in user_list:
        if user['Email'] == email:
            user_list.remove(user)
            print("User deleted.")
            return
    print("User with this email not found.")

def authorize_user():
    email = input("Enter email: ")
    password = input("Enter password: ")

    for user in user_list:
        if user['Email'] == email and user['Password'] == password:
            print(f"You are successfully logged in as {user['Name']}.")
            return

    print("Wrong email or password.")

while True:
    print("Choose one option:")
    print("1. Create User")
    print("2. Show list of Users")
    print("3. Delete user from List")
    print("4. Authorization")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        create_user()
    elif choice == '2':
        show_users()
    elif choice == '3':
        delete_user()
    elif choice == '4':
        authorize_user()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a number from 1 to 5.")
