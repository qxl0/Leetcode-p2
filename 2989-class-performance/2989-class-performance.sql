# Write your MySQL query statement below
with cte as (
    select student_id,assignment1+assignment2+assignment3 as totalscore
    from scores
)
select max(totalscore)-min(totalscore) as difference_in_score
from cte