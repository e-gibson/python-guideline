import sqlite3

# connect to db
conn = sqlite3.connect('acer.db')
print("Opened Database successfully")

# inserting values in db
# method called execute performs operations
conn.execute("INSERT INTO EMPLOYEE(ID, NAME, AGE, ADDRESS, SALARY)\
             VALUES(1, 'Jeff', 33, 'California', 45000.00)");

conn.execute("INSERT INTO EMPLOYEE(ID, NAME, AGE, ADDRESS, SALARY)\
             VALUES(2, 'Allen', 25, 'Texas', 15000.00)");

conn.execute("INSERT INTO EMPLOYEE(ID, NAME, AGE, ADDRESS, SALARY)\
             VALUES(3, 'Mark', 23, 'Norway', 145000.00)");

conn.execute("INSERT INTO EMPLOYEE(ID, NAME, AGE, ADDRESS, SALARY)\
             VALUES(4, 'Brendah', 30, 'Kenya', 25000.00)");

# saving changes
conn.commit()
print("Records created successfully")
# close connection
conn.close()