/*
Lesson 13: Multi-Table JOINs and Data Merging.

Mission Scenario:
Due to a sudden spike in pirate activity, the logistics syndicate has issued an emergency 
evacuation order for all cargo heading toward the 'Alpha-01' sector. We must perform a 
double JOIN sequence starting from the core transactional records (orders), bridging through 
the destination endpoints (space_stations), and terminating at the geographical boundaries (sectors) 
to isolate and secure high-risk shipments.

Expected Query Output Reference:
+----+--------+---------------+-------------+
| id | weight | station_name  | sector_code |
+----+--------+---------------+-------------+
|  1 | 15.500 | Deep Space 9  | Alpha-01    |
|  2 | 120.000| Omega Outpost | Alpha-01    |
+----+--------+---------------+-------------+

Key Concepts:
- Linear Join Path: When navigating normalized hierarchies, you cannot jump directly 
  from the bottom (orders) to the top (sectors) without declaring the intermediate bridge 
  relationship (space_stations).
- Casing Sensitivity: Text filtering inside the WHERE clause is strictly case-sensitive 
  by default in many relational engines, requiring exact literal string matches ('Alpha-01').
*/

SELECT 
    o.id AS order_id, 
    o.weight AS order_weight, 
    ss.station_name, 
    s.sector_code
FROM orders AS o
JOIN space_stations AS ss ON o.station_id = ss.id
JOIN sectors AS s ON s.id = ss.sector_id
WHERE s.sector_code = 'Alpha-01';