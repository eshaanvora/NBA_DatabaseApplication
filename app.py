#Eshaan Vora
#EshaanVora@gmail.com

import os.path
import sys
import csv

#Import mySQL connector for database connection
import mysql.connector
from mysql.connector import errorcode

def pretty_print(lst):
    print("Results:")
    for i in lst:
        print(i)
    print("")

def get_choice(lst):
    choice = input("Enter choice number: ")
    while choice.isdigit() == False:
        print("Incorrect option. Try again")
        choice = input("Enter choice number: ")
    while int(choice) not in lst:
        print("Incorrect option. Try again")
        choice = input("Enter choice number: ")
    return int(choice)

def write_csv_prompt(results):
    choice = input("Save results to CSV? (y/n) ")
    while choice.isdigit() == True:
        print("Incorrect option. Try again")
        choice = input("Enter choice number: ")
    if choice[0].upper() == "Y":
        with open("QueryResults.csv", 'w') as csvfile:
            writeFile = csv.writer(csvfile)
            writeFile.writerows(results)
            csvfile.close()

def options():
    print("Select from the following menu options:"+
    "\n1 View Draft Year and Draft Number of NBA MVPs \n2 Top 10 overall draft picks per team"+
    "\n3 View historical homegame wins per franchise \n4 View count of positions played by MVPs\n5 View Active Players \n6 View most sucessful team owners and headcoaches"+
    "\n7 Add new player \n8 Delete a player \n9 Update Player Records \n10 Total home wins for a given player \n11 View average draft pick per team (Lower draft average is advantageous)\n12 Exit")

    user_choice = get_choice([1,2,3,4,5,6,7,8,9,10,11,12])
    return(user_choice)

def Queries(user_choice):
    if user_choice == 1:
        query = "SELECT championYear, player_name, year_draft, number_picked_overall FROM mvp JOIN draft on mvp.playerID = draft.playerID"
        printQuery(query)
    elif user_choice == 2:
        current_player_prompt = input("Would you like to view results for only active players ? ")
        team_choice = "'" + input("Input team abbreviation (Ex: Los Angeles Lakers = LAL):") + "'"
        if current_player_prompt[0].upper() == "Y":
            query = "SELECT player_name, number_picked_overall FROM draft_active WHERE number_picked_overall < 10 AND team_abbreviation = " +team_choice
        else:
            query = "SELECT player_name, number_picked_overall FROM draft WHERE number_picked_overall < 10 AND team_abbreviation = " +team_choice
        dbCursor.execute(query,team_choice)
        results = dbCursor.fetchall()
        pretty_print(results)
        write_csv_prompt(results)
    elif user_choice == 3:
        query = "SELECT full_name, COUNT(win_home) as home_wins FROM team JOIN game on team.id = game.team_id_home WHERE game.win_home LIKE '1' GROUP BY team.id, team.full_name ORDER BY home_wins DESC"
        #or game.Win_AWAY LIKE '1' "
        printQuery(query)
    elif user_choice == 4:
        query = "SELECT playerPosition, COUNT(playerPosition) FROM mvp GROUP BY playerPosition"
        printQuery(query)
    elif user_choice == 5:
        query = "SELECT player_name, team_full_name FROM draft_active ORDER BY team_full_name ASC"
        dbCursor.execute(query)
        results = dbCursor.fetchall()
        pretty_print(results)
        write_csv_prompt(results)
    elif user_choice == 6:
        query = "SELECT t.headcoach_name, t.generalmanager_name, COUNT(win_home) homeWin FROM game g INNER JOIN team t ON g.team_ID_home = t.id GROUP BY t.headcoach_name, t.generalmanager_name"
        print("TeamOwner, HeadCoach, NumberOfWins")
        printQuery(query)
    elif user_choice == 7:
        id = input("What is their id: (Ex: Up to max 7 values '1000001' or '12823'):")
        first_name = input("What is their FIRST name: ") + " "
        last_name = input("What is their LAST name: ")
        full_name = first_name + last_name
        is_active = input("Is this player active (1 for yes, 0 for no):")
        values = (id,full_name,first_name,last_name,is_active)
        query = "INSERT INTO player VALUES(%s, %s, %s, %s, %s)"
        dbCursor.execute(query,values)
        NBA_DB_Connection.commit();
    elif user_choice == 8:
        full_name = "'" + input("What is the name of the player you want to delete: ") + "'"
        try:
            query = "DELETE FROM player WHERE full_name = " + full_name
            dbCursor.execute(query,full_name)
            NBA_DB_Connection.commit();
            print("Deleted record sucessfully \n")
        except:
            print("Oops that didn't work. Please try again. \n")

        #Add option to trade players from one team to another
        #For future commit

    elif user_choice == 9:
        full_name = "'" + input ("What is the name of the player you want to update?: ") + "'"
        print("What attribute you like to change from the following attributes?")
        query = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'player'"
        dbCursor.execute(query)
        results = dbCursor.fetchall()
        print(results)
        variable_change = input()
        value_change = input("What would you like you change this value to? ")
        try:
            query = "UPDATE player SET " + variable_change + " = " + value_change + " WHERE full_name = " + full_name
            dbCursor.execute(query)
            NBA_DB_Connection.commit()
            print("Record sucessfully updated")
        except:
            print("Oops, that didn't work. Try again.")

    elif user_choice == 10:
        player_choice = "'" + input("What is the full name of the player? ") + "'"
        query = "SELECT p.full_name, COUNT(win_home) TotalWins FROM game g  INNER JOIN draft d ON g.team_ID_home = d.team_ID INNER JOIN player p ON d.playerID = p.id WHERE p.full_name = " +player_choice+ " GROUP BY p.full_name"
        printQuery(query)
    elif user_choice == 11:
        query = "SELECT team_full_name, AVG(number_round_pick) as avgPick FROM draft GROUP BY team_full_name ORDER BY avgPick"
        printQuery(query)
    elif user_choice == 12:
        exit()

def printQuery(query):
    dbCursor.execute(query)
    results = dbCursor.fetchall()
    pretty_print(results)

try:
   NBA_DB_Connection = mysql.connector.connect(
   user='root',
   password='Password',
   #Public IP address: '35.192.72.137' Port: 3306
   host='localhost',
   database='NBA_DB')

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

#######MAIN##############
while True:
    user_choice = options()
    Queries(user_choice)
