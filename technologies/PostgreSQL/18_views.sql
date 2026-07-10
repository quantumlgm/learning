/*
Lesson 18: Database Views and Materialized Views.

Mission Scenario:
To comply with security and architecture patterns, we create two view types:
1. 'ships_view' (Standard View): Acts as a security mask, hiding technical metrics 
   (like speed) from non-engineering personnel. It computes dynamically on every call.
2. 'sectors_m_view' (Materialized View): Caches sector mappings to disk for rapid reading. 
   Requires explicit manual lifecycle synchronization to pull changes from underlying tables.

Visualizing Architecture:
[Base Tables: ships, sectors] --(Changes occur inside)
       │
       ├─► ships_view (Virtual Filter) ──► Reads base table live on every SELECT
       │
       └─► sectors_m_view (Physical Snapshot) ──► Frozen on disk until REFRESH is called
*/

-- Standard View 
create view ships_view(id, courier_id, model) as 
select id, courier_id, model 
from ships;

-- Materialized View 
create materialized view sectors_m_view(id, sector_code, planet_id) as 
select id, sector_code, planet_id 
from sectors;

refresh materialized view sectors_m_view;