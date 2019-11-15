# backend initial commit
# nothing submitted thus far. Hugo 11_13_2019
# testing Hugo 11_15_2019

import sqlite3

conn = sqlite3.connect('shoes.db')


c = conn.cursor()

# Create table
# c.execute('''CREATE TABLE shoes
  #            (brand text, model text, release_date text, price text)''')

# Insert a row of data
c.execute("INSERT INTO shoes VALUES ('Adidas','yeezy boost','2017', 250.0)")


def Steven_inserts():
    brands = input("brand")
    models = input("model")
    releases = input("release")
    prices = input("price")

    c.execute("INSERT INTO shoes (brand,model,release_date,price) VALUES(?,?,?),(brand, model, release, price)")
    conn.commit()
    for row in c.execute('SELECT * FROM shoes ORDER BY price'):
        print(row)


# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.

for row in c.execute('SELECT * FROM shoes ORDER BY price'):
    print(row)

Steven_inserts()
conn.close()









conn.close()



