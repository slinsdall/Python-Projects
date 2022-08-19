import sqlite3
connection = sqlite3.connect(r"C:\Users\slins\OneDrive\Documents\GitHub\Tech-Academy-Projects\Python-Projects\test_database.db")
c = connection.cursor()
c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
c.execute("INSERT INTO People VALUES('Ron', 'Obvious', 42)")
connection.commit()

connection = sqlite3.connect(':memory:')
c.execute("DROP TABLE IF EXISRS People")
connection.close()

with sqlite3.connect("test_database.db") as connection:
# perform any SQL operations using connection here


