/*
Lesson 3: Multi-Level Result-Set Sorting, Operator Precedence, and Deterministic Ordering.

This module demonstrates advanced record sorting using the PostgreSQL 'order by' clause.
It highlights the architecture of nested, multi-column prioritization and discusses the 
critical backend concept of deterministic pagination—preventing row-shuffling bugs across 
network requests by establishing a fallback alphanumeric sort key.

Working Table: 'space_ships'
+----+-----------------+-------------+-------------+---------------+----------------+-----------------+---------------+
| id | ship_name       | class_type  | warp_rating | crew_capacity | status         | commission_date | registry_code |
+----+-----------------+-------------+-------------+---------------+----------------+-----------------+---------------+
| 1  | Hyperion-X      | Cruiser     | 8.5         | 120           | Active         | 2022-03-15      | NCC-74656-A   |
| 2  | Vanguard Prime  | Dreadnought | 6.2         | 450           | Active         | 2019-11-01      | NX-01-D       |
| 3  | Shadow Strike   | Stealth     | 9.1         | 12            | Maintenance    | 2024-06-20      | SS-999-X      |
| 4  | Starlight E     | Explorer    | 7.8         | 45            | Active         | 2021-08-12      | NCC-1701-E    |
| 5  | Behemoth Heavy  | Dreadnought | 5.0         | 600           | Decommissioned | 2015-05-30      | OLD-888       |
| 6  | Zephyr-X        | Stealth     | 9.4         | 15            | Active         | 2025-01-10      | SS-101-X      |
| 7  | Aurora Borealis | Explorer    | 8.2         | 50            | Active         | 2023-07-04      | NCC-90210-B   |
| 8  | Solaria         | Cruiser     | 7.5         | 95            | Active         | 2020-12-25      | NCC-5543-A    |
+----+-----------------+-------------+-------------+---------------+----------------+-----------------+---------------+

Key Concepts:
- Direct and Inverted Sorting ('asc' / 'desc'): Controlling dataset flow direction, sorting 
  lexicographically backwards for text arrays and numerically backwards for integers.
- Multi-Column Evaluation Hierarchy: Layering conditions sequentially where the secondary sort 
  ('crew_capacity') triggers only if the primary sort values ('class_type') are identical.
- Alphanumeric Tie-Breaking (Determinism): Appending a unique text property ('ship_name') to the 
  end of the 'order by' chain to guarantee invariant output structures across UI re-renders.
- Syntactical Execution Chain: Enforcing strict SQL lifecycle syntax where filtering ('where') 
  mutates the initial pool, sorting reorganizes it, and slicing ('limit') truncates the final stream.
*/

select ship_name, class_type, crew_capacity, warp_rating
from space_ships
where warp_rating > 6 and status = 'Active'
order by class_type desc, crew_capacity desc, ship_name
limit 3;