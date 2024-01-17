# Write your MySQL query statement below
with cte as (
    select purchase_date,week(purchase_date)-week('2023-11-01')+1 as week_of_month, weekday(purchase_date) as wkd,amount_spend
    from purchases
),
cte2 as (
    select week_of_month, purchase_date, sum(amount_spend) as total_amount
    from cte
    where wkd=4
    group by week_of_month,purchase_date
    order by 1
)
select * from cte2

