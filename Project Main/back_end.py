# backend initial commit
# nothing submitted thus far. Hugo 11_13_2019
# testing Hugo 11_15_2019

import sqlite3

def start():
    conn = sqlite3.connect('shoes.db')
    c = conn.cursor()
    # Create table
    c.execute('CREATE TABLE IF NOT EXISTS shoe(brand text, model text, price text)')
    # insert
    conn.commit()
    conn.close()


def Steven_inserts(brands, models, prices):
    conn = sqlite3.connect('shoes.db')
    c = conn.cursor()
    c.execute('INSERT INTO shoe Values(?,?,?)',(brands, models, prices))
    conn.commit()
    conn.close()

def print_me():
    conn = sqlite3.connect('shoes.db')
    c = conn.cursor()
    for row in c.execute('SELECT * FROM shoes ORDER BY price'):
        print(row)

    conn.close()

start()
shoe = input("brand")
mod = input("model")
cash = input("price")
Steven_inserts(shoe,mod,cash)
print_me()

# still working on it
# Hugo 11_15_2019

#christian is still working on it...


