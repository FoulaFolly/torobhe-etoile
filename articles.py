import psycopg2
from config import config

def ajouter_article(nom, description, prix):
	 #insert element in the table 
    sql = "INSERT INTO Articles(nom, description, prix) VALUES(%s,%s,%s)"
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql,(nom,description, prix))
        # commit the changes to the database
        conn.commit()
        # closee communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    print('\nOperation done well')

def rechercher_article(nom):
    	
	sql = "SELECT * FROM Articles WHERE nom = %s" # WHERE telephone = tel
	conn = None
	try:
	    # read database configuration
	    params = config()
        # connect to the PostgreSQL database
	    conn = psycopg2.connect(**params)
        # create a new cursor
	    cur = conn.cursor()
        # execute the SELECT statement
	    cur.execute(sql,(nom,))
	    vendeur = cur.fetchall()
	    print(vendeur)
        # commit the changes to the database
	    conn.commit()
        # close communication with the database
	    cur.close()
	except (Exception, psycopg2.DatabaseError) as error:
	    print(error)
	finally:
	    if conn is not None:
	        conn.close()
	print('\nOperation done well')    
        

def supprimer_article(nom):
	""" delete part by part name """
	conn = None
	rows_deleted = 0
	try:
	    # read database configuration
	    params = config()
	    # connect to the PostgreSQL database
	    conn = psycopg2.connect(**params)
	    # create a new cursor
	    cur = conn.cursor()
	    # execute the UPDATE  statement
	    cur.execute("DELETE FROM Articles WHERE nom = %s", (nom,))
	    # get the number of updated rows
	    rows_deleted = cur.rowcount
	    # Commit the changes to the database
	    conn.commit()
	    # Close communication with the PostgreSQL database
	    cur.close()
	except (Exception, psycopg2.DatabaseError) as error:
	    print(error)
	finally:
	    if conn is not None:
	        conn.close()
	#return the number of update row        
	return rows_deleted 

if __name__ == '__main__':
	supp=input("donnez le nom de l'article à supprimer")
	deleted_rows = supprimer_article(supp)
	print('The number of deleted rows: ', deleted_rows)    