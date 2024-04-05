# Write your MySQL query statement below
with recursive TweetCTE as (
    SELECT REGEXP_SUBSTR(tweet, '#[a-zA-Z0-9_]+') AS hashtag,
           REGEXP_REPLACE(tweet, '#[a-zA-Z0-9_]+', '',1,1) AS tweet
    FROM tweets
  where tweet_date between "2024-02-01" AND "2024-02-29"
  UNION ALL
  SELECT REGEXP_SUBSTR(tweet, '#[a-zA-Z0-9_]+') AS hashtag,
         REGEXP_REPLACE(tweet, '#[a-zA-Z0-9_]+', '',1,1) AS tweet
  FROM TweetCTE
  WHERE hashtag is not null
)
select hashtag,count(*) as count    
from TweetCTE
where hashtag is not null
group by hashtag 
order by 2 desc, hashtag desc 
limit 3