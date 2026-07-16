/*
Lesson 21: Practical Common Table Expressions (CTE / WITH).

Mission Scenario:
The syndicate's leadership wants to identify the "elite" ships in our fleet.
We need to find ships whose individual speed is STRICTLY higher than the average 
speed of their specific model.

Why we use CTE here:
We cannot use an aggregate function like AVG(speed) directly in the WHERE clause 
of a standard query. By using a CTE, we calculate the averages first in a temporary 
virtual table, and then easily join and filter against it.

Visualizing the CTE flow:
+---------------------------------------------------------+
| STEP 1: CTE "avg_speed" (Calculates averages)           |
| model           | avg_speed                             |
|-----------------|---------------------------------------|
| Exceed Sunny    | 966.6                                 |
| Stormbringer    | 650.0                                 |
+---------------------------------------------------------+
                           |
                           v (JOINed with main tables)
+---------------------------------------------------------+
| STEP 2: Main Query (Filters: ships.speed > avg_speed)   |
| first_name | model        | speed | model_average_speed |
|------------|--------------|-------|---------------------|
| Alex       | Stormbringer | 700   | 650.0   (700 > 650) |
| Elena      | Exceed Sunny | 1200  | 966.6  (1200 > 966) |
+---------------------------------------------------------+
*/

with avg_speed as (
	select model, avg(speed) as avg_speed
	from ships
	group by model
)
select 
	c.first_name, 
	c.last_name,
	s.model,
	s.speed,
	asd.avg_speed
from couriers as c
join ships as s on c.id = s.courier_id
join avg_speed as asd on s.model = asd.model
where s.speed > asd.avg_speed 
order by s.model, s.speed
