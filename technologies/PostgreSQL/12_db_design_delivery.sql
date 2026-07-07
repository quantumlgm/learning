/*
Lesson 12: Relational Database Architecture and DDL Schema Design.

Mission Scenario:
The Interplanetary Logistics Syndicate requires a robust, relational schema to track 
cargo shipments across the galaxy. We need to construct a bulletproof database design 
where Planets and Couriers act as independent master entities. Space Ships must be 
assigned to specific Couriers (1:N relationship), and the Central Orders table will 
serve as the core junction, ensuring every parcel is strictly linked to a valid 
Space Ship and a destination Planet via Foreign Key constraints.

Database Architecture Reference (Entity-Relationship State):
+-----------------+        +-----------------+
|     courier     |        |     planet      |
+-----------------+        +-----------------+
| id (PK)         |        | id (PK)         |
| first_name      |        | name            |
+--------+--------+        +--------+--------+
         |                          |
         | 1:N                      | 1:N
         v                          |
+--------+--------+                 |
|      ship       |                 |
+-----------------+                 |
| id (PK)         |                 |
| courier_id (FK) |                 |
+--------+--------+                 |
         |                          |
         | 1:N                      v
         |                  +-------+---------+
         +----------------->|     orders      |
                            +-----------------+
                            | id (PK)         |
                            | ship_id (FK)    |
                            | planet_id (FK)  |
                            | weight, type    |
                            +-----------------+

Key Concepts:
- Primary Key (PK) vs Foreign Key (FK): A Primary Key uniquely identifies a row in a 
  master table. A Foreign Key is a pointer column created strictly inside a child 
  table (the "Many" side) that references a Primary Key in a parent table (the "One" side).
- Dependency Rule: Parent tables (courier, planet) must be created first because they 
  can exist independently. Child tables (ship, orders) cannot hold records pointing to 
  non-existent parents, preventing orphaned or invalid delivery data.
*/

drop table if exists planet cascade;
create table planet (
	id serial primary key,
	name varchar(100)	
);

drop table if exists courier cascade;
create table courier (
	id serial primary key,
	first_name varchar(100),
	last_name varchar(100),
	phone_number varchar(100)
);

drop table if exists ship cascade;
create table ship (
	id serial primary key,
	courier_id int,
	model varchar(100),
	speed int,

	constraint courier_id_fk foreign key (courier_id) references courier(id)
);

drop table if exists orders cascade;
create table orders (
	id serial primary key,
	ship_id int,
	planet_id int,
	weight decimal(10, 3),
	order_data timestamp,
	type varchar(255),

	constraint ship_id_fk foreign key (ship_id) references ship(id),
	constraint planet_id_fk foreign key (planet_id) references planet(id)
)