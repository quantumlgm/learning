/*
Lesson 2: Advanced Row Filtering, Logical Predicates, and Pattern Matching.

Mission Scenario:
The Space Security Service is running a fleet audit. You need to find all ships that 
belong to Cruiser, Stealth, or Explorer classes, were built between 2021 and 2024, 
and have registry codes ending with the letters 'A' or 'X'. Finally, you must exclude 
any ships that contain the word 'Shadow' in their name for security reasons.

Working Table: 'space_ships'
+----+-----------------+-------------+-------------+---------------+----------------+-----------------+---------------+
| id | ship_name       | class_type  | warp_rating | crew_capacity | status         | commission_date | registry_code |
+----+-----------------+-------------+-------------+---------------+----------------+-----------------+---------------+
| 1  | Hyperion-X      | Cruiser     | 8.5         | 120           | Active         | 2022-03-15      | NCC-74656-A   |
| 4  | Starlight E     | Explorer    | 7.8         | 45            | Active         | 2021-08-12      | NCC-1701-E    |
| 7  | Aurora Borealis | Explorer    | 8.2         | 50            | Active         | 2023-07-04      | NCC-90210-B   |
| 8  | Solaria         | Cruiser     | 7.5         | 95            | Active         | 2020-12-25      | NCC-5543-A    |
+----+-----------------+-------------+-------------+---------------+----------------+-----------------+---------------+

Key Concepts:
- List Filtering ('in'): Checking if a value matches any item in a specific list, 
  which is cleaner than writing multiple 'OR' conditions.
- Range Filtering ('between'): Selecting values within a specific start and end point, 
  ideal for date and time checks.
- Text Patterns ('like'): Finding rows based on string search rules. The '%' symbol 
  works as a wildcard (e.g., '%A' means 'ends with A').
- Logic Brackets '()': Grouping search conditions together so the database reads 
  'AND' and 'OR' logic in the correct order.
*/

select ship_name, registry_code, commission_date
from space_ships 
where class_type in ('Cruiser', 'Stealth', 'Explorer') 
  and commission_date between '2021-01-01' and '2024-12-31'
  and (registry_code like '%X' or registry_code like '%A')
  and ship_name not like '%Shadow%';