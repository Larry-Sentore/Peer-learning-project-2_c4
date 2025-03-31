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
    pass

def upload_documents():
    documents = {}
    
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


def check_application_status():
    pass
    
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