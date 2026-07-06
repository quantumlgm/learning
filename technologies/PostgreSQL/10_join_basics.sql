/*
Lesson 10: Relational Data Merging via INNER JOIN.

Mission Scenario:
The Admiralty needs a unified operational report. We need to combine data from 
'space_stations' and 'sectors' to display the station name alongside its 
sector code and danger level. The report must filter and show only combat-ready 
stations located in high-risk sectors (danger level greater than 2), sorted by 
danger from highest to lowest.

Working Tables State (After Data Seeding):
Table 1: 'sectors' (sc)
+----+-------------+--------------+
| id | sector_code | danger_level |
+----+-------------+--------------+
| 1  | alpha-01    | 1            |
| 2  | widow-7     | 4            |
| 3  | epsilon-4   | 2            |
+----+-------------+--------------+

Table 2: 'space_stations' (ss)
+----+----------------+--------+---------------+-----------+
| id | station_name   | combat | energy_output | sector_id |
+----+----------------+--------+---------------+-----------+
| 1  | Deep Space 9   | false  | 4500          | 1         |
| 2  | Citadel        | false  | 3000          | 2         |
| 3  | Omega Outpost  | true   | 9500          | 1         |
| 6  | Nautilus       | true   | 5500          | 2         |
...  | ...            | ...    | ...           | ...       |
+----+----------------+--------+---------------+-----------+

Key Concepts:
- 'inner join' / 'join': Merges rows from two different tables into a single 
  result set based on a matching condition specified in the 'on' clause.
- Table Aliasing ('as ss', 'as sc'): Allows assigning short nicknames to tables. 
  This keeps the query clean and readable when prefixing column names.
- Multi-Table Filtering: After joining, you can filter columns from both tables 
  simultaneously using standard 'where' logical operators.
*/

select 
    ss.station_name, 
    sc.sector_code, 
    sc.danger_level
from space_stations as ss 
join sectors as sc on ss.sector_id = sc.id
where sc.danger_level > 2 and ss.combat = true
order by sc.danger_level desc;