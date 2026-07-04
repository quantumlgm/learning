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
*/

SELECT ship_name AS vessel_name, class_type, crew_capacity AS max_crew
FROM space_ships
LIMIT 4;