<h2><a href="https://leetcode.com/problems/maximum-weight-in-two-bags">3647. Maximum Weight in Two Bags</a></h2><h3>Medium</h3><hr><p>You are given an integer array <code>weights</code> and two integers <code>w1</code> and <code>w2</code> representing the <strong>maximum</strong> capacities of two bags.</p>

<p>Each item may be placed in <strong>at most</strong> one bag such that:</p>

<ul>
	<li>Bag 1 holds <strong>at most</strong> <code>w1</code> total weight.</li>
	<li>Bag 2 holds <strong>at most</strong> <code>w2</code> total weight.</li>
</ul>

<p>Return the <strong>maximum</strong> total weight that can be packed into the two bags.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">weights = [1,4,3,2], w1 = 5, w2 = 4</span></p>

<p><strong>Output:</strong> <span class="example-io">9</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Bag 1: Place <code>weights[2] = 3</code> and <code>weights[3] = 2</code> as <code>3 + 2 = 5 &lt;= w1</code></li>
	<li>Bag 2: Place <code>weights[1] = 4</code> as <code>4 &lt;= w2</code></li>
	<li>Total weight: <code>5 + 4 = 9</code></li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">weights = [3,6,4,8], w1 = 9, w2 = 7</span></p>

<p><strong>Output:</strong> <span class="example-io">15</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Bag 1: Place <code>weights[3] = 8</code> as <code>8 &lt;= w1</code></li>
	<li>Bag 2: Place <code>weights[0] = 3</code> and <code>weights[2] = 4</code> as <code>3 + 4 = 7 &lt;= w2</code></li>
	<li>Total weight: <code>8 + 7 = 15</code></li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">weights = [5,7], w1 = 2, w2 = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>No weight fits in either bag, thus the answer is 0.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= weights.length &lt;= 100</code></li>
	<li><code>1 &lt;= weights[i] &lt;= 100</code></li>
	<li><code>1 &lt;= w1, w2 &lt;= 300</code></li>
</ul>
