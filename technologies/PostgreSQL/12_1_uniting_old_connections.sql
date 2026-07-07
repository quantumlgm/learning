/*
Lesson 12.1: Schema Refactoring, Data Normalization, and Foreign Key Adjustments.

Mission Scenario:
To eliminate data redundancy and prevent logical anomalies, the system architecture 
requires a strict hierarchical refactoring. Orders must target specific endpoints directly 
without duplicating higher-level routing data. We alter the existing tables to strip 
redundant lineage columns, inject new destination foreign keys, and establish a clean, 
normalized cascade from Master Entities down to Transactional Records.

Working Architecture Tree (Normalized Data Hierarchy):
 
   [couriers]           [planets]
       |                   |
       | 1:N               | 1:N
       v                   v
    [ships]            [sectors]
       |                   |
       |                   | 1:N
       |                   v
       |            [space_stations]
       |                   |
       | 1:N               | 1:N
       +---------> <-------+
                  |
                  v
               [orders]

Key Concepts:
- Data Redundancy & Anomalies: Storing planet_id directly inside the orders table while 
  it is already implicitly linked via sectors and stations creates a risk of conflicting 
  data. Removing it enforces transactional integrity.
- Altering Foreign Keys: When executing ALTER TABLE statements to append constraints, 
  the local foreign key column name must strictly map to the exact primary key identifier 
  of its designated parent table to maintain referential validation.
*/

alter table orders drop constraint station_id_fk;

alter table orders add column station_id int;
alter table orders add constraint station_id_fk foreign key (station_id) references space_stations(id);

alter table sectors add column planet_id int;
alter table sectors add constraint planet_id_fk foreign key (planet_id) references planets(id);

