/*
Lesson 6: Row Grouping and Data Aggregation using GROUP BY.

Mission Scenario:
The Galactic Federation wants a statistical report about space stations. 
We need to count how many stations are in each sector. We only care about 
powerful stations (energy above 4000) or new stations where energy is not 
set yet (NULL). The final list must show sectors with the most stations first.

Working Table State (Source Data Reference):
+----+----------------+-------------+--------+---------------+
| id | station_name   | sector_code | combat | energy_output |
+----+----------------+-------------+--------+---------------+
| 1  | Deep Space 9   | Alpha-01    | false  | NULL          |
| 2  | Citadel        | Widow-7     | false  | 3000          |
| 4  | Deep Space 10  | Alpha-01    | false  | NULL          |
+----+----------------+-------------+--------+---------------+

Key Concepts:
- 'group by': Converted multiple individual rows into a single summary row 
  for each unique sector code.
- 'as' (Column Aliasing): Created a temporary name 'station_count' for the 
  aggregated column so we can easily reuse it inside the 'order by' clause.
- 'is null': A special SQL operator. You cannot use '=' to find NULL values 
  because NULL means "unknown". You must always write 'column is null'.
- 'count(*)': Counts all rows that belong to the group after the 'where' 
  filter removes unwanted data.
*/

select sector_code, count(*) as station_count from space_stations
where energy_output > 4000 or energy_output is null
group by sector_code 
order by station_count desc, sector_code