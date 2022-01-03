from sqlite3 import *

##this is the connection to the database we want to view/add enteries to##
conn = connect("database.db")

##this is to add an inital entry to db to avoid future loops (explained in report)##
# username = "test2"
# email = "test2@gmail.com"
# vote = "the weeknd"
# conn.execute("INSERT INTO Users (USERNAME,EMAIL,VOTE) VALUES (?,?,?)" , (username,email,vote))
# conn.commit()

##to select a query to be able to view data saved in db##
cursor = conn.execute("SELECT ID,USERNAME,EMAIL,VOTE from Users")

for row in cursor:

    print(f"This is the {row[0]} entry")
    print("ID:" , row[0])
    print("Username:" , row[1])
    print("Email:" , row[2])
    print("Vote:" , row[3] , "\n")

conn.close()