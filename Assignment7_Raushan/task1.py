# python connected with database
# import psycopg2
# connect = psycopg2.connect(dbname="postgres",user="postgres",password="PGRaushan@123",host="localhost",port="5432")
# print("connected Successfully")


# create table

# import psycopg2
# conn = psycopg2.connect(dbname="postgres",user="postgres",password="PGRaushan@123",host="localhost",port="5432")

# cursor = conn.cursor()
# cursor.execute('''create table employees(Name Text,ID int, Age int);''')
# print("Table created successfully")

# conn.commit()
# conn.close()



"""
# insert daata

import psycopg2

# Create table
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="PGRaushan@123",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS employees(
    Name TEXT,
    ID INT,
    Age INT
);
''')

print("Table created successfully")

conn.commit()
cursor.close()
conn.close()


# Insert data function
def data():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="PGRaushan@123",
        host="localhost",
        port="5432"
    )

    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO employees(Name, ID, Age)
    VALUES ('Raushan', 1, 21);
    ''')

    print("Data added successfully")

    conn.commit()
    cursor.close()
    conn.close()


# Call function
data()

"""


"""
# add data


import psycopg2

# Create table
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="PGRaushan@123",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS employees(
    Name TEXT,
    ID INT,
    Age INT
);
''')

print("Table created successfully")

conn.commit()
cursor.close()
conn.close()


# Insert data function
def data():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="PGRaushan@123",
        host="localhost",
        port="5432"
    )

    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO employees(Name, ID, Age)
    VALUES ('Raushan', 1, 21);
    ''')

    print("Data added successfully")

    conn.commit()
    cursor.close()
    conn.close()


def extract():
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="PGRaushan@123",host="localhost",port="5432")
    
    
    cursor = conn.cursor()
    cursor.execute('''select * from employees;''')
    show=cursor.fetchone()
    print(show[0]) #index
    #print("Table created successfully")
    
    
    conn.commit()
    cursor.close()
    conn.close()


extract()

"""



# user input


import psycopg2

# Create table
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="PGRaushan@123",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS employees(
    Name TEXT,
    ID INT,
    Age INT
);
''')

print("Table created successfully")

conn.commit()
cursor.close()
conn.close()


# Insert data function
def data():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="PGRaushan@123",
        host="localhost",
        port="5432"
    )

    cursor = conn.cursor()
    
    name = input("Enter name : ")
    id = input("Enter id : ")
    age = input("Enter age : ")
    
    
    query=('''INSERT INTO employees(Name, ID, Age)VALUES (%s,%s,%s);''')
    cursor.execute(query,(name,id,age))

    print("Data added successfully")

    conn.commit()
    cursor.close()
    conn.close()


data()
