[Discussion Post (created on 6/11/2021 at 22:23)](https://leetcode.com/problems/longest-happy-prefix/discuss/1615098/Bruteforce)  
<h2>1392. Longest Happy Prefix</h2><h3>Hard</h3><hr><div><p>A string is called a <strong>happy prefix</strong> if is a <strong>non-empty</strong> prefix which is also a suffix (excluding itself).</p>

<p>Given a string <code>s</code>, return <em>the <strong>longest happy prefix</strong> of</em> <code>s</code>. Return an empty string <code>""</code> if no such prefix exists.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> s = "level"
<strong>Output:</strong> "l"
<strong>Explanation:</strong> s contains 4 prefix excluding itself ("l", "le", "lev", "leve"), and suffix ("l", "el", "vel", "evel"). The largest prefix which is also suffix is given by "l".
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> s = "ababab"
<strong>Output:</strong> "abab"
<strong>Explanation:</strong> "abab" is the largest prefix which is also suffix. They can overlap in the original string.
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> s = "leetcodeleet"
<strong>Output:</strong> "leet"
</pre>

<p><strong>Example 4:</strong></p>

<pre><strong>Input:</strong> s = "a"
<strong>Output:</strong> ""
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> contains only lowercase English letters.</li>
</ul>
</div>