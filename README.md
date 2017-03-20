# Tournament Results Backend

This repository implements a backend to store players and matches scores. It is designed to implement a swiss pairing mechanism to decide the pairs of players for the next match. The concept is that winners are paired with winners with the same (more or less) previous wins and this is maintained for all players. so all players in a tournament play the same number of matches.

#### *Technology and general architecture*
- Backend code implemented in Python (2.7) 
- Database is implemented using PostgreSQL
- Python is using the psycopg2 library as API to the DB
 
#### *Files in the repository*
- tournament.py - implements the Python code of the project
- tournament_test.py - implements a testing code (runs the tournament.py file)
- tournament.sql - implements SQL code to build the tournament db, it's tables and views.

#### *special instructions*
- install and setup postgresql on your machine plus python 2.7
- install the psycopg2 library by typing pip install psycopg2
- clone the repository to your local machine
- in order to create the db of the tournament enter the postgresql command line from the tournament folder (typing psql)
- then type into the psql command line:
'$ \i tournament.sql'. 
This should run all the SQL commands from the file as a script.

####
in order to test the tournament backend you can use the included test file.
type:
'$ python tournament_test.py'

you should get a list of test results printed onto the screen with a success message at the end.

