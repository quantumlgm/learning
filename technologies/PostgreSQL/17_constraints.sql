/*
Lesson 17: Database Constraints (Data Integrity Rules).

Mission Scenario:
To establish a secure corporate registry, we implement a personnel table with built-in 
validation boundaries. The system enforces business logic directly at the database layer: 
preventing anonymous entries, guaranteeing individual communication lines, preventing 
underage labor violations, and establishing a standard starting phase for newcomers.

Visualizing Table Structure and Constraints:
+---------------------------------------------------------------------------------------+
|                              EMPLOYEES_REGISTRATION TABLE                             |
+------------+--------------+-----------------------------------------------------------+
| Column     | Type         | Active Constraints / Rules                                |
+------------+--------------+-----------------------------------------------------------+
| id         | SERIAL       | PRIMARY KEY (Automatic, Unique, Not Null)                 |
| first_name | VARCHAR(255) | NOT NULL (Name is mandatory)                              |
| last_name  | VARCHAR(255) | NOT NULL (Surname is mandatory)                           |
| email      | VARCHAR(255) | UNIQUE [email_unique] (No duplicate accounts)             |
| age        | INT          | CHECK [check_age] (Must be >= 18)                         |
| status     | VARCHAR(255) | DEFAULT 'On probation' (Fallback value if omitted)       |
+------------+--------------+-----------------------------------------------------------+
*/

create table employees_registration (
    id serial primary key,
    first_name varchar(255) not null,
    last_name varchar(255) not null,
    email varchar(255),
    age int,
    status varchar(255) default 'on probation',

    constraint check_age check(age >= 18),
    constraint email_unique unique(email)
);