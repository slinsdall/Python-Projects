import sqlite3

#This is creating a database
conn = sqlite3.connect('assignments.db')

with conn:
    cur = conn.cursor()
    #This will create a table in the db with 2 columns, one auto for ID and second is going to have data input
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_filelist( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_filename TEXT)")
    conn.commit()
conn.close()

conn = sqlite3.connect('assignments.db')

#This is a tuple
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg',)

#For loop will look for the files ending in txt
for x in fileList:
    if x.endswith('txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_filelist (col_filename) VALUES (?)", (x,))
            print(x)
conn.close()



