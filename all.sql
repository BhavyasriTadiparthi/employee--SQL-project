CREATE TABLE employees(
 emp_id INTEGER PRIMARY KEY,
 name TEXT,
 department TEXT,
 salary INTEGER
);

INSERT INTO employees VALUES
(1,'Rohit','IT',70000),
(2,'Anu','HR',60000),
(3,'Kiran','IT',80000),
(4,'Divya','Finance',65000),
(5,'Sai','Marketing',72000);


SELECT * FROM employees;
SELECT * FROM employees ORDER BY salary DESC LIMIT 1;
SELECT AVG(salary) FROM employees;
SELECT AVG(salary) FROM employees;
SELECT department, COUNT(*) FROM employees GROUP BY department;


