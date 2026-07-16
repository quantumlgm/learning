/*
Lesson 20: Practical Window Functions (OVER, PARTITION BY, ORDER BY).

Mission Scenario:
We are generating a financial audit report for the courier syndicate. 
For every single delivery, we need to show the individual profit, the cumulative 
running total for that specific courier (ordered by delivery cost), and their 
overall total career earnings.

Visualizing Partitioning and Running Totals in a single window:
+---------------------------------------------------------------------------------------+
|                                  COURIER: ALEX (ID: 1)                                |
+------------------+-----------------+--------------------------------------------------+
| delivery_amount  | total_profit    | history_profit (Partitioned by ID + Ordered)    |
+------------------+-----------------+--------------------------------------------------+
| 100              | 600             | 100                                              |
| 200              | 600             | 300  (100 + 200)                                 |
| 300              | 600             | 600  (300 + 300)                                 |
+------------------+-----------------+--------------------------------------------------+
  *At this point, the partition changes to Courier ID 2. The running sum resets!*
+---------------------------------------------------------------------------------------+
|                                 COURIER: ELENA (ID: 2)                                |
+------------------+-----------------+--------------------------------------------------+
| 150              | 450             | 150  (Reset to start fresh for Elena)            |
| 300              | 450             | 450  (150 + 300)                                 |
+------------------+-----------------+--------------------------------------------------+
*/

select 
	c.first_name, 
	c.last_name,
	o.cost as delivery_amount,
	sum(o.cost) over (partition by c.first_name, c.last_name) as total_profit,
	sum(o.cost) over (partition by c.id order by o.cost, o.id) as history_porfit
from couriers c
join ships as s on c.id = s.courier_id
join orders as o on s.id = o.ship_id
