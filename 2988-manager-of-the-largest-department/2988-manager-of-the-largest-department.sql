# Write your MySQL query statement below
with cte as (
    select dep_id,count(*) as numemployee
    from employees
    group by dep_id    
), 
cte2 as (
    select dep_id
    from cte 
    where numemployee = (select max(numemployee) from cte)    
)
select e.emp_name as manager_name, e.dep_id
from employees e join cte2 c on e.dep_id=c.dep_id
where e.position = 'Manager'
order by e.dep_id
