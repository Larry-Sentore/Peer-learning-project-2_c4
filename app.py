# This is a simple National ID Application System that allows users to sign up, login, apply for a national ID, upload documents, view documents, and check application status.
import sqlite3
from memories import connect, create_tables

class NationalIDSystem:
    def __init__(self):
        create_tables()
        self.conn, self.c = connect()
#This is to sign up and register a user
    def sign_up(self):
        choice = input("Do you want to sign up or login? (S/L): ")
        if choice == "S":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            #Check if user already exists
            self.c.execute("SELECT * FROM users WHERE username=?", (username,))
            if self.c.fetchone():
                log = input("Username already exists. if you want to log in, press L: ")
                if log == "L":
                    return self.login_user()
                else:
                    print("Please use another username.")
                    return self.sign_up()
            
            #Insert new user into the database
            self.c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            self.conn.commit()
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
        self.c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        if self.c.fetchone():
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
#Checks if user had already applied
        self.c.execute("SELECT * FROM applications WHERE username=?", (username,))
        if self.c.fetchone():
            print("You already applied for a National ID.")
        else:
            #Stores application in the database
            self.c.execute("INSERT INTO applications (username, name, date_of_birth, address, status) VALUES (?, ?, ?, ?, ?)", (username, name, date_of_birth, address, "pending"))
            self.conn.commit()
            print(f"Application submitted successfully, {name}!")

#Function to "upload" documents manually
    def upload_documents(self, username):
        print(" Upload Documents for National ID ")
#Prompts user to enter the type of doc and input the content themselves
        while True:
            doc_type = input("What type of document are you uploading? (e.g. birth certificate, passport, etc.): ")
            content = input("Please enter the content of the document: ")
            self.c.execute("INSERT INTO documents (username, doc_type, content) VALUES (?, ?, ?)", (username, doc_type, content))
            self.conn.commit()
            
            more = input("Is there more content to add? (Y/N): ")
            if more == "N":
                break
        
        print("Documents uploaded successfully!")
        
#Function to view uploaded documents and their content 
    def view_documents(self, username):
        self.c.execute("SELECT doc_type, content FROM documents WHERE username = ?", (username,))
        documents = self.c.fetchall()
        if documents:
            print("Your uploaded documents:")
            for doc_type, content in documents:
                print(f"- {doc_type}: {content}")
        else:
            print("No documents uploaded yet.")

#Function that checks application status
#Status is pending by default since we arent connecting it to a real database
    def check_application_status(self, username):
        self.c.execute("SELECT status FROM applications WHERE username = ?", (username,))
        result = self.c.fetchone()

        if result:
            print(f"Application Status: {result}")
        else:
            print("No application found.")

#Function to share documents with others 
    def share_documents(self, username):
        reciever = input("Who would you like to send the documents to?")
        #Checking if user is in the database
        self.c.execute("SELECT username FROM users WHERE username = ?", (reciever,))
        if self.c.fetchone():
            #Checking if there are documents to share
            self.c.execute("SELECT doc_type, content FROM documents WHERE username = ?", (username,))
            documents = self.c.fetchall()
            if not documents:
                print("No documents to share")
                return
            else:
                for doc in documents:
                    self.c.execute("INSERT INTO documents (username, doc_type, content) VALUES (?, ?, ?)", (reciever, doc[0], doc[1]))
                self.conn.commit()
            print(f"Documents shared with {reciever}")
        else:
            print("User does not exist")
            return 
        
#Main function to run the system
#Prompts user to sign up or log in and then choose an action
    def main(self):
        print("Welcome to the National ID Application System")
        username = self.sign_up()
        while True:
            print("------------------------")
            print("1. Apply for National ID")
            print("2. Upload Documents")
            print("3. View Documents")
            print("4. Check Application Status")
            print("5. Share Documents")
            print("6. Exit")
            print("------------------------")

            choice = input("Please enter your choice (1-5): ")
            print("------------------------")
            if choice == '1':
                self.apply_for_national_id(username)
            elif choice == '2':
                self.upload_documents(username)
            elif choice == '3':
                self.view_documents(username)
            elif choice == '4':
                self.check_application_status(username)
            elif choice == '5': 
                self.share_documents(username)
            elif choice == '6':
                print("Thank you for using the National ID Application System!")
                self.conn.close()
                break
            else:
                print("Invalid choice. Please try again.")
