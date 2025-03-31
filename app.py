#Yes guys
#This is an app that will allow citizens to apply for a national id and also store and send their other documents
def login():

def apply_for_national_id():

def upload_documents():

def check_application_status():

def view_documents():

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