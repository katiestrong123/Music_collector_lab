DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;

CREATE TABLE artists (
id SERIAL PRIMARY KEY, -- Primary Key
name VARCHAR(255)
);

CREATE TABLE albums (
  id SERIAL PRIMARY KEY, -- Primary Key
  artist_id INT REFERENCES artists(id), -- Foreign Key refs to artists table
  title VARCHAR(255),  
  genre VARCHAR(255)
);