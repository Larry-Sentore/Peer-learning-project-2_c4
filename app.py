#Yes guys
#This is an app that will allow citizens to apply for a national id and also store and send their other documents
def main ():
    print("Welcome to the National ID Application System")
    print("1. Apply for National ID")
    print("2. Upload Documents")
    print("3. Check Application Status")
    print("4. Exit")

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