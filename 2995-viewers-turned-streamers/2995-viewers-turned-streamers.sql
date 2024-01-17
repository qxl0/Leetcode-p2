# Write your MySQL query statement below
with cte as (
    select user_id, dense_rank() over(partition by user_id order by session_start) as rk,session_type
    from sessions    
),
cte2 as (
    select user_id
    from cte
    where rk=1 and session_type='Viewer'
),
cte3 as (
    select user_id, count(*) as sessions_count
    from sessions
    where session_type='Streamer' and user_id in (select user_id from cte2)   
    group by user_id 
)
select user_id,sessions_count
from cte3 
order by sessions_count desc,user_id desc
