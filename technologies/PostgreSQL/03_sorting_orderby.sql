/*
Lesson 3: Multi-Level Result-Set Sorting, Operator Precedence, and Deterministic Ordering.

Mission Scenario:
A cosmic storm is coming, and the fleet needs an emergency evacuation list. You need to find 
active ships with a warp rating above 6.0. The list must be sorted by ship class backwards, 
then by the largest crew capacity. If ships have identical classes and capacity, sort them 
by name alphabetically so the UI list stays stable and never jumps around.

Working Table: 'space_ships'
+----+-----------------+-------------+-------------+---------------+----------------+-----------------+---------------+
| id | ship_name       | class_type  | warp_rating | crew_capacity | status         | commission_date | registry_code |
+----+-----------------+-------------+-------------+---------------+----------------+-----------------+---------------+
| 1  | Hyperion-X      | Cruiser     | 8.5         | 120           | Active         | 2022-03-15      | NCC-74656-A   |
| 4  | Starlight E     | Explorer    | 7.8         | 45            | Active         | 2021-08-12      | NCC-1701-E    |
| 6  | Zephyr-X        | Stealth     | 9.4         | 15            | Active         | 2025-01-10      | SS-101-X      |
+----+-----------------+-------------+-------------+---------------+----------------+-----------------+---------------+

Key Concepts:
- Sort Direction ('asc' / 'desc'): Sorting data from smallest to largest ('asc') 
  or from largest to smallest ('desc').
- Multi-Column Sort: Sorting by multiple columns at once. The database sorts by the 
  first column, and uses the second column only if there is a tie.
- Deterministic Sort: Adding a unique column (like ship name or ID) to the end of the 
  sort chain. This guarantees that the list always looks exactly the same on every page refresh.
- SQL Order of Words: SQL queries must follow a strict order: SELECT -> FROM -> WHERE -> ORDER BY -> LIMIT.
*/

select ship_name, class_type, crew_capacity, warp_rating
from space_ships
where warp_rating > 6 and status = 'Active'
order by class_type desc, crew_capacity desc, ship_name
limit 3;