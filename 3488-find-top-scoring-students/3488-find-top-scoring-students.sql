# Write your MySQL query statement below
with cte as (
    select a.student_id, a.major, b.course_id
    from students a join enrollments b on a.student_id=b.student_id
    join courses c on b.course_id=c.course_id 
    where b.grade='A' and a.major=c.major
    order by a.student_id
),
cte2 as (
    select student_id, major,  count(*) over (partition by student_id) as totalcourses 
    from cte    
    order by student_id
)
select distinct student_id
from cte2 c
where totalcourses = (select count(*) from courses where major=c.major)