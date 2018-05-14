#!/usr/bin/python 
#https://w3resource.com/PostgreSQL/postgresql-subqueries.php
import psycopg2
from config import config

def sql_creer_table_articles():
     return """CREATE TABLE IF NOT EXISTS Articles (
     id SERIAL PRIMARY KEY,
     nom VARCHAR(255) NOT NULL,
     description VARCHAR,
     prix REAL
     )
     """

def sql_creer_table_clients():
    return """ CREATE TABLE IF NOT EXISTS Clients(
                id SERIAL PRIMARY KEY,
                nom VARCHAR NOT NULL,
                addresse VARCHAR(255) NOT NULL,
                telephone INT NOT NULL,
                email VARCHAR
          )
        """

def sql_creer_table_vendeurs():
    return """
        CREATE TABLE IF NOT EXISTS Vendeurs (
                id SERIAL PRIMARY KEY,
                nom VARCHAR NOT NULL,
                addresse VARCHAR(255) NOT NULL,
                telephone INT NOT NULL,
                email VARCHAR
        )
        """

def sql_creer_table_utilisateurs():
    return """
        CREATE TABLE IF NOT EXISTS Utilisateurs(
     id SERIAL PRIMARY KEY,
     nom VARCHAR NOT NULL,
     addresse VARCHAR(255),
     email VARCHAR NOT NULL,
     mot_de_passe text NOT NULL,
     telephone INT )"""

def creer_tables():
    """ create tables in the PostgreSQL database"""

    # Articles
    commands = (
     sql_creer_table_articles(),
     sql_creer_table_clients(),
     sql_creer_table_vendeurs(),
     sql_creer_table_utilisateurs())
        
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # commit the changes
        conn.commit()
        # close communication with the PostgreSQL database server
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    print("TABS CREATION DONE SUCCESFULLY")        
 
def supprimer_table(table):
    sql = " DROP TABLE {}".format(table)
    
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        cur.execute(sql)
        # commit the changes
        conn.commit()
        # close communication with the PostgreSQL database server
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    print("TABLE DROP DONE SUCCESFULLY")    

def afficher_table(table):
    sql = "SELECT * FROM {}".format(table)
    
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        cur.execute(sql)
        vendeurs = cur.fetchall()
        for vendeur in vendeurs:
            print(vendeur)

        # close communication with the PostgreSQL database server
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def afficher_base_de_donnees():
    pass

 
if __name__ == '__main__':
    # supprimer_table("Utilisateurs")
    # creer_tables()
    afficher_table("Articles")
    # afficher_base_de_donnees()
    #pass
