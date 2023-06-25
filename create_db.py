import sqlite3
def Create_db():
    con=sqlite3.connect(database=r'sms.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS register(eid INTEGER PRIMARY KEY AUTOINCREMENT,cust_Id NUMERIC,f_name text,shop_name text,contact text,email text,question text,answer text,password text,license text,govid text,Idno text,Address text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS employee(cid INTEGER PRIMARY KEY AUTOINCREMENT,Name text,contact text,email text,govid text,Idno text,Address text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT,name text,contact text,desc text,status text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS category(Cid INTEGER PRIMARY KEY AUTOINCREMENT,name text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS product(pid INTEGER PRIMARY KEY AUTOINCREMENT,Category text,name text,price text,qty NUMERIC,status text,dealer_name text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS dealer(did INTEGER PRIMARY KEY AUTOINCREMENT,agency text,name text,contact text,gov_id text,id_no text,email text,password text,address text)")
    con.commit()

Create_db()