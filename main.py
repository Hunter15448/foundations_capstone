import sqlite3
import csv
import bcrypt

connection = sqlite3.connect("dp_capstone.db")
cursor = connection.cursor()

with open("schema.sql") as my_queries:
    queries = my_queries.read()

cursor.executescript(queries)

# ------------------------------------------------------- LOGIN SCREEN

login_screen = '''
WELECOME TO THE COMPENTECY INTERFACE 

PLEASE LOGIN BY USING YOUR EMAIL AND PASSOWRD
'''
# ------------------------------------------------------- MANAGER INTEFACE
manager_interface = '''
MANAGER INTERFACE
[1] VIEW 

[2] ADD 

[3] EDIT 

[4] DELETE 

[5] CVS IMPORT/ EXPORT

[6] Quit
'''

view = '''
WHAT WOULD YOU LIKE TO VIEW?
[1] view all users in a list
[2] search for users by first name or last name
[3] view a report of all users and their competency levels for a given competency
[4] view a competency level report for an individual user
[5] view a list of assessments for a given user
[6] go back
'''
add_interface ='''
WHAT WOULD YOU LIKE TO ADD?
[1] add a user
[2] add a new competency
[3] add a new assessment to a competency
[4] add an assessment result
[5] go back
'''

edit = '''
WHAT WOULD YOU LIKE TO EDIT?
[1] edit a user's information
[2] edit a competency
[3] edit an assessment
[4] edit an assessment result
[5] go back
'''

delete = '''
WHO'S INFORMATION WOULD YOU LIKE TO DELETE?
PLEASE ENTER THEIR NAME HERE:
'''
csv_imp_ex = '''
[1] IMPORT ASSESMENT RESULTS CSV TO DATABASE
[2] IMPORT USER INFO FROM CSV TO DATABASE
[3] EXPORT ASSESSMENT RESULTS FROM DATABASE TO CSV
[4] GO BACK
'''
# ------------------------------------------------------- USER INTERFACE
user_interface = '''
EMPLOYEE INTERFACE

[1] View your test scores   

[2] Change personal info

[3] QUIT  

'''
# _____________________________________________
# |                                           |
# |  EMPLOYEE INTERFACE                       |
# |___________________________________________|
# |                                           |
# |  [1] View your test scores                |                                         
# |  [2] Change personal info     .____.      |
# |  [3] QUIT         .---------. | == |      |
# |                   |.-"""""-.| |----|      |
# |                   ||       || | == |      |
# |                   ||       || |----|      |
# |                   |'-.....-'| |::::|      |
# |                   `"")---(""` |___.|      |
# |                   /:::::::::::\" _  "      |
# |                  /:::=======:::\`\`\      |
# |                  `"""""""""""""`  '-'     |                 
# _____________________________________________
update_user = '''
WHAT INFO WOULD YOU LIKE TO UPDATE?

[1] EMAIL

[2] PHONE 

[3] PASSOWRD

[4] GO BACK
'''

# ------------------------------------------------------ DELETE USER

cool_interface = '''
_____________________________________________
|                                           |
|  EMPLOYEE INTERFACE                       |
|___________________________________________|
|                                           |
|  [1] EMAIL                                |                                         
|  [2] PHONE                    .____.      |
|  [3] PASSOWRD     .---------. | == |      |
|  [4] GO BACK      |.-"""""-.| |----|      |
|                   ||       || | == |      |
|                   ||       || |----|      |
|                   |'-.....-'| |::::|      |
|                   `"")---(""` |___.|      |
|                   /:::::::::::\" _  "      |
|                  /:::=======:::\`\`\      |
|                  `"""""""""""""`  '-'     |                 
_____________________________________________ 
'''

# ------------------------------------------------------- CSV ASSESSMENT EXPORT

def csv_reader():
    csv_name = input('Please enter the name of the CSV file you would like to import')
    with open(f'{csv_name}') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'{" ".join(row)}')
                line_count += 1
            else:
                query = "INSERT INTO Assessment_Results (user_id, name_of_assessment, score, date_taken, manager) values(?, ?, ?, ?, ?)"
                val1 = (row[0])
                val2 = (row[1])
                val3 = (row[2])
                val4 = (row[3])
                val5 = (row[4])
                values = (val1, val2, val3, val4, val5)

                cursor.execute(query, values)
                connection.commit()
                print(f'{row[0]:<8}{row[1]:<14}{row[2]:<6}{row[3]:<6}')

                line_count += 1
# csv_reader()
# ------------------------------------------------------- CSV USER IMPORT
def csv_writer():  
    header = ('User_id','First Name','Last Name','Email','Phone','User Typer','Hire Date','Date Created','Active Status')
    rows = cursor.execute("SELECT * FROM Users").fetchall()
    csv_name = input('Please enter the name of the CSV file you would like to export: ')
    with open(f'{csv_name}', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)
# csv_writer()
# ------------------------------------------------------- CSV ASSESSMENT RESULTS IMPORT
def csv_test():  
    header = ('User_id','Assessment_id','Score','Date_taken')
    rows = cursor.execute("SELECT * FROM Assessment_Results").fetchall()
    csv_name = input('Please enter the name of the CSV file you would like to export: ')
    with open(f'{csv_name}', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)
# csv_test()

    
# ------------------------------------------------------- VIEW ALL USERS

def view_people():
    rows = cursor.execute("SELECT * FROM Users").fetchall();
    print(f'\n{"ID":3} {"First Name":<12}{"Last Name":<12}')

    for row in rows:
        print(f'{row[0]:<4}{row[1]:<12}{row[2]:<12}')


# ------------------------------------------------------- SEARCH USER BY NAME

def search_by_name():
    query = "SELECT * FROM Users WHERE first_name LIKE ?"
    value = input("Please enter the name of the individual you would like to know more about: ")
    value = (f'%{value}%')
    results = cursor.execute(query,(value,)).fetchall()
    print(f'\n{"ID":3} {"First Name":<25}{"Last Name":<17}')

    for row in results:
        print(f'\n{row[0]:<4}{row[1]:<25}{row[2]:<17}')

# ------------------------------------------------------- VIEW COMPENTENCY OF ALL USERS

def view_all_compentencies():
    rows = cursor.execute("SELECT * FROM COMPENTENCIES").fetchall();
    print(f'\n{"ID":3} {"Compentency":<12}{"Date":<12}')

    for row in rows:
        print(f'{row[0]:<4}{row[1]:<12}{row[2]:<12}')

# ------------------------------------------------------- VIEW COMPENTENCY OF A USER

def search_compentacy_level():
    query = "SELECT * FROM COMPENTENCIES WHERE user_id LIKE ?"
    value = input("Please enter the User Id that you would like to know the compentency of: ")
    value = (f'%{value}%')
    results = cursor.execute(query,(value,)).fetchall()
    print(f'\n{"ID":3} {"First Name":<25}{"Last Name":<17}')

    for row in results:
        print(f'\n{row[0]:<4}{row[1]:<25}{row[2]:<17}')
    query1 ="SELECT AVG(score) FROM Assessment_Results WHERE user_id LIKE ?"

    cursor.execute(query1, (value,))
    avg=cursor.fetchall()
    for row in avg:
        print(f'\nThe users average compentecies is {row[0]}%')

# ------------------------------------------------------- VIEW LIST OF ASSESSMENTS FOR A USER
# def average():
#     query ="SELECT AVG(score) FROM Assessment_Results WHERE user_id=?"
#     value = input('please enter a user id:')
#     cursor.execute(query, value)
#     avg=cursor.fetchall()
#     for row in avg:
#         print(f'The users average is {row[0]}%')
# average()
# ------------------------------------------------------- VIEW LIST OF ASSESSMENTS FOR A USER

def search_assessments():
    query = "SELECT * FROM Assessments WHERE user_id LIKE ?"
    value = input("Please enter the User Id that you would like to know the assessments of: ")
    value = (f'%{value}%')
    results = cursor.execute(query,(value,)).fetchall()
    print(f'\n{"ID":3} {"First Name":<25}{"Last Name":<17}')

    for row in results:
        print(f'\n{row[0]:<4}{row[1]:<25}{row[2]:<17}')
# ------------------------------------------------------ CODE HASHING PASSWORDS
# def code_hash():
    
    # rows = ("SELECT password FROM Users WHERE email=?")
    # val3 = input('please confirm email. This may take awhhile. Please wait.:')
    # cursor.execute(rows, (val3,))
    # for row in rows:
        # bytes = val3.encode('utf-8')
        # salt = bcrypt.gensalt()
        # hash = bcrypt.hashpw(bytes, salt)
        # query = ('UPDATE Users SET password=?')
        # cursor.execute(query, (hash,))
        # connection.commit()
# code_hash()
# ------------------------------------------------------- ADD USER

def add():
    query = "INSERT INTO Users (first_name, last_name, email, phone, password, user_type, hire_date, date_created, active) values(?, ?, ?, ?, ?, ?, ?, ?, ?)"
    val1 = input("Please enter a first name: ")
    val2 = input("Please enter a last name: ")
    val4 = input("Please enter a phone number: ")
    val5 = input("Please enter a Password: ")
    bytes = val5.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)
    val6 = input("Please enter a user type: ")
    val7 = input("Please enter a hire date: ")
    val8 = input("Please enter date created: ")
    val3 = input("please enter a email:")
    val10 = ("1")
    values = (val1, val2, val3, val4, hash, val6, val7, val8, val10)
    cursor.execute(query, values)
    connection.commit()
#     print(f'\n{values[0]} was added to the database and your Login is your first name')
# add()

# ------------------------------------------------------- ADD Compentency


def add_comp():
    print()
    query = "INSERT INTO COMPENTENCIES (user_id, name, date_created) values(?, ?, ?)"
    val0 = input('Please enter a user_id')
    val4 = input(''' 

    Please type out a compentecy below that you would like to report on
    ---------------------------------------------------------------------
    Data Types
    Variables
    Functions
    Boolean Logic
    Conditionals
    Loops
    Data Structures
    Lists
    Dictionaries
    Working with Files
    Exception Handling
    Quality Assurance (QA)
    Object-Oriented Programming
    Recursion
    Databases
    ''')
  
    val2 = input("Please enter todays date: ")
    
    values = (val0, val4, val2)

    cursor.execute(query, values)
    connection.commit()
    print(f"\nUser {values[0]}'s compentency was added to the database!")


# ------------------------------------------------------ ADD ASSIGNMENT

def add_assessment():
    query = "INSERT INTO Assessments (user_id, name_of_assessment, date_created) values(?, ?, ?)"
    val0 = input('Please enter a user_id: ')
    val1 = input("Please enter name of assesment: ")
    val2 = input("Please enter date test was taken: ")
   
    values = (val0, val1, val2)

    cursor.execute(query, values)
    connection.commit()
    print(f"\nUser {values[0]}'s test was added to the database!")


# ------------------------------------------------------ ADD ASSIGNMENT RESULTS

def add_assessment_results():
    query = "INSERT INTO Assessment_Results (user_id, name_of_assessment, score, date_taken, manager) values(?, ?, ?, ?, ?)"
    val0 = input('Please enter a user_id: ')
    val1 = input(''' 

    Please type out a compentecy below that you would like to report on
    ---------------------------------------------------------------------
    Data Types
    Variables
    Functions
    Boolean Logic
    Conditionals
    Loops
    Data Structures
    Lists
    Dictionaries
    Working with Files
    Exception Handling
    Quality Assurance (QA)
    Object-Oriented Programming
    Recursion
    Databases
    ''')
    val2 = input('''
    Competencies are measured and tracked on a scale from 0-4:
    0 - No competency - Needs Training and Direction
    1 - Basic Competency - Needs Ongoing Support
    2 - Intermediate Competency - Needs Occasional Support
    3 - Advanced Competency - Completes Task Independently
    4 - Expert Competency - Can Effectively pass on this knowledge and can initiate optimizations

    Enter where the employee is on the scale:
    ''')
    val3 = input("Please enter date test was taken: ")
    val4 = input("Please enter manager: ")
   
    values = (val0, val1, val2, val3, val4)

    cursor.execute(query, values)
    connection.commit()
    print(f"\nUser {values[0]}'s test was added to the database!")

# ------------------------------------------------------ UPDATE USER EMAIL

def update_email():
    query = "UPDATE Users SET email=? WHERE user_id=?"
    
    val4 = input("Please enter new email: ")
    value = input("Please enter your user ID: ")

    values = (val4, value)

    cursor.execute(query, values)
    connection.commit()

# ------------------------------------------------------ UPDATE USER PHONE

def update_phone():
    query = "UPDATE Users SET phone=? WHERE user_id=?"
    
    
    val5 = input("Please enter a new phone: ")
    value = input("Please enter your user ID: ")

    values = (val5, value)

    cursor.execute(query, values)
    connection.commit()

# ------------------------------------------------------ UPDATE USER PASSWORD

def update_password():
    query = "UPDATE Users SET password=? WHERE user_id=?"
    
    val6 = input("Please enter a new password: ")
    value = input("Please enter your user ID: ")

    values = (val6, value)

    cursor.execute(query, values)
    connection.commit()

# ------------------------------------------------------ EDIT COMPENTENCY

def update_users_compentency():
    query = "UPDATE COMPENTENCIES SET name=? WHERE user_id=? AND name=?"
    
    val18 = input("what test would you like to change:")
    value = input("User ID please: ")
    val8 = input("what is the new test name?: ")

    values = (val8, value,val18)

    cursor.execute(query, values)
    connection.commit()


# ------------------------------------------------------ EDIT ASSESSMENT

def update_users_assessment():
    query = "UPDATE Assessments SET name_of_assessment=? WHERE user_id=? AND name_of_assessment=?"
    
    val18 = input("what test would you like to change: ")
    value = input("User ID please: ")
    val8 = input("what is the new test name?: ")

    values = (val8, value,val18)

    cursor.execute(query, values)
    connection.commit()


# ------------------------------------------------------ EDIT ASSESSMENT RESULTS

def update_users_results():
    query = "UPDATE Assessment_Results SET score=? WHERE user_id=? AND name_of_assessment=?"
    
    val18 = input("what test would you like to change: ")
    value = input("User ID please: ")
    val8 = input("please enter a new score: ")

    values = (val8, value,val18)

    cursor.execute(query, values)
    connection.commit()

# ------------------------------------------------------ DELETE USER

def update_active_status():
    query = "UPDATE Users SET active=? WHERE user_id=?"
    
    val8 = input("Please enter a 1 for active or a 0 to deactivate: ")
    value = input("Please enter the User Id that you would like to know the assessments of: ")

    values = (val8, value)

    cursor.execute(query, values)
    connection.commit()


# ------------------------------------------------------ CODE HASHING PASSWORDS
def code_encoder():
    row = cursor.execute("SELECT password FROM Users WHERE user_id=?",(10,)).fetchone()
    hash = row[0]
    user = input().encode('utf-8')
    result = bcrypt.checkpw(user, hash)
    print(result)
# ------------------------------------------------------ CODE FOR USER INTERFACE

def user_space():
    while True:
        start = input(user_interface)
        if start == '1':
            search_assessments()
            start
        elif start == '2':
            while True:
                cool = input(update_user)
                if cool == '1':
                    update_email()
                    cool
                elif cool == '2':
                    update_phone()
                    cool
                elif cool == '3':    
                    update_password()
                    cool
                elif cool == '4':
                    start
                    break
        elif start == '3':
            quit()
# user_space()

# ------------------------------------------------------ CODE FOR MANGER INTERFACE

def manager_space():
    while True:
        start = input(manager_interface)
        if start == "1":
            while True:
                view_input = input(view)
                if view_input == '1':
                    view_people()
                elif view_input == '2':
                    search_by_name()
                elif view_input == '3':
                    view_all_compentencies()
                elif view_input == '4':
                    search_compentacy_level()
                elif view_input == '5':
                    search_assessments()
                elif view_input == '6':
                    start
                    break
        elif start == "2":
            while True:
                add_loadout = input(add_interface)
                if add_loadout == '1':
                    add()
                elif add_loadout == '2':
                    add_comp()
                elif add_loadout == '3':
                    add_assessment()
                elif add_loadout == '4':
                    add_assessment_results()
                elif add_loadout == '5':
                    start
                    break
        elif start == "3":
            while True:
                edit_input = input(edit)
                if edit_input == "1":
                    while True:
                        cool = input(update_user)
                        if cool == '1':
                            update_email()
                            cool
                        elif cool == '2':
                            update_phone()
                            cool
                        elif cool == '3':    
                            update_password()
                            cool
                        elif cool == '4':
                            start
                            break
                elif edit_input == "2":
                    update_users_compentency()
                elif edit_input == "3":
                    update_users_assessment()
                elif edit_input == "4":
                    update_users_results()
                elif edit_input == "5":
                    start
                    break
        elif start == "4":
            while True:
                delete_interface = input('''
DEACTIVATE A EMPLOYEES
[1] CONTINUE WITH DEACTIVATION
[2] GO BACK
''')
                if delete_interface == '1':
                    update_active_status()
                elif delete_interface == '2':
                    start
                    break
        elif start == "5":
            while True:
                csv_interface = input(csv_imp_ex)
                if csv_interface == '1':
                    csv_test()
                elif csv_interface == '2':
                    csv_writer()
                elif csv_interface == '3':
                    csv_reader()
                elif csv_interface == '4':
                    start
                    break
        elif start == "6":
            quit()
# manager_space()

# ------------------------------------------------------ PASSWORD LOGIN
def pass_login():
    print(login_screen)
    query = ("SELECT password FROM Users WHERE email=?")
    email = input('PLEASE ENTER YOUR EMAIL:\n')
    password = input('PLEASE ENTER YOUR PASSWORD:\n')
    row = cursor.execute(query, (email,)).fetchone()
    encoder = password.encode('utf-8')
    if row:
        results = bcrypt.checkpw(encoder, row[0])
        print(row)
        print(results)
    
        while True:
            query = ("SELECT user_type FROM Users WHERE email=?")
            # usable_email = str(email)
            row = cursor.execute(query, (email,))
            connection.commit()
            for rows in row:
                user_type = (rows[0])
                lower = user_type.lower()
            if lower == 'manager':
                manager_space()
            else:
                user_space()
    else:
        print("\n-----PLEASE LOG IN AGAIN-----")
        return
        

while True:            
        pass_login()

