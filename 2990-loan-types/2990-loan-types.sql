# Write your MySQL query statement below
select distinct a.user_id
from loans a join loans b on a.user_id=b.user_id
where a.loan_type='Refinance' and b.loan_type='Mortgage'
order by a.user_id