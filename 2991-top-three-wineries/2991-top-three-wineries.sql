# Write your MySQL query statement below
with cte as (
    select distinct country
    from Wineries
),
cte2 as (
    select country,winery,sum(points) as total
    from Wineries group by country    , winery 
),
ranks as (
    select *, row_number() over (partition by country order by total desc, winery asc) as rnk 
    from cte2 
), 
rank1 as (
select country  ,concat_ws(" ",winery, concat("(",total ,")")) as top_winery  
from cte
left join ranks using(country)
where rnk = 1
),
rank2 as (
select country  , case when total is null then 'No second winery' 
                  else concat_ws(" ",winery, concat("(",total ,")")) end as second_winery  
from cte
left join (select * from ranks where rnk=2) temp using(country)
),
rank3 as (
select country  , case when total is null then 'No third winery' 
                  else concat_ws(" ",winery, concat("(",total ,")")) end as third_winery  
from cte
left join (select * from ranks where rnk=3) temp using(country)

)
# select * from rank1
select * from rank1 inner join rank2 using(country) inner join rank3 using(country) order by country

