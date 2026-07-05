/*
Lesson 5: Data Modification via INSERT, UPDATE, and DELETE.

Mission Scenario:
The Galactic Federation needs to manage space stations in real-time. 
We need to add a new station to the 'Alpha-01' sector, update combat and energy 
settings for all stations in 'Widow-7' due to a peace treaty, and completely 
remove all records of stations in 'Sector-G' because it was destroyed.

Working Table State (After Script Execution):
+----+----------------+-------------+--------+---------------+
| id | station_name   | sector_code | combat | energy_output |
+----+----------------+-------------+--------+---------------+
| 1  | Deep Space 9   | Alpha-01    | false  | NULL          |
| 2  | Citadel        | Widow-7     | false  | 3000          |
| 4  | Deep Space 10  | Alpha-01    | false  | NULL          |
+----+----------------+-------------+--------+---------------+
Note: 'Omega Outpost' from Sector-G is deleted. 
'Deep Space 9' energy remains NULL because it wasn't modified.

Key Concepts:
- 'insert into': Used to add new rows. If you skip a column (like 'energy_output'), 
  SQL automatically puts a NULL value there.
- 'update': Used to change existing data. You use 'set' to change column values. 
  Always use 'where' to target specific rows, or you will change the whole database!
- 'delete from': Used to permanently remove rows. Just like 'update', it needs a 
  'where' clause to avoid deleting all data in the table.
*/

insert into space_stations (station_name, sector_code, combat)
values ('Deep Space 10', 'Alpha-01', false);

update space_stations 
set combat = false, energy_output = 3000
where sector_code = 'Widow-7';

delete from space_stations 
where sector_code = 'Sector-G';