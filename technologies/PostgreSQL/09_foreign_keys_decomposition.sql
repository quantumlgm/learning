/*
Lesson 9: Database Decomposition and Foreign Key Constraints.

Mission Scenario:
Our database has duplicate text codes for sectors, which is bad design. 
We need to perform data decomposition: create a new, separate 'sectors' table, 
and then link our 'space_stations' table to it using a Foreign Key. Finally, 
we will safely drop the old text column because the relationship replaces it.

Working Tables State (After Structural Migration):
Table 1: 'sectors' (Parent Table)
+----+-------------+--------------+
| id | sector_code | danger_level |
+----+-------------+--------------+
| PK | Unique Text | Integer(0-5) |
+----+-------------+--------------+

Table 2: 'space_stations' (Child Table - Mutated)
+----+----------------+--------+---------------+-----------+
| id | station_name   | combat | energy_output | sector_id |
+----+----------------+--------+---------------+-----------+
| PK | Varchar        | Boolean| Integer       | FK ------> links to sectors.id
+----+----------------+--------+---------------+-----------+
Note: The old text column 'sector_code' is now permanently removed.

Key Concepts:
- Data Decomposition: Splitting one large, messy table into smaller, specialized 
  tables to prevent data duplication and save disk space.
- 'foreign key': A column constraint that links two tables together. It guarantees 
  referential integrity — you cannot link a station to a sector id that does not exist.
- 'check' constraint: A native validation rule that stops invalid data (like 
  danger level 999) from entering the database at the architectural level.
*/

drop table if exists sectors cascade;

create table sectors (
	id serial primary key,
	sector_code varchar(20) unique,
	danger_level int check (danger_level >= 0 and danger_level <= 5)
);

alter table space_stations add column sector_id int;
alter table space_stations add foreign key (sector_id) references sectors(id);

alter table space_stations drop column sector_code;