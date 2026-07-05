/*
Lesson 1: Data Retrieval Fundamentals, Column Aliasing, and Output Constraints.

Mission Scenario:
You are building an analytical dashboard for a space RPG game. The UI team asks for a 
list of the first 4 ships added to the system. To save network bandwidth, you must select 
only specific columns and rename them to match the new frontend design requirements.

Working Table: 'space_ships'
+----+-----------+-------------+-------------+---------------+----------------+
| id | ship_name | class_type  | warp_rating | crew_capacity | status         |
+----+-----------+-------------+-------------+---------------+----------------+
| 1  | Hyperion  | Cruiser     | 8.5         | 120           | Active         |
| 2  | Vanguard  | Dreadnought | 6.2         | 450           | Active         |
| 3  | Shadow    | Stealth     | 9.1         | 12            | Maintenance    |
| 4  | Starlight | Explorer    | 7.8         | 45            | Active         |
+----+-----------+-------------+-------------+---------------+----------------+

Key Concepts:
- Selective Projection: Listing specific columns instead of using 'SELECT *'. This makes 
  queries faster and saves server memory.
- Column Aliasing ('as'): Renaming columns on the fly (e.g., 'ship_name' to 'vessel_name') 
  to match frontend API expectations.
- Output Limiting ('limit'): Restricting the number of rows returned by the database. 
  This is the main tool for creating page-by-page data views (pagination).
*/

SELECT ship_name AS vessel_name, class_type, crew_capacity AS max_crew
FROM space_ships
LIMIT 4;