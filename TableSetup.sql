CREATE DATABASE IF NOT EXISTS NBA_DB;

USE NBA_DB;

CREATE TABLE player(
id VARCHAR(7) NOT NULL PRIMARY KEY,
full_name VARCHAR(50),
first_name VARCHAR(50),
last_name VARCHAR(50),
is_active BOOLEAN,
team_id VARCHAR(20),
birthdate VARCHAR(12),
country VARCHAR(30),
height VARCHAR(3),
weight INT,
position VARCHAR(20),
team_name VARCHAR(50),
from_year INT,
to_year	INT,
points	FLOAT,
assists	FLOAT,
rebounds FLOAT,
all_star_appearances INT,
INDEX(id)
);

CREATE TABLE team(
id VARCHAR(10) NOT NULL PRIMARY KEY,
full_name VARCHAR(50),
abbreviationName VARCHAR(3),
nickname VARCHAR(50),
city VARCHAR(50),
state VARCHAR(50),
year_founded YEAR,
owner_name VARCHAR(50),
headcoach_name VARCHAR(50),
generalmanager_name VARCHAR(50)
);

CREATE TABLE mvp(
championYear INT,
playerID VARCHAR(7) NOT NULL,
playerName VARCHAR(50),
playerPosition VARCHAR(2),
teamID VARCHAR(10) NOT NULL,
teamName VARCHAR(50),
FOREIGN KEY (playerID) REFERENCES player(id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE game (
game_ID VARCHAR(10),
seasonID VARCHAR(7),
team_ID_home VARCHAR(10),
team_name_home VARCHAR(50),
game_date VARCHAR(8),
matchup_home VARCHAR(12),
win_home BOOLEAN,
fgm_home INT,
points_home INT,
plus_points_home VARCHAR(4),
team_ID_away VARCHAR(10),
team_name_away VARCHAR(50),
season_year YEAR,
hometeam_wins INT,
hometeam_losses INT,
series_leader VARCHAR(50)
);

CREATE TABLE draft(
year_draft YEAR,
number_picked_overall INT(5),
number_round INT(5),
number_round_pick INT(5),
player_name VARCHAR(50),
team_abbreviation VARCHAR(4),
previous_organization_name VARCHAR(100),
previous_organization_type VARCHAR(50),
playerID VARCHAR(7),
team_ID VARCHAR(10),
team_full_name VARCHAR(50),
previous_organization_level VARCHAR(3)
);

CREATE VIEW player_active AS
SELECT *
FROM player
WHERE is_active;

CREATE VIEW draft_active AS
SELECT *
FROM draft
WHERE playerID IN (
	SELECT id
    FROM player_active);

CREATE VIEW mvp_active AS
SELECT *
FROM mvp
WHERE playerID IN (
	SELECT id
    FROM player_active);