# Write your MySQL query statement below
with cte as (
    select substring(email, locate('@',email)+1, length(email)) as domain
    from emails
)
select domain as email_domain,count(*) as count from cte where right(domain, 3)='com'
group by domain 
order by 1 asc