/*
Lesson 11: Outer Joins (LEFT, FULL) and Cross Joins.

Mission Scenario:
1. Infrastructure Audit: We need to list all existing space stations, including 
   autonomous hubs that are not linked to any specific sector. 
2. War Games Matrix: The Defense Staff needs to combine every single combat-ready 
   station with every available sector to calculate hypothetical deployment paths.

Working Tables State (Source Data Reference):
Table 1: 'sectors' (sc)
+----+-------------+--------------+
| id | sector_code | danger_level |
+----+-------------+--------------+
| 1  | alpha-01    | 1            |
| 2  | widow-7     | 4            |
| ...| ghost-99    | 5            |  <-- Sector with no stations
+----+-------------+--------------+

Table 2: 'space_stations' (ss)
+----+----------------+--------+---------------+-----------+
| id | station_name   | combat | energy_output | sector_id |
+----+----------------+--------+---------------+-----------+
| 1  | Deep Space 9   | false  | 4500          | 1         |
| 9  | roaming-hub    | false  | 1500          | NULL      |  <-- Station with no sector
+----+----------------+--------+---------------+-----------+

Key Concepts:
- 'full outer join': Combines rows from both tables. If there is no match on 
  the joining condition, it preserves the unmatched rows and fills the missing 
  side with NULL values.
- 'cross join': Creates a Cartesian product of two tables. It pairs every row 
  from the first table with every row from the second table without any 'on' condition.
*/

-- Query 1: Analysis of all stations (including autonomous ones)
select 
    ss.station_name, 
    sc.sector_code
from space_stations as ss
full outer join sectors as sc on ss.sector_id = sc.id;

-- Query 2: Deployment matrix for combat stations across all sectors
select 
    ss.station_name, 
    sc.sector_code
from space_stations as ss
cross join sectors as sc
where ss.combat = true;