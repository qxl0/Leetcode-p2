# Write your MySQL query statement below
select CONCAT("#", SUBSTRING_INDEX(SUBSTRING_INDEX(tweet, "#", -1), " ", 1)) as hashtag,count(*) as hashtag_count 
from tweets 
where tweet_date between "2024-02-01" AND "2024-02-29"
group by hashtag 
order by 2 desc, hashtag desc 
limit 3