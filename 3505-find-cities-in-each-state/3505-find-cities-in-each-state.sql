# Write your MySQL query statement below
select state, ltrim(group_concat(concat(' ', city) order by city)) as cities 
from cities 
group by state 
order by state 