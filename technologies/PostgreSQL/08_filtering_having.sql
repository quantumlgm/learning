/*
Lesson 8: Group Filtering using the HAVING Clause.

Mission Scenario:
The Galactic Council needs to find civilian sectors with high energy infrastructure 
and a high concentration of objects. We need to filter out combat stations first, 
group the remaining stations by sector, and then keep only the sectors that have 
MORE THAN 1 civilian station AND a total energy output GREATER THAN 7000. 
Finally, we show the average power for these sectors, sorted from highest to lowest.

Working Table State (Source Data Reference):
+----+----------------+-------------+--------+---------------+
| id | station_name   | sector_code | combat | energy_output |
+----+----------------+-------------+--------+---------------+
| 1  | Deep Space 9   | Alpha-01    | false  | 4500          |
| 2  | Citadel        | Widow-7     | false  | 3000          |
| 3  | Omega Outpost  | Alpha-01    | true   | 9500          |
| 4  | Babylon 5      | Epsilon-4   | false  | 6200          |
| 5  | Starbase 74    | Alpha-01    | true   | 12000         |
| 6  | Nautilus       | Widow-7     | true   | 5500          |
| 7  | Horizon        | Epsilon-4   | false  | 4100          |
| 8  | Zenith         | Widow-7     | false  | 3000          |
+----+----------------+-------------+--------+---------------+

Key Concepts:
- 'where' vs 'having': The 'where' clause filters rows BEFORE grouping (removes 
  military stations). The 'having' clause filters groups AFTER 'group by' runs 
  (checks total count and sum for the whole sector).
- Execution Order: SQL always evaluates 'where' -> 'group by' -> 'having' -> 
  'select' -> 'order by'. That is why you can use aggregate functions inside 
  'having', but you cannot use them inside 'where'.
*/

select 
    sector_code, 
    avg(energy_output) as avg_power
from space_stations
where combat = false 
group by sector_code 
having count(combat) > 1 and sum(energy_output) > 7000
order by avg_power desc