'''This houses the python functions used to work the database.'''
# !/usr/bin/env python
# tournament.py -- implementation of a Swiss-system tournament
#
# TODO: add a bye system to all ow odd numbers of players to enter
# TODO: add a front ent user interface for the tournament database

import psycopg2
import bleach


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def delete_matches():
    """Remove all the match records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM matches")
    DB.commit()
    DB.close()

def delete_players():
    """Remove all the player records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM players")
    DB.commit()
    DB.close()


def count_players():
    """Returns the number of players currently registered."""
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT * FROM count_players")
    DB.commit()
    player_count = c.fetchall()[0][0]
    DB.close()
    return player_count


def is_even(i):
    """ Returns a boolean falue telling if the value is even """
    return (i % 2) == 0


def register_player(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
      WARNING: some names may be modified in order to protect the database.
    """

    """ use bleach to clean the name of the registered user """
    clean_name = bleach.clean(name, strip=True)
    DB = connect()
    c = DB.cursor()
    c.execute("INSERT INTO players (player_name) VALUES (%s)", (clean_name,))
    DB.commit()
    DB.close()


def player_standings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        player_id: the player's unique id (assigned by the database)
        player_name: the player's full name (as registered)
        wins: the number of matches the player has won
        match_count: the number of matches the player has played
    """
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT * FROM current_standings")
    DB.commit()
    standings = c.fetchall()
    DB.close()
    return standings


def report_match(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """

    DB = connect()
    c = DB.cursor()
    c.execute("INSERT INTO matches (winner, loser) VALUES (%s,%s);", (winner, loser))
    DB.commit()
    DB.close()

def swiss_pairings():
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

    DB = connect()
    c = DB.cursor()
    match_count = c.execute("SELECT COUNT(*) FROM matches")
    c.execute("SELECT player_id, player_name FROM current_standings")
    standings = c.fetchall()
    DB.commit
    c.execute("SELECT player_id, player_name FROM seed_initial_round")
    seed = c.fetchall()
    DB.commit()

    """ Get player_count from count_players function """
    player_count = count_players()
    """ determine if playercount is an even number """
    if is_even(player_count) == True:
        pairings = []

        """ randomly seed matches if no matches have been played. """
        if match_count == 0:
            for x in range(0, player_count-1, 2):
                pairings.append(seed[x] + seed[x+1])
        else:
            for x in range(0, player_count-1, 2):
                pairings.append(standings[x] + standings[x+1])

    else: raise ValueError("The tournament requires and even number of players. \
                            Please add or remove a single player.")
    """ close the DB and return the match pairings """
    DB.close()
    return pairings

