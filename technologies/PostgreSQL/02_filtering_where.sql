/*
Lesson 2: Advanced Row Filtering, Logical Predicates, and Pattern Matching.

This module demonstrates complex row filtration techniques using the PostgreSQL 'where' clause.
It highlights the execution order of conditional operators, strict type-matching for temporal 
data (dates), and safe evaluation of Boolean logic (AND, OR, NOT) to prevent record leakage.

Key Concepts:
- Set Inclusion via 'in': Utilizing discrete lists for internal schema evaluation, replacing 
  verbose and inefficient chains of 'or' statements.
- Range Bound Filtering ('between'): Performing inclusive temporal slicing on date objects 
  without incurring type-casting errors.
- Wildcard Pattern Constraints ('like'): Enforcing suffix validation using the '%' wildcard 
  and segregating conditions via explicit operator precedence brackets '()'.
- Inversion Filtering ('not like'): Implementing exclusive logical filters to strip specific 
  substring occurrences from the final output array.

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
*/

select ship_name, registry_code, commission_date
from space_ships 
where class_type in ('Cruiser', 'Stealth', 'Explorer') 
  and commission_date between '2021-01-01' and '2024-12-31'
  and (registry_code like '%X' or registry_code like '%A')
  and ship_name not like '%Shadow%';