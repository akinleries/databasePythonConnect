#Connect to mysql database using python and retrieve some data

#import the needed packages

import mysql.connector
from mysql.connector import Error

#define the connector function

def Connect_insert():
    '''function to connect and fetch rows in a database'''

    #create a variable for the connect object

    conn = None

    try:
        conn = mysql.connector.connect(host = 'localhost', database = 'movie_review', user = 'root', password = 'lasisi')
        print('Connecting to database server')
        if conn.is_connected:
           print('connected to database server')
           db_cursor = conn.cursor()

           #create a variable to contain the sql query to be executed
           sql = "insert into Human (HumanId, name, color, Gender, BloodGroup) Values (%s, %s, %s, %s, %s)"

           #create a list variable to contain all the values we want to insert into the table

           val = []

           for countUserInput in range(3):
                movies_id = input("your id number  : ")
                title = input("enter movie title pls  : ")
                release_year = input("movie  : ")
                genres = input("enter genres : ")
                colection_in_mil = input( "enter collection_in_mil  : ")
                val.append((movies_id, title, release_year, genres, colection_in_mil))
           #execute the query using the execute many function
           db_cursor.executemany(sql, val)

           #commit to the database
           conn.commit()

           #print a success message
           print(db_cursor.rowcount, "row was inserted")

           #close the cursor
           db_cursor.close

    except Error as e:
        print('connection failed due to the following', e)
    finally:
        if conn is not None and conn.is_connected:
           conn.close
           print('Disconected from the database')


Connect_insert()

