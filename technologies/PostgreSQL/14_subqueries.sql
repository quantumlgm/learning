/*
Lesson 14: Subqueries (Subselects) in SQL.

Mission Scenario:
To identify infrastructure anomalies, the engineering division requires a list of space 
stations whose power generation exceeds the overall systemic average. We utilize a 
scalar subquery inside the WHERE clause to dynamically compute the average energy output 
before filtering the final data set, eliminating hardcoded numeric thresholds.

Expected Query Output Reference:
+---------------+---------------+
| station_name  | energy_output |
+---------------+---------------+
| Omega Outpost |          9500 |
| Babylon 5     |          6200 |
+---------------+---------------+

Key Concepts:
- Scalar Subquery: A nested SELECT statement enclosed in parentheses that returns a single 
  value (one row, one column). It can be used with standard comparison operators (>, <, =).
- Execution Order: The database engine evaluates the inner subquery first, caches the 
  aggregated result, and then utilizes it to execute the outer filtering sequence.
*/

select station_name, energy_output 
from space_stations
where energy_output > (
	select avg(energy_output) from space_stations
)