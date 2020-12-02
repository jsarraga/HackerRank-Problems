
The Employee table is described as follows:

Employee
COLUMN          TYPE
employee_id     INTEGER
name            STRING
months          INTEGER
salary          INTEGER

#### Write a query that prints a list of employee names (i.e.: the name attribute) from the Employee table in alphabetical order.

SELECT name FROM employee ORDER BY name;

#### Write a query that prints a list of employee names (i.e.: the name attribute) for employees in Employee having a salary greater than  $2000 per month who have been employees for less than 10 months. Sort your result by ascending employee_id.

SELECT name FROM employee WHERE salary > 2000 AND months < 10 ORDER BY employee_id ASC;

#### We define an employee's total earnings to be their monthly  worked, and the maximum total earnings to be the maximum total earnings for any employee in the Employee table. Write a query to find the maximum total earnings for all employees as well as the total number of employees who have maximum total earnings. Then print these values as  space-separated integers.

SELECT (salary * months) as earnings, count(1) FROM employee GROUP BY earnings ORDER BY 1 DESC LIMIT 1; 