/*
Lesson 7: Advanced Data Aggregation and Mathematical Expressions.

Mission Scenario:
The Galactic Federation needs an energy audit for non-combat space stations. 
We need to group stations by their sectors and calculate three things: the total 
energy power, the average energy power, and the energy gap (difference between 
the maximum and minimum power in that sector). Finally, we must show the top 2 
most energy-efficient sectors.

Working Table State (After Data Refresh):
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
- Math inside SELECT: You can use standard math operations (like minus '-') 
  directly between aggregate functions, for example: 'max(column) - min(column)'.
- 'sum()' and 'avg()': 'sum' adds all numbers in the group together, while 
  'avg' automatically calculates the arithmetic mean for each group.
- Global Filters ('where') with Aggregates: The 'where' clause runs BEFORE the 
  grouping happens. It completely removes combat stations (combat = true) so 
  they do not affect our math.
*/

select 
    sector_code, 
    sum(energy_output) as total_power, 
    avg(energy_output) as average_power,
    max(energy_output) - min(energy_output) as power_gap
from space_stations
where combat = false
group by sector_code
order by average_power desc
limit 2;