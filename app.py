# This is a simple National ID Application System that allows users to sign up, login, apply for a national ID, upload documents, view documents, and check application status.
class NationalIDSystem:
    def __init__(self):
        self.users = {}
        self.documents = {}
        self.applications = {}
#This is to sign up and register a user
    def sign_up(self):
        choice = input("Do you want to sign up or login? (S/L): ")
        if choice == "S":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            self.users[username] = password
            print("Sign up successful!")
            return username
        elif choice == "L":
            return self.login_user()
        else:
            print("Invalid choice")
            return self.sign_up()
#Function to log in a user
    def login_user(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        #Checks if user is in the database
        if username in self.users and self.users[username] == password:
            print("Login successful!")
            return username
        else:
            print("Invalid username or password.")
            return self.login_user()
#Function to collect input for the ID application
    def apply_for_national_id(self, username):
        print("Apply for National ID")
        name = input("Enter your full name: ")
        date_of_birth = input("Enter your date of birth (DD-MM-YYYY): ")
        address = input("Enter your current address: ")
#Checks if user had already applies
        if username in self.applications:
            print("You already applied for a National ID.")
        else:
#Stores application in a dictionary
            self.applications[username] = {
                "name": name,
                "date_of_birth": date_of_birth,
                "address": address,
                "status": "Pending"
            }
            print(f"Application submitted successfully, {name}!")
#Function to "upload" documents manually
    def upload_documents(self):
        print(" Upload Documents for National ID ")
#Prompts user to enter the type of doc and input the content themselves
        while True:
            doc_type = input("What type of document are you uploading? (e.g. birth certificate, passport, etc.): ")
            content = input("Please enter the content of the document: ")
            self.documents[doc_type] = content
            
            more = input("Is there more content to add? (Y/N): ")
            if more == "N":
                break
        
        print("Documents uploaded successfully!")
        print(f"You uploaded {len(self.documents)} document(s).")
        
        # Display uploaded documents
        if self.documents:
            print("\nUploaded documents:")
            for doc_type in self.documents:
                print(f"- {doc_type}")
#Function to view uploaded documents and their content 
    def view_documents(self):
        if self.documents:
            print("Your uploaded documents:")
            for doc_type, content in self.documents.items():
                print(f"- {doc_type}: {content}")
        else:
            print("No documents uploaded yet.")
#Function that checks application status
#Status is pending by default since we arent connecting it to a real database
    def check_application_status(self, username):
        if username in self.applications:
            print(f"Application Status: {self.applications[username]['status']}")
        else:
            print("No application found.")

    def share_documents(self):
        reciever = ("Who would you like to send the documents to?")
        if reciever in self.users:
            print(f"Documents shared with {reciever}")
        else:
            print("No users to share with.")
#Main function to run the system
#Prompts user to sign up or log in and then choose an action
    def main(self):
        print("Welcome to the National ID Application System")
        username = self.sign_up()
        while True:
            print("1. Apply for National ID")
            print("2. Upload Documents")
            print("3. View Documents")
            print("4. Check Application Status")
            print("5. Share Documents")
            print("6. Exit")

            choice = input("Please enter your choice (1-5): ")
            if choice == '1':
                self.apply_for_national_id(username)
            elif choice == '2':
                self.upload_documents()
            elif choice == '3':
                self.view_documents()
            elif choice == '4':
                self.check_application_status(username)
            elif choice == '5': 
                self.share_documents()
            elif choice == '5':
                print("Thank you for using the National ID Application System!")
                break
            else:
                print("Invalid choice. Please try again.")