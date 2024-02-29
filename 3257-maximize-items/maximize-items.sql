# Write your MySQL query statement below
with prime as 
(
    select item_type,
    case when 500000>sum(square_footage) then floor(500000/sum(square_footage))*count(*)
         else count(*) end as item_count,
    case when 500000>sum(square_footage) then floor(500000/sum(square_footage))*sum(square_footage)
         else 500000 end as total_square_footage
    from inventory where item_type='prime_eligible'
),
notprime as 
(
    select item_type,
          floor((500000-(select total_square_footage from prime))/sum(square_footage))*count(*) as item_count
    from inventory
    where item_type='not_prime'
)
select item_type,item_count from prime
UNION ALL
select item_type,item_count from notprime 
order by item_count desc 
