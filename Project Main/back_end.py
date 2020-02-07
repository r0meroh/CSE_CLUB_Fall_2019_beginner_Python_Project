# backend initial commit

import sqlite3
# hello dorian

def start():
    conn = sqlite3.connect('shoes.db')
    c = conn.cursor()
    # Create table
    c.execute('CREATE TABLE IF NOT EXISTS shoe(brand text, model text, price text)')
    # insert
    conn.commit()
    conn.close()

def insert(brands, models, prices):
    conn = sqlite3.connect('shoes.db')
    c = conn.cursor()
    c.execute('INSERT INTO shoe Values(?,?,?)', (brands, models, prices))
    conn.commit()
    conn.close()

def print_me():
    conn = sqlite3.connect('shoes.db')
    c = conn.cursor()
    for row in c.execute('SELECT * FROM shoe ORDER BY price'):
        print(row)
    c.execute('SELECT * FROM shoe ORDER BY price')
    rows = c.fetchall()
    conn.close()
    return rows

# Steven Ortega 12/17/2019
def remove_shoe(Model):
    conn = sqlite3.connect('shoes.db')
    c = conn.cursor()
    c.execute('DELETE FROM shoe WHERE model=?',(Model,))
    conn.commit()
    conn.close()
# Christian Mesina 12/17/2019
def search_shoe(brand='',model='',price=''):
    conn = sqlite3.connect('shoes.db')
    c = conn.cursor()
    for row in c.execute('SELECT * FROM shoe WHERE brand=?',(brand,)):
        print(row)

    c.execute('SELECT * FROM shoe WHERE brand=? OR model=? OR price=?',(brand,model,price))
    row = c.fetchall()
    conn.close()
    return row

start()
#print_me()
#shoe = input("brand")
#mod = input("model")
#cash = input("price")
#insert(shoe, mod, cash)
#print_me()

#r = input("Enter a shoe to be removed: ")
#remove_shoe(r)
#print_me()

#s = input("Enter a shoe to be searched: ")
#search_shoe(s)
