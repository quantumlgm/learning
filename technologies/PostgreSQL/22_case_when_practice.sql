/*
Lesson 22: Conditional Logic with CASE WHEN.

Mission Scenario:
The syndicate's financial department is introducing a progressive tax (duty) 
on cargo based on its weight. We need to categorize orders and calculate 
the duty in credits, but only for orders delivered by space stations.

Logic of CASE WHEN:
Works like an if-elif-else block in Python. It evaluates conditions sequentially 
and returns the value for the first true condition.

Why we can't reference 'weight_category' in the second CASE:
The SQL engine processes all expressions in the SELECT clause simultaneously. 
Therefore, 'weight_category' does not exist yet when 'due' is being calculated. 
We must either repeat the condition or use a CTE.
*/

select 
	o.id, 
	o.weight,
	case
		when o.weight > 10 then 'Heaavy' 
		when o.weight >= 5 then 'Medium'
		else 'Light'
	end as weight_category,
	case 
		when o.weight > 10 then 500
		when o.weight >= 5 then 250
		else 100
	end as due
from orders o
where station_id is not null
order by o.weight desc
