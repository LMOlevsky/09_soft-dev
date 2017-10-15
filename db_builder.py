import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================

courses_file = csv.DictReader(open("courses.csv"))
peeps_file = csv.DictReader(open("peeps.csv"))

c.execute("CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER);")
c.execute("CREATE TABLE peeps (name TEXT, age INTEGER, id INTEGER);")

for row in courses_file:
    command = "INSERT INTO courses VALUES (" + "'"+row["code"]+"'," + row["mark"] + "," + row["id"] + ");"
    c.execute(command)

for row in peeps_file:
    command = "INSERT INTO peeps VALUES (" + "'"+row["name"]+"'," + row["age"] + "," + row["id"] + ");"
    c.execute(command)

#==========================================================
db.commit() #save changes
db.close()  #close database


