#Yes guys
#This is an app that will allow citizens to apply for a national id and also store and send their other documents
documents = {}
users = {}

def sign_up(users):
    # This function will allow users to login to the app
    choice = input("Do you want to sign up or login? (S/L): ")
    if choice == "S":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        users[username] = password
        print("Sign up successful!")
        return username
    elif choice == "L":
        return login_user(users)
    else:
        print("Invalid choice")
        sign_up(users)

def login_user(users):
    # This function will allow users to login to the app
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users and users[username] == password:
        print("Login successful!")
        return username
    else:
        print("Invalid username or password, ")
        login_user(users)

    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users and users[username] == password:
        print("Login successful!")
        return username
    else:
        print("Invalid username or password")
        login_user(users)


def apply_for_national_id(documements):
    # This function will allow users to apply for a national id
    print("\nApply for National ID")
    name = input("Enter your full name: ")
    date_of_birth = input("Enter your date of birth (DD-MM-YYYY): ")
    address = input("Enter your current address: ")

    if name in users:
        print("You already applied for a National ID.")
    else:
        users[name] = {
            "date_of_birth": date_of_birth,
            "address": address,
            "documents": [],
            "status": "Pending"
        }
        print(f"Application submitted successfully, {name}!")
def upload_documents(documents):
    
    print(" Upload Documents for National ID ")
    
    while True:
        doc_type = input("What type of document are you uploading? (e.g. birth certificate, passport, etc.): ")
        
        content = input("Please enter the content of the document(): ")
        
        documents[doc_type] = content
        
        more = input("Is there more content to add? (Y/N): ")
        
        if more == "N":
            break
    
    print("\nDocuments uploaded successfully!")
    print(f"You uploaded {len(documents)} document(s).")
    
    # Display uploaded documents
    if documents:
        print("\nUploaded documents:")
        for doc_type, content in documents.items():
            print(f"- {doc_type}")
    
    return documents
    
def view_documents(documents):
    if documents:
        for doc_type, content in documents.items():
            print(f"- {doc_type}: {content}")

# Check Application Status
def check_application_status():
    application_id = input("Enter your application ID: ")
    status = "Pending"  # Example status
    # Status is pending, because we are not connecting it to a real database
    print(f"Application ID {application_id} is currently: {status}")

def main ():
    print("Welcome to the National ID Application System")
    sign_up(users)
    print("1. Apply for National ID")
    print("2. Upload Documents")
    print("3. View documents ")
    print("4. Check Application Status")
    print("5. Exit")

    while True:
        choice = input("Please enter your choice (1-4): ")
        if choice == '1':
            apply_for_national_id()
        elif choice == '2':
            upload_documents()
        elif choice == '3':
            check_application_status()
        elif choice == '4':
            print("Thank you for using the National ID Application System!")
            break
        else:
            print("Invalid choice. Please try again.")

main()