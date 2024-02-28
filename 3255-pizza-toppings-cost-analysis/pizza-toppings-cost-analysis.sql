# Write your MySQL query statement below
select CONCAT(t1.topping_name, ",", t2.topping_name, ",", t3.topping_name) as pizza, 
    t1.cost+t2.cost+t3.cost as total_cost
from Toppings t1 CROSS JOIN Toppings t2 ON t1.topping_name<t2.topping_name
CROSS JOIN Toppings t3 ON t2.topping_name<t3.topping_name
ORDER BY 2 desc, 1 asc