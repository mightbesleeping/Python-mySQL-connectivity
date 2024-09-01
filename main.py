import mysql.connector as msql

def connect_to_database():
    host = 'localhost'
    user = 'root'
    password = input("Enter MySQL password: ")

    try:
        # Connect to MySQL server (not a specific database)
        cn = msql.connect(host=host, user=user, password=password)
        if cn.is_connected():
            print("Connected to MySQL server")

            # Create the database if it doesn't exist
            cur = cn.cursor()
            cur.execute("CREATE DATABASE IF NOT EXISTS student")
            print("Checked/Created the 'student' database successfully.")

            # Now connect to the 'student' database
            cn.database = 'student'
            return cn
    except msql.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def create_table(cn):
    cur = cn.cursor()
    try:
        cur.execute('''
            CREATE TABLE IF NOT EXISTS train (
                train_no VARCHAR(10) PRIMARY KEY,
                train_name VARCHAR(100) NOT NULL,
                time TIME,
                date_of_arrival DATE,
                platform_no INT
            )
        ''')
        print("Checked/Created the 'train' table successfully.")
    except msql.Error as e:
        print(f"Error creating table: {e}")

def list_trains(cn):
    try:
        cur = cn.cursor()
        cur.execute('SELECT train_name, train_no, TIME_FORMAT(time, "%H:%i") AS formatted_time, date_of_arrival, platform_no FROM train')
        result = cur.fetchall()
        for row in result:
            train_name, train_no, formatted_time, date_of_arrival, platform_no = row
            formatted_date = date_of_arrival.strftime("%d-%m-%Y") if date_of_arrival else "N/A"
            print(f"Train Name: {train_name}, Train No: {train_no}, Time: {formatted_time}, Date of Arrival: {formatted_date}, Platform No: {platform_no}")
    except msql.Error as e:
        print(f"Error fetching train list: {e}")

def show_train_details(cn):
    cv = input('Enter train no.: ').strip()
    cur = cn.cursor()
    try:
        cur.execute('SELECT * FROM train WHERE train_no = %s', (cv,))
        result = cur.fetchall()
        if result:
            for row in result:
                train_no, train_name, time, date_of_arrival, platform_no = row
                formatted_time = str(time) if time else "N/A"
                formatted_date = date_of_arrival.strftime("%d-%m-%Y") if date_of_arrival else "N/A"
                print(f"Train No: {train_no}, Train Name: {train_name}, Time: {formatted_time}, Date of Arrival: {formatted_date}, Platform No: {platform_no}")
        else:
            print("No train found with the provided number.")
    except msql.Error as e:
        print(f"Error fetching train details: {e}")


def add_train(cn):
    print('If no value is there, enter NULL (case insensitive)')

    n1 = input('Enter train no.: ').strip()
    if not n1:
        print('Train number cannot be empty')
        return

    n2 = input('Enter train name: ').strip().upper()
    n3 = input('Enter time (HH:MM): ').strip()
    n4 = input('Enter date of arrival (YYYY-MM-DD): ').strip()
    n5 = input('Enter platform no: ').strip()

    n2 = None if n2.upper() == 'NULL' else n2
    n3 = None if n3.upper() == 'NULL' else n3
    n4 = None if n4.upper() == 'NULL' else n4
    n5 = None if n5.upper() == 'NULL' else n5

    cur = cn.cursor()
    try:
        cur.execute('''INSERT INTO train (train_no, train_name, time, date_of_arrival, platform_no) 
                       VALUES (%s, %s, %s, %s, %s)''', (n1, n2, n3, n4, n5))
        cn.commit()
        print("Train added successfully!")
    except msql.Error as e:
        print(f"Error adding the train: {e}")

def delete_train(cn):
    cv = input("Enter train no.: ").strip()
    cur = cn.cursor()
    try:
        cur.execute('DELETE FROM train WHERE train_no = %s', (cv,))
        cn.commit()
        if cur.rowcount > 0:
            print(f"Train {cv} deleted successfully!")
        else:
            print(f"No train found with the number {cv}.")
    except msql.Error as e:
        print(f"Error deleting the train: {e}")

def menu():
    c = 'y'
    while c == 'y':
        cn = connect_to_database()
        if cn:
            create_table(cn)
            print("Enter values according to the list mentioned below:")
            print("1. List of trains")
            print("2. Add train")
            print("3. Show details of a train")
            print("4. Delete a train")
            cx = int(input("Enter your query: "))

            if cx == 1:
                list_trains(cn)
            elif cx == 2:
                add_train(cn)
            elif cx == 3:
                show_train_details(cn)
            elif cx == 4:
                delete_train(cn)
            else:
                print("Invalid option")

            cn.close()
            c = input("Do you want to continue (y/n)? ").lower()

if __name__ == "__main__":
    menu()
