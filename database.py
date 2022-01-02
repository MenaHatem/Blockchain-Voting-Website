from sqlite3 import *

conn = connect("database.db")

conn.execute(''' CREATE TABLE Users ( 
                   ID        INTEGER  PRIMARY KEY  AUTOINCREMENT ,
                   USERNAME  TEXT                  NOT NULL      ,
                   EMAIL     TEXT     UNIQUE       NOT NULL      
                 )''')

conn.execute(''' CREATE TABLE Vote ( 
                   ID        INTEGER  PRIMARY KEY  AUTOINCREMENT ,
                   VOTE      TEXT                  NOT NULL                 
                 )''')
conn.close()