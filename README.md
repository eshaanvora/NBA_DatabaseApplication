## NBA Database Application

This repo contains programs to implement a NBA statistics application including programs to create & setup database schema configured on mySQL server

The file 'DataUploader.py' creates the Database, including setting relational schema and populating data while the file 'app.py' is the actual driver program for the NBA application.

## Identifying Information

* Name: Eshaan Vora
* Email: EshaanVora@gmail.com

## Source Files

* DataUploader.py
* TableSetup.sql
* UploadHelper.py
* app.py
* ER_Diagram.pdf
* /CLEANDATA_CSV/player.csv
* /CLEANDATA_CSV/team.csv
* /CLEANDATA_CSV/draft.csv
* /CLEANDATA_CSV/game.csv
* /CLEANDATA_CSV/mvp.csv
* QueryResults.csv

## Program Functionality:

*                Add new player records
*                Delete player records
*                Modify player records
*                Save results to .CSV file
*                Generate statistics about MVP players
*                Generate statistics about drafts and draft picks
*                Generate statistics about games won including owner and team managers 
*                Filter results by current NBA players
*                Openly query via your mySQL IDE using database setup files
*                'DataUploader.py' will create the 'NBA_DB' database, setup tables, and populate the database for use by 'app.py'
*                This program also handles improper input into query injection fields and exits gracefully
*                Terminal/Python command line is front end and back end is Python and SQL with MySQL Server

## Execution Instructions 

Modify database connection credentials in 'DataUploader.py' and 'app.py' to your mySQL server connection

Run: python3 DataUploader.py
Run: python3 app.py

## Dataset

* Modified & cleaned from: https://www.kaggle.com/datasets/wyattowalsh/basketball
