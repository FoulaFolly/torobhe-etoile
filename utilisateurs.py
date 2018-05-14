import psycopg2
from config import config

def ajouter_utilisateur(nom, addresse, email, mot_de_passe, telephone):
	  #insert element in the table 
    sql = "INSERT INTO Utilisateurs(nom, addresse, email, mot_de_passe, telephone) VALUES(%s,%s,%s,%s,%s)"
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql,(nom,addresse,email,mot_de_passe,telephone))
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

def rechercher_utilisateur(telephone):
	sql = "SELECT * FROM Utilisateurs WHERE telephone = %s" # WHERE telephone = tel
	conn = None
	try:
        # read database configuration
		params = config()
        # connect to the PostgreSQL database
		conn = psycopg2.connect(**params)
        # create a new cursor
		cur = conn.cursor()
        # execute the SELECT statement
		cur.execute(sql,(telephone,))
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

def supprimer_utilisateur(telephone):
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
	    cur.execute("DELETE FROM Utilisateurs WHERE telephone = %s", (telephone,))
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
    numberTel=int(input("give the user's number: "))
    rechercher_utilisateur(numberTel)
    # supprimer_utilisateur(numberTel)    
    # ajouter_utilisateur("Pathe", "188L", "pathe@lll.com", "mot_de_passe", 3324);
    
