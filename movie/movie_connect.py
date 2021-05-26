#Connect to mysql database using python and retrieve some data

#import the needed packages

import mysql.connector
from mysql.connector import Error

#define the connector function

def Connect_fetch():
    '''function to connect and fetch rows in a database'''

    #create a variable for the connect object

    conn = None

    try:
        conn = mysql.connector.connect(host = 'localhost', database = 'movie_review', user = 'root', password = 'lasisi')
        print('Connecting to database server')
        if conn.is_connected:
            print('connected to database server')

         #select Query
        sql_select_query = "select * from movies"
        cursor = conn.cursor()
        cursor.execute(sql_select_query)
        records = cursor.fetchall()
        print('total number of rows in movies is: ',  cursor.rowcount)

       #Display the output data
        print("\nPrinting each buyer record")
        for row in records:
            print("movies_id: ", row[0])
            print("title", row[1])
            print("release_year", row[2])
            print("genres", row[3])
            print("colection_in_mil", row[4], '\n')

    except Error as e:
              print('not connecting due to : ', e)

    finally:
        if conn is not None and conn.is_connected():
              conn.close()
              print('database shutdown')


Connect_fetch()
