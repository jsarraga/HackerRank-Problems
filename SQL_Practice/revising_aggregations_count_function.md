CITY
FIELD           TYPE
id              number
name            varchar(17)
countrycode     varchar(3)
district        varchar(20)
population      number




#### Query a count of the number of cities in CITY having a Population larger than 100000

select count(name) from city where population > 100000;