#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
# Code base form Udacity
# Implementation by Oren Tayar - March 2017

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    conn = psycopg2.connect("dbname=tournament")
    curs = conn.cursor()
    return (conn, curs)
    # comment - if your database requires a user and password use the following line instead
    # psycopg2.connect("dbname=tournament user=user_name password=your_password")


# deletes all the match results in the table
def deleteMatches():
    """Remove all the match records from the database."""
    conn,curs = connect()
    curs.execute("DELETE FROM matches;")
    conn.commit()
    curs.close()
    conn.close()
    
# deletes all the registered players
def deletePlayers():
    """Remove all the player records from the database."""
    conn,curs = connect()
    curs.execute("DELETE FROM players;")
    conn.commit()
    curs.close()
    conn.close()

# counts the number of players
def countPlayers():
    """Returns the number of players currently registered."""
    conn,curs = connect()
    curs.execute("select count(*) from players;")
    rows = curs.fetchall()
    n = rows[0][0]
    curs.close()
    conn.close()
    return n

# registers a new user
def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    conn,curs = connect()
    curs.execute("insert into players (name) values (%s)", [name])
    conn.commit()
    curs.close()
    conn.close()

# returns a table of all players with their wins and total played matches
def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn,curs = connect()
    curs.execute("select * from standings")
    rows = curs.fetchall()
    curs.close()
    conn.close()
    return rows 
    
# enables to report a match with its winner
def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn,curs = connect()
    curs.execute("insert into matches (winner,loser) values (%d, %d)" % (winner,loser))
    conn.commit()
    curs.close()
    conn.close()    
    
# returns the set of next games by pairs of players
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    conn,curs = connect()
    curs.execute("select * from pairs")
    rows = curs.fetchall()
    curs.close()
    conn.close()
    return rows


