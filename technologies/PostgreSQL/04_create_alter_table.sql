/*
Lesson 4: Database Schema Design, DDL Mutations, and Table Evolution.

This module demonstrates Data Definition Language (DDL) fundamentals using PostgreSQL.
It showcases the lifecycle of an database object from safe initialization, constraints 
enforcement (Primary Keys via Auto-Sequencing), to subsequent structural modification 
without dropping existing dataset records.

Key Concepts:
- Idempotent Initialization ('drop table if exists'): Preventing environment setup failures 
  by purging conflicting legacy relations before creating new ones.
- Implicit Sequence Generation ('serial'): Abstracting primary key incrementation logic 
  away from the application layer to enforce entity integrity constraints natively.
- Schema Migration ('alter table'): Executing real-time table modifications including structural 
  extension ('add column'), destructive dropping ('drop column'), and property tracking adjustment ('rename to').
- Nullable Trailing Data Allocation: Demonstrating how existing rows seamlessly adapt to new schema 
  states by defaulting newly added fields to structural 'null' states.
  
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