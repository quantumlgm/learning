/*
Lesson 19 (Practice): Combining Datasets with UNION ALL.

Mission Scenario:
The dispatch center requires a unified registry of all physical assets in space 
(both moving ships and static space stations). To prevent data loss, we must preserve 
all entries (even if naming collisions occur) and present them in a single, 
alphabetically sorted catalog.

Key SQL Rule Discovered:
In UNION/UNION ALL operations, the very first SELECT statement establishes the schema 
and column names for the entire output. Subsequent SELECTs must match this structure 
and will have their columns implicitly renamed to match the first query's alias (e.g., 'obj').

Visualizing UNION ALL (Vertical Stacking):
[SELECT 1: ships]           ──►  (obj: "Hyperion",   type: "space_ship")
                                        │
                                  ( UNION ALL )  -- Vertical append
                                        │
[SELECT 2: space_stations]  ──►  (obj: "Sector 4",   type: "space_station")
                                        │
[FINAL RESULT]              ──►  Ordered alphabetically by 'obj'
*/

select s.model as obj, 'space_ship' as type from ships s
union all
select ss.station_name as obj, 'space_station' as type from space_stations ss
order by obj;