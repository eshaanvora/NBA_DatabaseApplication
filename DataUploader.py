#Eshaan Vora
#EshaanVora@gmail.com

import os.path

#Import mySQL connector for database connection
import mysql.connector
from mysql.connector import errorcode

#Import helper functions to clean data
from UploadHelper import helper

#Locate CSV file on local computer
fileNames = ["team","player","mvp","game","draft"]

#Define function to run SQL queries from a '.sql' file
def executeQueriesFromFile(filename):
    # Open and read the file as a single buffer
    fd = open(filename, 'r')
    sqlFile = fd.read()
    fd.close()

    #Retrieve all SQL commands (SQL commands are split on ';')
    sqlCommands = sqlFile.split(';')
    # Execute every command from the input file
    for command in sqlCommands:
        try:
            dbCursor.execute(command)
            NBA_DB_Connection.commit()
        except:
            print("Database and Tables have already been setup")
            return

    print("'NBA_DB' Database and all Tables have sucessfully been created in MySQLServer ")

#Define function to load cleaned data into database tables
def bulk_load(data,insertTable):
    #Count number of attributes to generate placeholders for
    attribute_count = len(data[0])
    #Remove last comma from placeholder string to fix syntax
    placeholders = ("%s,"*attribute_count)[:-1]

    #Query with placeholders and parameter for column name
    query = "INSERT INTO " +insertTable+ " VALUES("+placeholders+")"
    dbCursor.executemany(query,data)
    NBA_DB_Connection.commit()
    print("QUERY EXECUTED: " + query)

#Establish connection to Google Cloud Platform
#If error occurs, check error type, then exit program
try:
   NBA_DB_Connection = mysql.connector.connect(
   user='root',
   password='Password',
   #Public IP address: '35.192.72.137' Port: 3306
   host='localhost')
   #Create cursor for NBA_DB database connection
   dbCursor = NBA_DB_Connection.cursor()
   print("Connection successful")

except mysql.connector.Error as err:
   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print('Invalid credentials')
      exit()
   elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print('Database not found')
      exit()
   else:
      print('Cannot connect to database:', err)
      exit()

############## MAIN ##########################################################################

executeQueriesFromFile('TableSetup.sql')

#Upload all data into database from the project's 'CLEANDATA_CSV' folder
for i in fileNames:
    filePath = "CLEANDATA_CSV/" + i + ".csv"
    data = helper.data_cleaner(filePath)
    try:
        bulk_load(data,i)
    except:
        print("Data has already been uploaded to SQL Server. Exiting program.")
        NBA_DB_Connection.close()
        exit()

NBA_DB_Connection.close()
