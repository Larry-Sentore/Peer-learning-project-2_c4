import sqlite3


def connect():
    """Connect to the SQLite database."""
    conn = sqlite3.connect('data_handling.db')
    c = conn.cursor()
    return conn,c

def create_tables():

    c, conn = connect()

    c.execute("""CREATE TABLE IF NOT EXISTS users(
          username text,
          password text        
          )""")

    c.execute("""CREATE TABLE IF NOT EXISTS applications(
          username text,
          name text,
          date_of_birth text,
          address text,
          status text
          )""")

    c.execute("""CREATE TABLE IF NOT EXISTS documents(
          username text,
          doc_type text,
          content text
          )""")

def view_table(table_name):
    conn = sqlite3.connect('data_handling.db') 
    c = conn.cursor()

    c.execute(f"SELECT * FROM {table_name}")  
    rows = c.fetchall()  

    if rows:
        print(f"Data from {table_name}:")
        for row in rows:
            print(row)
    else:
        print(f"No data found in {table_name}")

    conn.close() 

#view_table("users")  # Check users table
#view_table("applications")  # Check applications table
#view_table("documents")  # Check documents table


if __name__ == "__main__":
    create_tables()
    print("Database initialized successfully.")
