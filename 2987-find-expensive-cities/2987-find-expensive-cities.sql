# Write your MySQL query statement below
with cte0 as (
    select sum(price)/count(price) as nationalaverge
    from listings
)
,cte as (
    select city, sum(price)/count(city) as average
    from listings
    group by city
)
select city
from cte 
where average > (select nationalaverge from cte0)
order by city