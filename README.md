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
