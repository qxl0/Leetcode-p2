<h2><a href="https://leetcode.com/problems/find-expensive-cities/">2987. Find Expensive Cities</a></h2><h3>Easy</h3><hr><div class="sql-schema-wrapper__3VBi"><a class="sql-schema-link__3cEg">SQL Schema<svg viewBox="0 0 24 24" width="1em" height="1em" class="icon__1Md2"><path fill-rule="evenodd" d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"></path></svg></a></div><div><p>Table: <code>Listings</code></p>

<pre>+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| listing_id  | int     |
| city        | varchar |
| price       | int     |
+-------------+---------+
listing_id is column of unique values for this table.
This table contains listing_id, city, and price.
</pre>

<p>Write a solution to find <strong>cities </strong>where the <strong>average home prices</strong> exceed the <strong>national</strong> average home price.</p>

<p>Return <em>the result table sorted by </em><code>city</code><em> in <strong>ascending</strong> order</em><em>.</em></p>

<p>The result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> 
Listings table:
+------------+--------------+---------+
| listing_id | city         | price   | 
+------------+--------------+---------+
| 113        | LosAngeles   | 7560386 | 
| 136        | SanFrancisco | 2380268 |     
| 92         | Chicago      | 9833209 | 
| 60         | Chicago      | 5147582 | 
| 8          | Chicago      | 5274441 |  
| 79         | SanFrancisco | 8372065 | 
| 37         | Chicago      | 7939595 | 
| 53         | LosAngeles   | 4965123 | 
| 178        | SanFrancisco | 999207  | 
| 51         | NewYork      | 5951718 | 
| 121        | NewYork      | 2893760 | 
+------------+--------------+---------+
<strong>Output</strong>
+------------+
| city       | 
+------------+
| Chicago    | 
| LosAngeles |  
+------------+
<strong>Explanation</strong>
The national average home price is $6,122,059.45. Among the cities listed:
- Chicago has an average price of $7,043,706.75
- Los Angeles has an average price of $6,277,754.5
- San Francisco has an average price of $3,900,513.33
- New York has an average price of $4,422,739
Only Chicago and Los Angeles have average home prices exceeding the national average. Therefore, these two cities are included in the output table. The output table is sorted in ascending order based on the city names.

</pre>
</div>