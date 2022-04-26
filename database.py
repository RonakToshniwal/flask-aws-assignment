##database instruction file


import psycopg2



def insert(name,location,date):
    print(name,location,date) 
    con =psycopg2.connect(database="Ecom", user = "ronak", password = "Ronak123", host = "ecom2.crikfx69daff.ap-south-1.rds.amazonaws.com", port = "5432")

    cur=con.cursor()
    cur.execute(f"INSERT INTO students (name,location,date) values ('{name}','{location}','{date}');")
    con.commit()
    con.close()

def show():
    con =psycopg2.connect(database="Ecom", user = "ronak", password = "Ronak123", host = "ecom2.crikfx69daff.ap-south-1.rds.amazonaws.com", port = "5432")
    cur=con.cursor()
    cur.execute("SELECT * FROM students")
    rows=cur.fetchall()
    con.commit()
    con.close()
    return rows




