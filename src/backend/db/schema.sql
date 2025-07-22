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
	CREATE TABLE Team (
		teamId INT AUTO_INCREMENT PRIMARY KEY,
		teamName VARCHAR(100) NOT NULL,
		stadiumId INT NOT NULL,
		city VARCHAR(20) NOT NULL,
		state VARCHAR(2),
		logoPath VARCHAR(255) NOT NULL,
		FOREIGN KEY (stadiumId) REFERENCES Stadium(stadiumId)
	);
	
--(4) Created the COACH table

	CREATE TABLE Coach (
		coachId INT AUTO_INCREMENT PRIMARY KEY,
		fName VARCHAR(50) NOT NULL,
		lName VARCHAR(50) NOT NULL,
		teamId INT NOT NULL,
		FOREIGN KEY (teamId) REFERENCES Team(teamId)
	);


--(5) Create the POSITION table
	CREATE TABLE Position (
		positionId INT AUTO_INCREMENT PRIMARY KEY,
		positionName VARCHAR(20)
	);


--(6) Created the PLAYER table
	CREATE TABLE Player (
		playerId INT AUTO_INCREMENT PRIMARY KEY,
		fName VARCHAR(50) NOT NULL,
		lName VARCHAR(50) NOT NULL,
		teamId INT NOT NULL,
		positionId INT NOT NULL,
		FOREIGN KEY (teamId) REFERENCES Team(teamId),
		FOREIGN KEY (positionId) REFERENCES `Position`(positionId) 
	);




-- Create the GAME table
    CREATE TABLE Game (
        gameId INT AUTO_INCREMENT PRIMARY KEY,
		homeTeamId INT NOT NULL,
		awayTeamId INT NOT NULL,
        gameDate DATE NOT NULL,
		homeTeamScore INT NOT NULL,
		awayTeamScore INT NOT NULL,
		seasonId INT NOT NULL,
        FOREIGN KEY (homeTeamId) REFERENCES Team(teamId),
        FOREIGN KEY (awayTeamId) REFERENCES Team(teamId),
		FOREIGN KEY (seasonId) REFERENCES Season(seasonId)
    );

-- Create the SEASON table

	CREATE TABLE Season (
		seasonId INT AUTO_INCREMENT PRIMARY KEY,
		seasonYear VARCHAR(9) NOT NULL,
		startDate DATE NOT NULL,
		endDate DATE NOT NULL
	);


--Create the PLAYER STATS table
	CREATE TABLE offensivePlayerStats (
		offensiveStatsId INT AUTO_INCREMENT PRIMARY KEY,
		passingTouchdowns INT DEFAULT 0,
		receivingTouchdowns INT DEFAULT 0,
		rushingTouchdowns INT DEFAULT 0,
		rushingYards INT DEFAULT 0,
		passingYards INT DEFAULT 0,
		receivingYards INT DEFAULT 0,
		playerId INT NOT NULL,
		gameId INT NOT NULL,
		teamId INT NOT NULL,
		FOREIGN KEY (playerId) REFERENCES Player(playerId) ON DELETE CASCADE,
		FOREIGN KEY (gameId) REFERENCES Game(gameId) ON DELETE CASCADE,
		FOREIGN KEY (teamId) REFERENCES Team(teamId) ON DELETE CASCADE
		-- 'ON DELETE CASCADE' ensures that if a player, game, or team is deleted, their related stats are automatically removed to maintain data integrity.
	);

	CREATE TABLE defensivePlayerStats(
		defensiveStatsId INT AUTO_INCREMENT PRIMARY KEY,
		tackles INT DEFAULT 0,
		sacks INT DEFAULT 0, 
		interceptions INT DEFAULT 0,
		forcedFumbles INT DEFAULT 0,
		playerId INT NOT NULL,
		gameId INT NOT NULL,
		teamId INT NOT NULL,
		FOREIGN KEY (playerId) REFERENCES Player(playerId) ON DELETE CASCADE,
		FOREIGN KEY (gameId) REFERENCES Game(gameId) ON DELETE CASCADE,
		FOREIGN KEY (teamId) REFERENCES Team(teamId) ON DELETE CASCADE
		-- 'ON DELETE CASCADE' ensures that if a player, game, or team is deleted, their related stats are automatically removed to maintain data integrity.
	);


--Create the TEAM STATS table
	CREATE TABLE TeamStats (
		teamStatsId INT AUTO_INCREMENT PRIMARY KEY,
		teamId INT NOT NULL,
		totalWins INT DEFAULT 0,
		totalLosses INT DEFAULT 0,
		totalRushingTouchdowns INT DEFAULT 0,
		totalReceivingTouchdowns INT DEFAULT 0,
		totalPassingTouchdowns INT DEFAULT 0,
		totalRushingYards INT DEFAULT 0,
		totalReceivingYards INT DEFAULT 0,
		totalPassingYards INT DEFAULT 0,
		FOREIGN KEY (teamId) REFERENCES Team(teamId) ON DELETE CASCADE
	);