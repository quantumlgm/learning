/*
Lesson 1: Data Retrieval Fundamentals, Column Aliasing, and Output Constraints.

This module demonstrates the core mechanics of the SQL SELECT statement using PostgreSQL.
It highlights the architectural practice of selective column projection over wildcard 
retrieval, mitigating network overhead and enforcing data encapsulation layers.

Key Concepts:
- Explicit Column Projection: Isolating specific attributes ('ship_name', 'class_type', 
  'crew_capacity') to optimize query performance and memory allocation.
- Column Aliasing via 'AS': Decoupling internal database schema nomenclature from 
  application-layer requirements by restructuring result-set headers ('vessel_name', 'max_crew').
- Result-Set Cardinality Limiting: Utilizing the 'LIMIT' clause to truncate row outputs, 
  serving as the foundational backend mechanic for dataset pagination and buffering.

  Working Table: 'space_ships' 
+----+-----------+-------------+-------------+---------------+----------------+
| id | ship_name | class_type  | warp_rating | crew_capacity | status         |
+----+-----------+-------------+-------------+---------------+----------------+
| 1  | Hyperion  | Cruiser     | 8.5         | 120           | Active         |
| 2  | Vanguard  | Dreadnought | 6.2         | 450           | Active         |
| 3  | Shadow    | Stealth     | 9.1         | 12            | Maintenance    |
| 4  | Starlight | Explorer    | 7.8         | 45            | Active         |
| 5  | Behemoth  | Dreadnought | 5.0         | 600           | Decommissioned |
| 6  | Zephyr    | Stealth     | 9.4         | 15            | Active         |
| 7  | Aurora    | Explorer    | 8.2         | 50            | Active         |
+----+-----------+-------------+-------------+---------------+----------------+
*/

SELECT ship_name AS vessel_name, class_type, crew_capacity AS max_crew
FROM space_ships
LIMIT 4;