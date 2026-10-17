USE industry;
CREATE TABLE customers_data(CustomerID INT,Name VARCHAR(30),Age INT,Gender VARCHAR(10),City VARCHAR(30),Email VARCHAR(30),Phone VARCHAR(15),AnnualIncome_INR DOUBLE,SpendingScore INT,JoinDate DATE);
LOAD DATA LOCAL INFILE '/Users/krishnenduc/Documents/GitHub/Learning-Data-Science/MySQL/Data/customers_data.csv'
INTO TABLE customers_data
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
SELECT * FROM customers_data;

SELECT * FROM customers_data ORDER BY Age;
SELECT * FROM customers_data ORDER BY AnnualIncome_INR DESC;
SELECT Name,City FROM customers_data ORDER BY City;
SELECT * FROM customers_data ORDER BY SpendingScore DESC;
SELECT * FROM customers_data ORDER BY JoinDate;
SELECT Name,Gender,Age FROM customers_data ORDER BY GENDER,AGE DESC;

SELECT * FROM customers_data ORDER BY AnnualIncome_INR DESC LIMIT 5;
SELECT * FROM customers_data WHERE City='Delhi' ORDER BY Age LIMIT 3;
SELECT * FROM customers_data WHERE Gender='Female' ORDER BY SpendingScore DESC LIMIT 10;
SELECT * FROM customers_data ORDER BY JoinDate DESC LIMIT 5;
SELECT Name FROM customers_data WHERE Gender='Male' ORDER BY AnnualIncome_INR DESC LIMIT 5;
SELECT Name FROM customers_data WHERE SpendingScore>50 ORDER BY Age DESC LIMIT 3;

SELECT DISTINCT City FROM customers_data;
SELECT DISTINCT Gender FROM customers_data;
SELECT COUNT(DISTINCT CITY) FROM customers_data;
SELECT DISTINCT CITY,Gender FROM customers_data;
SELECT DISTINCT Age FROM customers_data WHERE SpendingScore>70;
SELECT DISTINCT YEAR(JoinDate) AS YEAR FROM customers_data;

SELECT AVG(Age) FROM customers_data;
SELECT MAX(AnnualIncome_INR),MIN(AnnualIncome_INR) FROM customers_data;
SELECT COUNT(*) FROM customers_data;
SELECT AVG(SpendingScore) FROM customers_data;
SELECT SUM(AnnualIncome_INR) FROM customers_data;
SELECT COUNT(*) FROM customers_data WHERE SpendingScore>80;

SELECT City,AVG(SpendingScore) FROM customers_data GROUP BY City;
SELECT City,Count(*) FROM customers_data GROUP BY City;
SELECT Gender,AVG(AnnualIncome_INR) FROM customers_data GROUP BY GENDER;
SELECT City,MAX(Age) FROM customers_data GROUP BY City;
SELECT Gender,COUNT(*) FROM customers_data GROUP BY Gender ORDER BY COUNT(*) DESC;
SELECT City,AVG(AnnualIncome_INR) FROM customers_data GROUP BY City HAVING COUNT(DISTINCT CustomerID)>3;

SELECT COUNT(DISTINCT CustomerID) FROM customers_data WHERE SpendingScore>90;

SELECT DISTINCT City FROM customers_data ORDER BY City;
SELECT DISTINCT Gender FROM customers_data WHERE Age>30 ORDER BY Gender;
SELECT City FROM customers_data WHERE SpendingScore>60 GROUP BY CITY ORDER BY MAX(SpendingScore) DESC LIMIT 5;
SELECT DISTINCT Age FROM customers_data WHERE Gender='Female' ORDER BY Age LIMIT 5;
SELECT DISTINCT AnnualIncome_INR FROM customers_data WHERE City='Mumbai' ORDER BY AnnualIncome_INR DESC LIMIT 3;
SELECT DISTINCT City FROM customers_data WHERE SpendingScore>90 GROUP BY City HAVING COUNT(DISTINCT CustomerID)>=1 LIMIT 5;
SELECT DISTINCT(YEAR(JoinDate)) FROM customers_data WHERE AnnualIncome_INR>1000000;
SELECT DISTINCT Gender,City FROM customers_data WHERE Age BETWEEN 25 AND 40 ORDER BY City LIMIT 10;
SELECT DISTINCT(SpendingScore) FROM customers_data WHERE Gender='Male' ORDER BY SpendingScore DESC LIMIT 5;
SELECT City,Count(*) FROM customers_data WHERE JoinDate>'2024-01-01' GROUP BY City ORDER BY COUNT(*) DESC LIMIT 5;
