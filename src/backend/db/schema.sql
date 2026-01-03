--(1) Create the database schema
	CREATE SCHEMA IF NOT EXISTS FootballDB;
	
--(2) Created the STADIUM table
	CREATE TABLE Stadium (
		stadiumId INT AUTO_INCREMENT PRIMARY KEY,
		stadiumName VARCHAR(30) NOT NULL,
		city VARCHAR(20) NOT NULL,
		state VARCHAR(2) NOT NULL,
		capacity INT 
	);
	
--(3) Created the TEAM table
-- 	CREATE TABLE Team (
-- 		teamId INT AUTO_INCREMENT PRIMARY KEY,
-- 		teamName VARCHAR(100) NOT NULL,
-- 		stadiumId INT NOT NULL,
-- 		city VARCHAR(20) NOT NULL,
-- 		state VARCHAR(2),
-- 		logoPath VARCHAR(255) NOT NULL,
-- 		FOREIGN KEY (stadiumId) REFERENCES Stadium(stadiumId)
-- 	);


	
--(4) Created the COACH table

-- 	CREATE TABLE Coach (
-- 		coachId INT AUTO_INCREMENT PRIMARY KEY,
-- 		fName VARCHAR(50) NOT NULL,
-- 		lName VARCHAR(50) NOT NULL,
-- 		teamId INT NOT NULL,
-- 		FOREIGN KEY (teamId) REFERENCES Team(teamId)
-- 	);

    CREATE TABLE Coach (
        coach_id SERIAL PRIMARY KEY,
        coach_name VARCHAR NOT NULL,
        team_id INT NOT NULL,
        FOREIGN KEY (team_id) REFERENCES Team(team_id)
    );

    CREATE TABLE Coach_Team_Season (
        coach_team_season_id SERIAL PRIMARY KEY,
        coach_id INT NOT NULL REFERENCES coach(coach_id),
        team_id INT NOT NULL REFERENCES team(team_id),
        season_id INT NOT NULL REFERENCES season(season_id),
        role VARCHAR(50)
    );

--(5) Create the POSITION table
    -- 	CREATE TABLE Position (
    -- 		positionId INT AUTO_INCREMENT PRIMARY KEY,
    -- 		positionName VARCHAR(20)
    -- 	);

    CREATE TABLE position (
        position_id SERIAL PRIMARY KEY,
        position_name VARCHAR(50)
    );

--(6) Created the PLAYER table
    -- 	CREATE TABLE Player (
    -- 		playerId INT AUTO_INCREMENT PRIMARY KEY,
    -- 		fName VARCHAR(50) NOT NULL,
    -- 		lName VARCHAR(50) NOT NULL,
    -- 		teamId INT NOT NULL,
    -- 		positionId INT NOT NULL,
    -- 		FOREIGN KEY (teamId) REFERENCES Team(teamId),
    -- 		FOREIGN KEY (positionId) REFERENCES `Position`(positionId)
    -- 	);

    CREATE TABLE player (
        player_id SERIAL PRIMARY KEY,
        player_name VARCHAR(50),
        age INT NOT NULL,
        height SMALLINT,
        weight SMALLINT,
        college VARCHAR(50),
        position_id INT NOT NULL REFERENCES position(position_id),
        player_img VARCHAR(255)
    );

    CREATE TABLE player_team (
        player_team_id SERIAL PRIMARY KEY,
        player_id INT NOT NULL REFERENCES player(player_id),
        team_id INT NOT NULL REFERENCES team(team_id),
        season_id INT NOT NULL REFERENCES season(season_id),
        jersey_number INT,
        UNIQUE(player_id, season_id)
    );

-- Create the GAME table
    --     CREATE TABLE Game (
    --         gameId INT AUTO_INCREMENT PRIMARY KEY,
    -- 		homeTeamId INT NOT NULL,
    -- 		awayTeamId INT NOT NULL,
    --         gameDate DATE NOT NULL,
    -- 		homeTeamScore INT NOT NULL,
    -- 		awayTeamScore INT NOT NULL,
    -- 		seasonId INT NOT NULL,
    --         FOREIGN KEY (homeTeamId) REFERENCES Team(teamId),
    --         FOREIGN KEY (awayTeamId) REFERENCES Team(teamId),
    -- 		FOREIGN KEY (seasonId) REFERENCES Season(seasonId)
    --     );
    CREATE TABLE game (
        game_id SERIAL PRIMARY KEY,
        home_team_id INT NOT NULL REFERENCES team(team_id),
        away_team_id INT NOT NULL REFERENCES team(team_id),
        game_date DATE NOT NULL,
        home_team_score INT NOT NULL,
        away_team_score INT NOT NULL,
        season_id INT NOT NULL REFERENCES season(season_id)
    );


-- Create the SEASON table

    -- 	CREATE TABLE Season (
    -- 		seasonId INT AUTO_INCREMENT PRIMARY KEY,
    -- 		seasonYear VARCHAR(9) NOT NULL,
    -- 		startDate DATE NOT NULL,
    -- 		endDate DATE NOT NULL
    -- 	);
    CREATE TABLE season (
        season_id SERIAL PRIMARY KEY,
        season_year VARCHAR(20) NOT NULL
    );

--Create the PLAYER STATS table
    -- 	CREATE TABLE offensivePlayerStats (
    -- 		offensiveStatsId INT AUTO_INCREMENT PRIMARY KEY,
    -- 		passingTouchdowns INT DEFAULT 0,
    -- 		receivingTouchdowns INT DEFAULT 0,
    -- 		rushingTouchdowns INT DEFAULT 0,
    -- 		rushingYards INT DEFAULT 0,
    -- 		passingYards INT DEFAULT 0,
    -- 		receivingYards INT DEFAULT 0,
    -- 		playerId INT NOT NULL,
    -- 		gameId INT NOT NULL,
    -- 		teamId INT NOT NULL,
    -- 		FOREIGN KEY (playerId) REFERENCES Player(playerId) ON DELETE CASCADE,
    -- 		FOREIGN KEY (gameId) REFERENCES Game(gameId) ON DELETE CASCADE,
    -- 		FOREIGN KEY (teamId) REFERENCES Team(teamId) ON DELETE CASCADE
    -- 		-- 'ON DELETE CASCADE' ensures that if a player, game, or team is deleted, their related stats are automatically removed to maintain data integrity.
    -- 	);
    CREATE TABLE OffPlayerStats(
        offensive_stats_id SERIAL PRIMARY KEY,
        passing_td INT DEFAULT 0,
        receiving_td INT DEFAULT 0,
        rushing_td INT DEFAULT 0,
        rushing_yards INT DEFAULT 0,
        passing_yards INT DEFAULT 0,
        receiving_yards INT DEFAULT 0,
        player_id INT NOT NULL REFERENCES player(player_id) ON DELETE CASCADE,
        game_id INT NOT NULL REFERENCES  game(game_id) ON DELETE CASCADE,
        team_id INT NOT NULL REFERENCES team(team_id) ON DELETE CASCADE,
        UNIQUE (player_id, game_id)
    );

    -- 	CREATE TABLE defensivePlayerStats(
    -- 		defensiveStatsId INT AUTO_INCREMENT PRIMARY KEY,
    -- 		tackles INT DEFAULT 0,
    -- 		sacks INT DEFAULT 0,
    -- 		interceptions INT DEFAULT 0,
    -- 		forcedFumbles INT DEFAULT 0,
    -- 		playerId INT NOT NULL,
    -- 		gameId INT NOT NULL,
    -- 		teamId INT NOT NULL,
    -- 		FOREIGN KEY (playerId) REFERENCES Player(playerId) ON DELETE CASCADE,
    -- 		FOREIGN KEY (gameId) REFERENCES Game(gameId) ON DELETE CASCADE,
    -- 		FOREIGN KEY (teamId) REFERENCES Team(teamId) ON DELETE CASCADE
    -- 		-- 'ON DELETE CASCADE' ensures that if a player, game, or team is deleted, their related stats are automatically removed to maintain data integrity.
    -- 	);
    CREATE TABLE defensivePlayerStats(
		defensiveStatsId SERIAL PRIMARY KEY,
		tackles INT DEFAULT 0,
		sacks INT DEFAULT 0,
		interceptions INT DEFAULT 0,
		forcedFumbles INT DEFAULT 0,
		player_id INT NOT NULL REFERENCES player(player_id) ON DELETE CASCADE,
		game_id INT NOT NULL REFERENCES game(game_id) ON DELETE CASCADE,
		team_id INT NOT NULL REFERENCES team(team_id) ON DELETE CASCADE,
        UNIQUE (player_id, game_id)
	);

--Create the TEAM STATS table
    -- 	CREATE TABLE TeamStats (
    -- 		teamStatsId INT AUTO_INCREMENT PRIMARY KEY,
    -- 		teamId INT NOT NULL,
    -- 		totalWins INT DEFAULT 0,
    -- 		totalLosses INT DEFAULT 0,
    -- 		totalRushingTouchdowns INT DEFAULT 0,
    -- 		totalReceivingTouchdowns INT DEFAULT 0,
    -- 		totalPassingTouchdowns INT DEFAULT 0,
    -- 		totalRushingYards INT DEFAULT 0,
    -- 		totalReceivingYards INT DEFAULT 0,
    -- 		totalPassingYards INT DEFAULT 0,
    -- 		FOREIGN KEY (teamId) REFERENCES Team(teamId) ON DELETE CASCADE
    -- 	);
    CREATE TABLE TeamStats (
		team_stats_id SERIAL PRIMARY KEY,
        season INT NOT NULL,
		team_id INT NOT NULL REFERENCES team(team_id) ON DELETE CASCADE,
		total_wins INT DEFAULT 0,
		total_losses INT DEFAULT 0,
        total_ties INT DEFAULT 0,
		total_rushing_touchdowns INT DEFAULT 0,
		total_receiving_touchdowns INT DEFAULT 0,
		total_passing_touchdowns INT DEFAULT 0,
		total_rushing_yards INT DEFAULT 0,
		total_receiving_yards INT DEFAULT 0,
		total_passing_yards INT DEFAULT 0,
        UNIQUE (team_id, season)
	);