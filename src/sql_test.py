import sqlite3

from numpy import insert

def create_table():
    #connect to database
    conn = sqlite3.connect('customer.db')

    #create cursor
    c = conn.cursor()

    #create table
    c.execute("""CREATE TABLE customers (
            first_name text,
            last_name text,
            email text
        )""")

    #commit our command to the database
    conn.commit()

    #close connection
    conn.close()



def insertRow():
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES ('Tim', 'Doe', 'tim@doe.com')")
    conn.commit()
    print("Row added...")
    conn.close()


def insert_multiple_rows():
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    many_customer = [
        ('John', 'Doe', 'jd@doe.com'),
        ('Jane', 'Doe', 'jad@doe.com'),
        ('John', 'Smith', 'js@doe.com'),
    ]
    c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customer)
    conn.commit()
    print("Multiple rows added...")
    conn.close()

def queryDatabase():
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM customers")
    for row in c.fetchall():
        print(row)
    conn.close()

def filterDatabase():
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM customers WHERE last_name = 'Doe'")
    items = c.fetchall()
    for item in items:
        print(item)


def updateDatabase():
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("UPDATE customers SET last_name = 'Doe' WHERE first_name = 'Jane'")
    conn.commit()
    conn.close()

