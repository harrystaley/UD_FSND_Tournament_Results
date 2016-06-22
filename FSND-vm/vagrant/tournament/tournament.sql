-- Table definitions for the tournament project.

-- TODO: add a bye system so that odd numbers of players can enter
-- TODO: add other tables to store player match records and numerous tournaments.

-- delete the DB if it exists
DROP DATABASE IF EXISTS tournament;
-- Create the tournament database
CREATE DATABASE tournament;
-- connect to the cournament database
\c tournament

-- create players table
CREATE TABLE players(
    player_id SERIAL PRIMARY KEY,
    player_name TEXT NOT NULL
);

-- create matches table
CREATE TABLE matches(
    match_id SERIAL PRIMARY KEY,
    winner INT REFERENCES players (player_id),
    loser INT REFERENCES players (player_id)
);

-- count regitered players view
CREATE OR REPLACE VIEW count_players AS
    SELECT COUNT(*) AS reg_players
    FROM players;

-- create the view for player standings
CREATE OR REPLACE VIEW current_standings AS
    SELECT  player_id,
            player_name,
            SUM(CASE WHEN players.player_id = matches.winner THEN 1 ELSE 0 END) AS wins,
            COUNT(matches) AS match_count
    FROM players
    LEFT OUTER JOIN matches
    ON players.player_id = matches.winner OR players.player_id = matches.loser
    GROUP BY player_id
    ORDER BY wins DESC,
             match_count ASC;

-- create a view to randomly seed the matches before the first round.
CREATE OR REPLACE VIEW seed_initial_round AS
    SELECT *
    FROM  players
    ORDER BY random();