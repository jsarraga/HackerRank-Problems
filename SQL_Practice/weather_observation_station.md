The STATION table is described as follows:


STATION
FIELD               TYPE
ID                  NUMBER
CITY                VARCHAR2(21)
STATE               VARCHAR2(2)
LAT_N               NUMBER
LONG_W              NUMBER


#### Query a list of CITY and STATE from the STATION table.

SELECT CITY, STATE FROM STATION;

#### Query a list of CITY names from STATION for cities that have an even ID number. Print the results in any order, but exclude duplicates from the answer.

SELECT DISTINCT CITY FROM STATION WHERE ID%2=0;

#### Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.

SELECT (SELECT COUNT(CITY)) - (SELECT COUNT(DISTINCT CITY)) FROM STATION;

#### Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.

SELECT city, length(city) FROM STATION ORDER BY length(city) DESC LIMIT 1;

SELECT city, length(city) FROM STATION ORDER BY length(city) ASC, city ASC LIMIT 1;

#### Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.

SELECT city FROM station WHERE city LIKE 'A%' OR city LIKE 'E%' OR city LIKE 'I%' OR city LIKE 'O%' OR city LIKE 'U%';


#### Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.

SELECT city FROM station WHERE city LIKE '%a' OR city LIKE '%e' OR city LIKE '%i' OR city LIKE '%o' OR city LIKE '%u';

#### Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your result cannot contain duplicates.

SELECT DISTINCT city FROM station WHERE city REGEXP '^[aeiou]' AND city REGEXP '[aeiou]$';

<!-- 
This uses a REGEXP built-in REGEX Pattern matcher. 
'xyz' finds entries that contain xyz anywhere.
'^' finds entries that begin with chars or an array of chars []. '$' finds entries that end with chars. 
-->

#### Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.

SELECT DISTINCT city FROM station WHERE city NOT REGEX '^[aeiou]';

#### Query the list of CITY names from STATION that do not end with vowels. Your result cannot contain duplicates.

SELECT DISTINCT city FROM station WHERE city NOT REGEXP '[aeiou]$';

#### Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.

SELECT DISTINCT city FROM station WHERE city NOT REGEXP '^[aeiou]' OR city NOT REGEXP '[aeiou]$';

#### Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.

SELECT DISTINCT city FROM station WHERE city NOT REGEXP '^[aeiou]' AND city NOT REGEXP '[aeiou]$';

###Query the following two values from the STATION table: 
# 1.) The sum of all values in LAT_N rounded to a scale of  decimal places. 
# 2.) The sum of all values in LONG_W rounded to a scale of  decimal places.
#output: lat long

SELECT ROUND(SUM(LAT_N), 2), ROUND(SUM(LONG_W), 2) from station;

#### Query the sum of Northern Latitudes (LAT_N) from STATION having values greater than 38.7880 and less than 137.2345. Truncate your answer to 4 decimal places.

SELECT ROUND(SUM(LAT_N),4) FROM Station WHERE LAT_N > 38.7880 AND LAT_N < 137.2345;

#### Query the greatest value of the Northern Latitudes (LAT_N) from STATION that is less than . Truncate your answer to  decimal places.

SELECT ROUND(MAX(LAT_N), 4) FROM Station where LAT_N < 137.2345;