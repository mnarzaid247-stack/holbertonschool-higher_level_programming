-- forghin key
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
	id INT PRIMARY KEY,
	state_id INT NOT NULL FOREIGN KEY REFERENEC TO states(id),
	name VARCHAR(256)
	);
