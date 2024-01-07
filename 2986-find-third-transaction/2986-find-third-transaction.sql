# Write your MySQL query statement below
with cte as (
    select user_id,transaction_date,spend,rank() over (partition by user_id order by transaction_date) as rn
    from Transactions
) 
select a.user_id, a.spend as third_transaction_spend, a.transaction_date as third_transaction_date
from cte a join cte p1 on a.user_id=p1.user_id and p1.rn=1
join cte p2 on a.user_id=p2.user_id and p2.rn=2
where a.rn = 3 and p1.spend<a.spend and p2.spend<a.spend
order by a.user_id
