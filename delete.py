import sqlite3

conn = sqlite3.connect('acer.db')
print("opened database successfully")

conn.execute("DELETE from EMPLOYEE where id=2")
conn.commit()

cursor = conn.execute("SELECT* from EMPLOYEE")
cursor1 = conn.execute("SELECT id, name, age, address, salary from EMPLOYEE")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("AGE = ", row[2])
    print("ADDRESS = ", row[3])
    print("SALARY = ", row[4])
print("Operation done successfully")
conn.close()
