#!/usr/local/lib/python3
import psycopg2

conn = psycopg2.connect(database="postgres", user="postgres", password="user", host="localhost", port="5432")
print("\nOpened database successfully")

#fonction create table
def TabUsers():
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS Users(
     id INT PRIMARY KEY NOT NULL,
     nom TEXT NOT NULL,
     adress text,
     numTel text);
     """)
    print("Table created successfully")
    conn.commit()

#insertion d'element
def inserTab():
    
   cur = conn.cursor()
   cur.execute("INSERT INTO Users (id,nom,adress,numTel) \
     VALUES (1,'Pathé LY', 'Saint-Louis', '+221777814577')");
   cur.execute("INSERT INTO Users (id,nom,adress,numTel) \
     VALUES (2,'Sadou LY', 'Sonfonia', '+224622287853')");
   conn.commit()
   print("Records created successfully")

#ajout d'une colonne
def modifColumn():
    cur = conn.cursor()
    cur.execute("ALTER TABLE Users ADD email text")
    cur.execute("ALTER TABLE Users ADD motPass text")
   # cur.execute("ALTER TABLE article ADD DateDachat date")
   # cur.execute("ALTER TABLE Users ALTER COLUMN numTel TYPE text")
   # cur.execute("UPDATE Users set numTel =+221777814577 where id=1")
    conn.commit()
    print("alter done successfully")


if __name__=='__main__': 
     
     TabUsers()
     #inserTab()
     modifColumn()  
     conn.close()
