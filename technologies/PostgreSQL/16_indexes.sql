/*
Lesson 16: Database Indexes and Query Optimization.

Mission Scenario:
The fleet dispatch system frequently queries the fleet inventory by specific vessel models 
to counter emergent threats. To avoid catastrophic Full Table Scans (Seq Scan) as the fleet 
scale grows, we implement a B-Tree index on the 'model' column of the 'ships' table, 
accelerating exact-match search lookups.

Visualizing Index and Base Table Relationship:
+------------------------------------+      +------------------------------------------+
|       SHIPS_MODEL_IDX (B-TREE)     |      |               SHIPS TABLE                |
+--------------------+---------------+      +----+---------------+-------+------------+
| Model (Sorted)     | Pointer (ctid)| ===> | id | model         | speed | courier_id |
+--------------------+---------------+      +----+---------------+-------+------------+
| Hyperion Star      | (page=0,line=1)|      |  1 | Hyperion Star |   450 |          3 |
| Kodiak-XL          | (page=0,line=3)|      |  2 | Stormbringer  |   600 |          2 |
| Stormbringer       | (page=0,line=2)|      |  3 | Kodiak-XL     |   300 |          3 |
+--------------------+---------------+      +----+---------------+-------+------------+

Key Concepts:
- Index Scan vs Seq Scan: An index provides an ordered companion structure allowing the database 
  engine to perform binary-style node traversal instead of reading the entire table row-by-row.
- Write Penalty: While indexes drastically improve read performance, they introduce overhead 
  on data modification statements (INSERT, UPDATE, DELETE) since the tree structure must 
  re-balance itself to maintain sorted node constraints.
*/


drop index if exists ships_model_idx;

create index ships_model_idx 
on ships(model);
