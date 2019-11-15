# backend initial commit
# nothing submitted thus far. Hugo 11_13_2019
# testing Hugo 11_15_2019

import sqlite3 #  -steven
c = conn.cursor()

#create table
c.execute('''CREATE TABLE stocks 
            (date text, trans text, symbol text, qty real, price real)''')

# insert a row of data
conn.commit()

conn.close()

