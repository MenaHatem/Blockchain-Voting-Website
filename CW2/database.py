from sqlite3 import *

##this is the connection to the database to be able to create tables inside of it##
conn = connect("database.db")

conn.execute(''' CREATE TABLE Users ( 
                   ID        INTEGER  PRIMARY KEY  AUTOINCREMENT ,
                   USERNAME  TEXT                  NOT NULL      ,
                   EMAIL     TEXT     UNIQUE       NOT NULL      ,  
                   VOTE      TEXT                  NOT NULL  
                 )''')
                 
conn.close()