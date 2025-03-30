#Yes guys
#This is an app that will allow citizens to apply for a national id and also store and send their other documents
def __init__(self):
    # Initializing a default app and password 
    self.users = {"admin": "admin123"}
    self.documents = {}

def login(self):
    # This function will allow users to login to the app
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in self.users and self.users[username] == password:
        print("Login successful!")
        return username
    else:
        print("Invalid username or password")
        self.login()


def apply_for_national_id():

def upload_documents():
    print("Upload Documents for National ID Application")
    print("Please upload the following documents:")

    documents = {
        "1": "Birth Certificate",
        "2": "ID Proof (Passport/License)",
        "3": "Address Proof",
        "4": "Passport-sized Photo"
    }
    for key, doc in documents.items():
        print(f"{key}. {doc}")
    
    # Get user input
    choice = input("\nSelect document to upload (1-4): ")
    
    # Check if valid choice
    if choice in documents:
        doc_name = documents[choice]
        filename = input(f"Enter filename for {doc_name}: ")
        
        if filename:
            print(f"{doc_name} uploaded successfully!")
        else:
            print("Upload cancelled.")
    else:
        print("Invalid choice.")

def check_application_status():

def view_documents():


def main ():
    print("Welcome to the National ID Application System")
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