-- creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- set db to new db
USE hbtn_0d_usa;
-- create new table
CREATE TABLE IF NOT EXISTS states(
id INT NOT NULL AUTO_INCREMENT UNIQUE,
name VARCHAR(256) NOT NULL, PRIMARY KEY (id));
Create database and table