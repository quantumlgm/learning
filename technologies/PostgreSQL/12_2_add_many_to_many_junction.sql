/*
Lesson 12.2: Implementing Many-to-Many (N:M) Relationships via Junction Tables.

Mission Scenario:
To map dynamic relationships where entities on both sides can have multiple associations, 
we introduce a bridge architecture. Couriers can obtain numerous distinct Qualifications, 
and a single Qualification can be shared by many Couriers. Since relational engines 
cannot connect N:M directly, we implement a centralized Junction Table holding composite 
Foreign Keys that map back to each respective master catalog.

Working Architecture State (Many-to-Many Resolution):
+-----------------+              +-------------------------+              +-----------------+
|    couriers     | (1)------>(N)|  courier_qualifications |(N)<-------(1) |  qualifications |
+-----------------+              +-------------------------+              +-----------------+
| id (PK, serial) |              | courier_id (FK, int)    |              | id (PK, serial) |
| first_name      |              | qualification_id (FK)   |              | name            |
+-----------------+              +-------------------------+              +-----------------+

Key Concepts:
- Junction / Pivot Table: A standalone table dedicated exclusively to resolving N:M bonds 
  by breaking them down into two separate 1:N connections pointing inward.
- Strict Type Alignment: The tracking attributes inside the intersection record must use 
  the 'int' data type to perfectly correspond with the 'serial' auto-incrementing 
  Primary Keys of the parent dimensions.
*/

drop table if exists qualifications cascade;
create table qualifications (
	id serial primary key,
	name varchar(512)
);

drop table if exists courier_qualifications cascade;
create table courier_qualifications (
	courier_id int,
	qualification_id int,

	constraint courier_id_fk foreign key (courier_id) references couriers(id),
	constraint qualification_id_fk foreign key (qualification_id) references qualifications(id)
);
