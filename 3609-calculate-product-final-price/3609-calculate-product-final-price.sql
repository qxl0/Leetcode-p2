# Write your MySQL query statement below
select a.product_id, a.price*(1-ifnull(b.discount,0.0)/100) as final_price,  a.category
from products a left join discounts b on a.category=b.category
order by a.product_id asc