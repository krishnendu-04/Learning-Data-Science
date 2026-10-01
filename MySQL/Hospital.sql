CREATE DATABASE Hospital;
USE Hospital;
CREATE TABLE Patients(patient_id int,name VARCHAR(30),disease VARCHAR(30),doctor VARCHAR(30),room VARCHAR(10));
INSERT INTO Patients VALUES(1,'Anu','Flu','Ben','A101'),(2,'Rohan','Back pain','Smitha','A102'),(3,'Jim','Cold','Ben','A103'),(4,'Farah','Asthma','Ben','B101'),(5,'Riya','Flu','Smitha','B102');
SELECT * from Patients;
