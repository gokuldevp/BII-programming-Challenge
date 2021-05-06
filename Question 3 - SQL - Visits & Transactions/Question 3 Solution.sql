/*
Write queries for the following scenarios and to retrieve the following information from
the tables mentioned below
1. Max user visit date
2. Max amount transaction at a date
3. User with max transaction amount
4. Average transaction per day
5. User visited but did not do a transaction

Database Tables:

'Visits' table:                   'Transactions' table:
+---------+-------------+        +---------+--------------------+---------+
| user_id | visit_date |         | user_id | transaction_date | amount  |
+---------+-------------+        +---------+--------------------+---------+
| 1       | 2020-01-01 |         | 1       | 2020-01-02       | 120     |
| 2       | 2020-01-02 |         | 2       | 2020-01-03       | 22      |
| 12      | 2020-01-01 |         | 7       | 2020-01-11       | 232     |
| 19      | 2020-01-03 |         | 1       | 2020-01-04       | 7       |
| 1       | 2020-01-02 |         | 9       | 2020-01-25       | 33      |
| 2       | 2020-01-03 |         | 9       | 2020-01-25       | 66      |
| 1       | 2020-01-04 |         | 8       | 2020-01-28       | 1       |
| 7       | 2020-01-11 |         | 9       | 2020-01-25       | 99      |
| 9       | 2020-01-25 |         +---------+--------------------+--------+
| 8       | 2020-01-28 |
+---------+------------+
*/

--> Creating the table Visits:
-- CREATE TABLE visits(
--     user_id INT NOT NULL,
-- 	visit_date DATE NOT NULL
-- );

--> Inserting Values into table Visits: 
-- INSERT INTO visits(user_id, visit_date) 
-- VALUES (1, '2020-01-01'),
--        (2, '2020-01-02'),
-- 	   (12,'2020-01-01'),
-- 	   (19,'2020-01-03'),
-- 	   (1, '2020-01-02'),
-- 	   (2, '2020-01-03'),
-- 	   (1, '2020-01-04'),
-- 	   (7, '2020-01-11'),
-- 	   (9, '2020-01-25'),
-- 	   (8, '2020-01-28');

--> Creating Table transactions:
-- CREATE TABLE transactions(
--     user_id INT NOT NULL,
-- 	transaction_date DATE NOT NULL,
-- 	amount INT NOT NULL
-- );

--> Inserting Values into Table transactions:
-- INSERT INTO transactions(user_id, transaction_date, amount)
-- VALUES (1, '2020-01-02', 120),
--        (2, '2020-01-03', 22 ),
-- 	   (7, '2020-01-11', 232),
-- 	   (1, '2020-01-04', 7  ),
-- 	   (9, '2020-01-25', 33 ),
-- 	   (9, '2020-01-25', 66 ),
-- 	   (8, '2020-01-28', 1  ),
-- 	   (9, '2020-01-25', 99 );
	   
--> 1. Max user visit date.
SELECT  visit_date  FROM  visits
GROUP BY visit_date
HAVING COUNT(*) 
IN (SELECT COUNT(*) FROM visits GROUP BY visit_date ORDER BY COUNT(*) DESC LIMIT 1);

--> 2. Max amount transaction at a date.
SELECT transaction_date, SUM(amount)  FROM transactions
GROUP BY transaction_date
ORDER BY SUM(amount) DESC;

--> 3. User with max transaction amount.
SELECT user_id FROM transactions
GROUP BY user_id
ORDER BY SUM(amount) DESC
LIMIT 1;

--> 4. Average transaction per day.
SELECT transaction_date, ROUND(AVG(amount))  FROM transactions
GROUP BY transaction_date
ORDER BY transaction_date;

--> 5. User visited but did not do a transaction
SELECT DISTINCT vis.user_id FROM visits AS vis
LEFT OUTER JOIN transactions AS tran
ON vis.user_id = tran.user_id
WHERE amount IS NULL;