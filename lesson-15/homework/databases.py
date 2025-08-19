# Create a new database with a table named Roster that has three fields: 
# Name, Species, and Age. 
# The Name and Species columns should be text fields, 
# and the Age column should be an integer field.

import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Roster1 (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)''')

cursor.executemany('''INSERT INTO Roster1 (Name, Species, Age) VALUES (?, ?, ?)''', [
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29)
])

conn.commit()

cursor.execute('''UPDATE Roster1
               SET Name = 'Ezri Dax'
               WHERE Name = 'Jadzia Dax'
''')

cursor.execute('SELECT * FROM Roster1')
result = cursor.fetchall()
for row in result:
    print(row)

cursor.execute('''SELECT Name, Age FROM Roster1 WHERE Species = 'Bajoran' ''')
result = cursor.fetchall()
for row in result:
    print(row)

conn.close()
