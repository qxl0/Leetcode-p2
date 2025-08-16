# Write your MySQL query statement below
with cte as (
    select a.book_id
    from reading_sessions a join reading_sessions b on a.book_id = b.book_id and 
    a.reader_name <> b.reader_name and ((a.session_rating >=4 and b.session_rating <=2) or
    (a.session_rating<=2 and b.session_rating >=4))    
), 
cte1 as (
    select a.book_id, count(*) as tn, max(session_rating) as hr, min(session_rating) as lr,
    sum(case when session_rating >=4 or session_rating<=2 then 1 else 0 end) as pr
    from reading_sessions a
    where book_id in (select book_id from cte)
    group by book_id
    having tn >=5
), 
cte2 as (
    select book_id, round(pr/tn,2) as polarization_score, hr-lr as rating_spread
    from cte1
)
select b.book_id, b.title, b.author,b.genre,b.pages,a.rating_spread, a.polarization_score
from cte2 a join books b on 
a.book_id = b.book_id
where a.polarization_score>=0.6
order by a.polarization_score desc, b.title desc