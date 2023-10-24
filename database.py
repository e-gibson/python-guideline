import sqlite3

# create a database and in this case it's called Acer
conn = sqlite3.connect('acer.db')
print("Opened database successfully")


# create a table in sqlite3
conn.execute('''
CREATE TABLE EMPLOYEE(
ID INT PRIMARY KEY NOT NULL ,
NAME TEXT NOT NULL ,
AGE INT NOT NULL ,
ADDRESS CHAR(50),
SALARY REAL
);
''')
print("Table created successfully")
conn.close()