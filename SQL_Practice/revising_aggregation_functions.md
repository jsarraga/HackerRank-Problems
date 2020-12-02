CITY
FIELD           TYPE
id              number
name            varchar(17)
countrycode     varchar(3)
district        varchar(20)
population      number




#### Query a count of the number of cities in CITY having a Population larger than 100000

select count(name) from city where population > 100000;

#### Query the total population of all cities in CITY where District is California.

select sum(population) from city where district='California';

#### Query the average population of all cities in CITY where District is California.

select avg(population) from city where distrcit='California';

#### Query the average population for all cities in CITY, rounded down to the nearest integer.

select round(avg(population)) from city;

#### Query the sum of the populations for all Japanese cities in CITY. The COUNTRYCODE for Japan is JPN.

select sum(population) from city where countrycode="jpn"

#### Query the difference between the maximum and minimum populations in CITY.

select max(population) - min(population) from city;

