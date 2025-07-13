# Write your MySQL query statement below
with cte1 as (
    select employee_id, yearweek(meeting_date,3) as wk, 
    case when sum(duration_hours) > 20 then 1 else 0 end as isheavy
    from meetings
    group by employee_id,yearweek(meeting_date,3)
    
), cte2 as (
    select employee_id, sum(isheavy) as cnt
    from cte1
    group by employee_id    
)

select a.employee_id,b.employee_name,b.department, a.cnt as meeting_heavy_weeks
from cte2 a join employees b on a.employee_id=b.employee_id
where a.cnt >=2
order by 4 desc, 2