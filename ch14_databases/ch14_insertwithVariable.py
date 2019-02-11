# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 14:34:18 2019

@author: gracy
"""


import sqlite3
import time
import datetime
import random
conn=sqlite3.connect('task2.db')
c=conn.cursor()

### Task 1 and 2

def create_table():
      c.execute ('CREATE TABLE IF NOT EXISTS stuffToBuild1(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')
#stuffToBuild is the database table name
# unix, datestamp, keyword, value are the column names in the database table. any names can be defined
# REAL and TEXT are the data types and format in each column, which are also SQL language      

create_table() 

def dynamic_data_entry():
      unix=time.time()
      date=str(datetime.datetime.fromtimestamp(unix).strftime('%d-%m-%Y, %H:%M:%S'))
      keyword='Python'
    
      value=random.randrange(0,10)
      c.execute('INSERT INTO stuffToBuild1(unix, datestamp, keyword, value) VALUES (?,?,?,?)', (unix, date, keyword, value))
      conn.commit()

for i in range (10):
      dynamic_data_entry()
      time.sleep(1) #the use of time.sleep(1) slows down the process so that the time values are not all the same
   
# after inserting values into a database, you will need to close the table and database with:
#c.close()
#conn.close()

### Task 3

def read_from_db_all():
      c.execute ('SELECT * FROM stuffToBuild1 WHERE value =8')
      for row in c.fetchall():
            print(row)
# the fetchall function is similar to the pull function in git
            
#read_from_db_all() 
# notice that this prints the results to the console

def read_from_db2():
      c.execute('SELECT * FROM stuffToBuild1 WHERE value =8 and unix>1534855733 and unix <1564855741 ')
      for row in c.fetchall():
            print (row[0]) #this shows you the unix values only, not the entire record 
            
read_from_db2()