import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="123"
    ) 
cur = connection.cursor()
select_query = """SELECT * FROM Phonebook;"""
create_table_query = '''CREATE TABLE IF NOT EXISTS Phonebook(
        name VARCHAR(50),
        surname VARCHAR(50),
        number VARCHAR(50)
        );'''

cur.execute(create_table_query)
cur.execute(select_query)
data = cur.fetchall()

def update_from_file(path):
    f = open(rf"{path}")
    for line in f.readlines():
        new_line = line.split(",")
        add_users_query = f"""INSERT INTO Phonebook
            (name, surname, number) VALUES ('{new_line[0]}','{new_line[1]}','{new_line[2]}');"""
        cur.execute(add_users_query)

def update():
    mode = input("""Choose operation:
1 to add user
2 to stop adding
3 to update data
4 to update data from file
5 to delete data
6 to get data
""")

    if mode == "1":
        name = input("Type your name: ")
        surname = input("Type your surname: ")
        number = input("Type your number: ")
        add_users_query = f"""INSERT INTO Phonebook
            (name, surname, number) VALUES ('{name}', '{surname}', '{number}');"""
        cur.execute(add_users_query)
        return True
    
    elif mode == "2":
        return False
    
    elif mode == "3":
        oper = input("Type:\n1 to change name\n2 to change number\n")
        if oper == "1":
            name = input("Type your name: ")
            if name in data:
                new_name = input("Type new name: ")
                change_name_query = f"""UPDATE Phonebook SET name = '{new_name}' WHERE name = '{name}';"""
                cur.execute(change_name_query)
                return True
            else:
                print("Your name not found. Try again")
                return True
        elif oper == "2":
            number = input("Type your number: ")
            if number in data:
                new_number = input("Type new number: ")
                change_name_query = f"""UPDATE Phonebook SET number = '{new_number}' WHERE number = '{number}';"""
                cur.execute(change_name_query)
                return True
            else:
                print("Your number not found. Try again")
                return True
            
        else:
            print("Error, try again")
            return True
        
    elif mode == "4":
        filepath = input("Enter filepath: ")
        update_from_file(filepath)
        return True

    elif mode == "5":
        oper = input("Type:\n1 to delete by name\n2 to delete by number\n")
        if oper == "1":
            name = input("Type your name: ")
            if name in data:
                delete_query = f"DELETE FROM phonebook WHERE name = '{name}'"
                cur.execute(delete_query)
                return True
            else:
                print("Your number not found. Try again")
                return True
        elif oper == "2":
            number = input("Type your number: ")
            if number in data:
                delete_query = f"DELETE FROM phonebook WHERE number = '{number}'"
                cur.execute(delete_query)
                return True
            else:
                print("Your number not found. Try again")
                return True
        else:
            print("Error, try again")
            return True
        
    elif mode == "6":
        oper = input("Type, what do you want to get(name, surname, number): ")
        if oper == "name":
            name = input("Type name: ")
            get_query = f"SELECT * FROM phonebook WHERE name = '{name}'"
            cur.execute(get_query)
            print(cur.fetchall())
        elif oper == "surname":
            surname = input("Type surname: ")
            get_query = f"SELECT * FROM phonebook WHERE surname = '{surname}'"
            cur.execute(get_query)
            print(cur.fetchall())

        elif oper == "number":
            number = input("Type number: ")
            get_query = f"SELECT * FROM phonebook WHERE number = '{number}'"
            cur.execute(get_query)
            print(cur.fetchall())
        else:
            print("Error, try again")
            return True
                
    else:
            print("Error, try again")
            return True
    

while True:
    if not update():
        break


connection.commit()
cur.close()
connection.close()