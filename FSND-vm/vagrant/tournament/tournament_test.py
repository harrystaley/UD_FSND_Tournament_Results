''' This python file tests the tournament database for Project 2 of the \
full stack web development nanodegree '''

# !/usr/bin/env python
#
# Test cases for tournament.py

import tournament


def test_delete_matches():
    '''This function tests to see if matches can be deleted'''
    tournament.delete_matches()
    print "1. Old matches can be deleted."


def test_delete():
    '''This function tests if player records can be deleted.'''
    tournament.delete_matches()
    tournament.delete_players()
    print "2. Player records can be deleted."


def test_count():
    '''This function tests if the the counts return properly
    from the database.'''
    tournament.delete_matches()
    tournament.delete_players()
    c_value = tournament.count_players()
    if c_value == '0':
        raise TypeError(
            "count_players() should return numeric zero, not string '0'.")
    if c_value != 0:
        raise ValueError("After deleting, count_Players should return zero.")
    print "3. After deleting, count_players() returns zero."


def test_register():
    '''this funciton tests if the player registration works correctly by
    returning the proper number of players registered.'''
    tournament.delete_matches()
    tournament.delete_players()
    tournament.register_player("Chandra Nalaar")
    c_value = tournament.count_players()
    if c_value != 1:
        raise ValueError(
            "After one player registers, count_players() should be 1.")
    print "4. After registering a player, count_players() returns 1."


def test_register_count_delete():
    '''This function tests to see if players can be registered and deleted.'''
    tournament.delete_matches()
    tournament.delete_players()
    tournament.register_player("Markov Chaney")
    tournament.register_player("Joe Malik")
    tournament.register_player("Mao Tsu-hsi")
    tournament.register_player("Atlanta Hope")
    c_value = tournament.count_players()
    if c_value != 4:
        raise ValueError(
            "After registering four players, count_players should be 4.")
    tournament.delete_players()
    c_value = tournament.count_players()
    if c_value != 0:
        raise ValueError("After deleting, count_players should return zero.")
    print "5. Players can be registered and deleted."


def test_standings_before_matches():
    '''This function tests if newly registred players appear in the
    standings without any matches'''
    tournament.delete_matches()
    tournament.delete_players()
    tournament.register_player("Melpomene Murray")
    tournament.register_player("Randy Schwartz")
    standings = tournament.player_standings()
    if len(standings) < 2:
        raise ValueError("Players should appear in player_standings even "
                         "before they have played any matches.")
    elif len(standings) > 2:
        raise ValueError("Only registered players should appear in standings.")
    if len(standings[0]) != 4:
        raise ValueError("Each player_standings row should have four columns.")
    [(id1, name1, wins1, matches1), (id2, name2, wins2, matches2)] = standings
    if matches1 != 0 or matches2 != 0 or wins1 != 0 or wins2 != 0:
        raise ValueError(
            "Newly registered players should have no matches or wins.")
    if set([name1, name2]) != set(["Melpomene Murray", "Randy Schwartz"]):
        raise ValueError("Registered players' names should appear in "
                         "standings, even if they have no matches played.")
    print "6. Newly registered players appear in the standings "\
          "with no matches."


def test_report_matches():
    '''This function tests to see if after a match the players' standing
    have been updated.'''
    tournament.delete_matches()
    tournament.delete_players()
    tournament.register_player("Bruno Walton")
    tournament.register_player("Boots O'Neal")
    tournament.register_player("Cathy Burton")
    tournament.register_player("Diane Grant")
    standings = tournament.player_standings()
    [id1, id2, id3, id4] = [row[0] for row in standings]
    tournament.report_match(id1, id2)
    tournament.report_match(id3, id4)
    standings = tournament.player_standings()
    for (i, n, w, m) in standings:
        if m != 1:
            raise ValueError("Each player should have one match recorded.")
        if i in (id1, id3) and w != 1:
            raise ValueError("Each match winner should have one win recorded.")
        elif i in (id2, id4) and w != 0:
            raise ValueError("Each match loser should have zero wins "
                             "recorded.")
    print "7. After a match, players have updated standings."


def test_pairings():
    '''This tests to see if match pairings work properly.'''
    tournament.delete_matches()
    tournament.delete_players()
    tournament.register_player("Twilight Sparkle")
    tournament.register_player("Fluttershy")
    tournament.register_player("Applejack")
    tournament.register_player("Pinkie Pie")
    standings = tournament.player_standings()
    [id1, id2, id3, id4] = [row[0] for row in standings]
    tournament.report_match(id1, id2)
    tournament.report_match(id3, id4)
    pairings = tournament.swiss_pairings()
    if len(pairings) != 2:
        raise ValueError(
            "For four players, swiss_Pairings should return two pairs.")
    [(pid1, pname1, pid2, pname2), (pid3, pname3, pid4, pname4)] = pairings
    correct_pairs = set([frozenset([id1, id3]), frozenset([id2, id4])])
    actual_pairs = set([frozenset([pid1, pid2]), frozenset([pid3, pid4])])
    if correct_pairs != actual_pairs:
        raise ValueError(
            "After one match, players with one win should be paired.")
    print "8. After one match, players with one win are paired."


if __name__ == '__main__':
    test_delete_matches()
    test_delete()
    test_count()
    test_register()
    test_register_count_delete()
    test_standings_before_matches()
    test_report_matches()
    test_pairings()
    print "Success!  All tests pass!"
