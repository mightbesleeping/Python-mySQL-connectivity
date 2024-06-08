import mysql.connector as msql

def connect_to_database():
    return msql.connect(host='localhost', user='root', password='38037', database='student')

def list_trains(cn):
    cur = cn.cursor()
    cur.execute('select train_name, train_no, TIME_FORMAT(time, "%H:%i") AS formatted_time from train')
    result = cur.fetchall()
    for x in result:
        print(x)

def add_train(cn):
    print('If no value is there then enter Null')

    n1 = input('Enter train no. ')
    if n1 == 'Null':
        print('Train number cannot be empty')
        return
    elif n1 == '':
        print('Train number cannot be empty')
        return

    n2 = input('Enter train name: ').upper()
    if n2 == 'NULL':
        n2 = 'null'

    n3 = input('Enter time (HH:MM): ')
    if n3 == 'Null':
        n3 = 'null'

    n4 = input('Enter date of arrival (YYYY-MM-DD): ')
    if n4 == 'Null':
        n4 = 'null'

    n5 = input('Enter platform no: ')
    if n5 == 'Null':
        n5 = 'null'

    cur = cn.cursor()
    try:
        cur.execute(f'''INSERT INTO train 
                    VALUES ("{n1}", "{n2}", "{n3}", "{n4}", {n5})''')
        cn.commit()
        print("Train added successfully!")
    except msql.Error as e:
        print(f"Error adding the train: {e}")

def show_train_details(cn):
    cv = input('Enter train no. ')
    cur = cn.cursor()
    cur.execute(f'''SELECT * FROM train
                WHERE train_no = "{cv}"''')
    result = cur.fetchall()
    for x in result:
        print(x)

def delete_train(cn):
    cv = input("Enter train_no. ")
    cur = cn.cursor()
    cur.execute(f'''DELETE FROM train
                WHERE train_no = "{cv}"''')
    cn.commit()
    print(f"Train {cv} deleted successfully!")

def menu():
    c = 'y'
    while c == 'y':
        cn = connect_to_database()

        if cn.is_connected():
            print("Connected to the database")
        else:
            print("Connection error")

        print("Enter values according to the list mention below \nList of trains = 1 \nAdd train = 2 \nShow details of a train = 3 \nDelete a Train = 4")
        cx = int(input("Enter your query: "))

        if cx == 1:
            list_trains(cn)
        elif cx == 2:
            add_train(cn)
        elif cx == 3:
            show_train_details(cn)
        elif cx == 4:
            delete_train(cn)

        cn.close()
        c = input("Do you want to continue (y/n)? ").lower()

if __name__ == "__main__":
    menu()
