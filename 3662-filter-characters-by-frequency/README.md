<h2><a href="https://leetcode.com/problems/filter-characters-by-frequency">3662. Filter Characters by Frequency</a></h2><h3>Easy</h3><hr><p>You are given a string <code>s</code> consisting of lowercase English letters and an integer <code>k</code>.</p>

<p>Your task is to construct a new string that contains only those characters from <code>s</code> which appear <strong>fewer</strong> than <code>k</code> times in the entire string. The order of characters in the new string must be the <strong>same</strong> as their <strong>order</strong> in <code>s</code>.</p>

<p>Return the resulting string. If no characters qualify, return an empty string.</p>

<p>Note: <strong>Every occurrence</strong> of a character that occurs fewer than <code>k</code> times is kept.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;aadbbcccca&quot;, k = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;dbb&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>Character frequencies in <code>s</code>:</p>

<ul>
	<li><code>&#39;a&#39;</code> appears 3 times</li>
	<li><code>&#39;d&#39;</code> appears 1 time</li>
	<li><code>&#39;b&#39;</code> appears 2 times</li>
	<li><code>&#39;c&#39;</code> appears 4 times</li>
</ul>

<p>Only <code>&#39;d&#39;</code> and <code>&#39;b&#39;</code> appear fewer than 3 times. Preserving their order, the result is <code>&quot;dbb&quot;</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;xyz&quot;, k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;xyz&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>All characters (<code>&#39;x&#39;</code>, <code>&#39;y&#39;</code>, <code>&#39;z&#39;</code>) appear exactly once, which is fewer than 2. Thus the whole string is returned.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
	<li><code>1 &lt;= k &lt;= s.length</code></li>
</ul>
