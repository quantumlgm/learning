/*
Lesson 15: Database Transactions (ACID Principles).

Mission Scenario:
To safely transfer asset ownership, a courier ('Alex', id=1) relinquishes command of 
the vessel 'Hyperion Star' (id=1) so it can be assigned to another courier ('Marcus', id=3). 
This requires a multi-step operation. We isolate these modifications inside a transaction block 
to guarantee Atomicity: if any step fails, the entire sequence rolls back, preventing 
the ship from being left without an owner.

Visualizing Table State Changes:
+--------------------------------------------------------+
|                      SHIPS TABLE                       |
+----+---------------+-------+------------+--------------+
| id | model         | speed | courier_id | State        |
+----+---------------+-------+------------+--------------+
|  1 | Hyperion Star |   450 |          1 | Initial      |
|  1 | Hyperion Star |   450 |       NULL | Step 1 Done  |
|  1 | Hyperion Star |   450 |          3 | Final Commit |
+----+---------------+-------+------------+--------------+

Key Concepts:
- START TRANSACTION: Initiates a private execution workspace. Changes made here are 
  invisible to other database connections until finalized.
- COMMIT: Permanently flushes all staged modifications within the transaction block to disk.
- ROLLBACK: Discards all operations executed since the START TRANSACTION statement, 
  reverting modified rows to their original state.
*/

start transaction;

update ships 
set courier_id = null 
where id = 1;

update ships 
set courier_id = 3 
where id = 1;

commit;