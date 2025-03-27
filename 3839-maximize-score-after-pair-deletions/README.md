<h2><a href="https://leetcode.com/problems/maximize-score-after-pair-deletions">3839. Maximize Score After Pair Deletions</a></h2><h3>Medium</h3><hr><p>You are given an array of integers <code>nums</code>. You <strong>must</strong> repeatedly perform one of the following operations while the array has more than two elements:</p>

<ul>
	<li>Remove the first two elements.</li>
	<li>Remove the last two elements.</li>
	<li>Remove the first and last element.</li>
</ul>

<p>For each operation, add the sum of the removed elements to your total score.</p>

<p>Return the <strong>maximum</strong> possible score you can achieve.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,4,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">6</span></p>

<p><strong>Explanation:</strong></p>

<p>The possible operations are:</p>

<ul>
	<li>Remove the first two elements <code>(2 + 4) = 6</code>. The remaining array is <code>[1]</code>.</li>
	<li>Remove the last two elements <code>(4 + 1) = 5</code>. The remaining array is <code>[2]</code>.</li>
	<li>Remove the first and last elements <code>(2 + 1) = 3</code>. The remaining array is <code>[4]</code>.</li>
</ul>

<p>The maximum score is obtained by removing the first two elements, resulting in a final score of 6.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [5,-1,4,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">7</span></p>

<p><strong>Explanation:</strong></p>

<p>The possible operations are:</p>

<ul>
	<li>Remove the first and last elements <code>(5 + 2) = 7</code>. The remaining array is <code>[-1, 4]</code>.</li>
	<li>Remove the first two elements <code>(5 + -1) = 4</code>. The remaining array is <code>[4, 2]</code>.</li>
	<li>Remove the last two elements <code>(4 + 2) = 6</code>. The remaining array is <code>[5, -1]</code>.</li>
</ul>

<p>The maximum score is obtained by removing the first and last elements, resulting in a total score of 7.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>
