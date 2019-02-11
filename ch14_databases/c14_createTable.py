# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 14:34:18 2019

@author: gracy
"""
#import sqlite3
##import mysql.connector
#myd   host="localhost",
#      user="yourusername",
#      passwd="yourpassword"
#)b = sqlite3.connector.connect(
#   
#mycursor=mydb.cursor()
#mycursor.execute("CREATE DATABASE mydatabase")

import sqlite3
conn=sqlite3.connect('task1.db')
c=conn.cursor()

def create_table():
      c.execute ('CREATE TABLE IF NOT EXISTS stuffToBuild(unix REAL, datestamp TEXT, key_word TEXT, value REAL)')
#stuffToBuild is the database table name
# unix, datestamp, keyword, value are the column names in the database table. any names can be defined
# REAL and TEXT are the data types and format in each column, which are also SQL language      
def data_entry ():
      c.execute("INSERT INTO stuffToBuild VALUES (142233222, '2018-01-01', 'python', 5)")
      conn.commit() 
#      c.close()
#      conn.close()


#in the create_table function i created 4 columns in the database so i will need to insert 4 values into the table,
      # one for each column.
      
# after inserting values into a database, you will need to close the table and database with:
      
#c.close()
#conn.close()


# now we call the function to create a table.
create_table()
data_entry()     