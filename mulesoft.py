import sqlite3

#create database
try:
    sqliteConnection = sqlite3.connect('database.db')
    cursor = sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")

    sqlite_select_Query = "select sqlite_version();"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    print("SQLite Database Version is: ", record)
    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")


#create table

try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    con = '''CREATE TABLE Movies(id INTEGER PRIMARY KEY,mname TEXT NOT NULL,actorname TEXT NOT NULL,actoressname TEXT NOT NULL,director TEXT NOT NULL,yearofrelease INT NOT NULL);'''
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")
    cursor.execute(con)
    sqliteConnection.commit()
    print("SQLite table created")

    cursor.close()

except sqlite3.Error as error:
    print("Error while creating a sqlite table", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("sqlite connection is closed")

#insert data
try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")

    con = """INSERT INTO Movies(id,name, actor, actress, director, year of release) VALUES (1,'Hum Sath Sath hain','Salmankhan','Sonali bandre','Sooraj Barjatya',1999)"""
    

    count = cursor.execute(con)
    sqliteConnection.commit()
    print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("record not inserted", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")