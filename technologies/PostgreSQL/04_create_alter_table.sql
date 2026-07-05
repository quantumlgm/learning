/*
Lesson 4: Database Schema Design, DDL Mutations, and Table Evolution.

Mission Scenario:
The Galactic Federation is building orbital outposts. We need to create a table to track 
these stations. However, the military command changes its requirements during the project. 
We must modify the table structure on the fly: add a reactor power column, remove the supply 
capacity column, and rename the military status column—all without breaking the database.

Initial Architectural Blueprint:
+----+--------------+-------------+-----------------+-------------+
| id | station_name | sector_code | supply_capacity | is_military |
+----+--------------+-------------+-----------------+-------------+

Mutated & Final Schema State (Working Table: 'space_stations'):
+----+----------------+-------------+--------+---------------+
| id | station_name   | sector_code | combat | energy_output |
+----+----------------+-------------+--------+---------------+
| 1  | Deep Space 9   | Alpha-01    | false  | NULL          |
| 2  | Citadel        | Widow-7     | true   | NULL          |
| 3  | Omega Outpost  | Sector-G    | true   | 9500          |
+----+----------------+-------------+--------+---------------+

Key Concepts:
- 'drop table if exists': Cleans up old tables before creating a new one to prevent errors.
- 'serial primary key': Automatically generates unique ID numbers for new rows.
- 'alter table': Modifies an existing table structure using 'add column', 'drop column', 
  and 'rename to'.
- NULL defaults: When you add a new column, existing rows automatically get a NULL 
  (empty) value in that field.
*/

drop table if exists space_stations;

create table space_stations (
    id serial primary key,
    station_name varchar(150),
    sector_code varchar(20),
    supply_capacity int,
    is_military boolean
);

insert into space_stations 
(station_name, sector_code, supply_capacity, is_military)
values 
('Deep Space 9', 'Alpha-01', 5000, false),
('Citadel', 'Widow-7', 12000, true);

alter table space_stations add column energy_output int;
alter table space_stations drop column supply_capacity;
alter table space_stations rename is_military to combat;

insert into space_stations 
(station_name, sector_code, combat, energy_output)
values ('Omega Outpost', 'Sector-G', true, 9500);