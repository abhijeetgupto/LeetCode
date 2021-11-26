<h2>1487. Making File Names Unique</h2><h3>Medium</h3><hr><div><p>Given an array of strings <code>names</code> of size <code>n</code>. You will create <code>n</code> folders in your file system <strong>such that</strong>, at the <code>ith</code> minute, you will create a folder with the name <code>names[i]</code>.</p>

<p>Since two files <strong>cannot</strong> have the same name, if you enter a folder name which is previously used,&nbsp;the system&nbsp;will have a suffix&nbsp;addition to its name in the form of <code>(k)</code>,&nbsp;where,&nbsp;<code>k</code> is the <strong>smallest positive integer</strong> such that the obtained name remains unique.</p>

<p>Return <em>an array of strings of length <code>n</code></em> where <code>ans[i]</code> is the actual name the system will assign to the <code>ith</code> folder when you create it.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> names = ["pes","fifa","gta","pes(2019)"]
<strong>Output:</strong> ["pes","fifa","gta","pes(2019)"]
<strong>Explanation:</strong> Let's see how the file system creates folder names:
"pes" --&gt; not assigned before, remains "pes"
"fifa" --&gt; not assigned before, remains "fifa"
"gta" --&gt; not assigned before, remains "gta"
"pes(2019)" --&gt; not assigned before, remains "pes(2019)"
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> names = ["gta","gta(1)","gta","avalon"]
<strong>Output:</strong> ["gta","gta(1)","gta(2)","avalon"]
<strong>Explanation:</strong> Let's see how the file system creates folder names:
"gta" --&gt; not assigned before, remains "gta"
"gta(1)" --&gt; not assigned before, remains "gta(1)"
"gta" --&gt; the name is reserved, system adds (k), since "gta(1)" is also reserved, systems put k = 2. it becomes "gta(2)"
"avalon" --&gt; not assigned before, remains "avalon"
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> names = ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"]
<strong>Output:</strong> ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece(4)"]
<strong>Explanation:</strong> When the last folder is created, the smallest positive valid k is 4, and it becomes "onepiece(4)".
</pre>

<p><strong>Example 4:</strong></p>

<pre><strong>Input:</strong> names = ["wano","wano","wano","wano"]
<strong>Output:</strong> ["wano","wano(1)","wano(2)","wano(3)"]
<strong>Explanation:</strong> Just increase the value of k each time you create folder "wano".
</pre>

<p><strong>Example 5:</strong></p>

<pre><strong>Input:</strong> names = ["kaido","kaido(1)","kaido","kaido(1)"]
<strong>Output:</strong> ["kaido","kaido(1)","kaido(2)","kaido(1)(1)"]
<strong>Explanation:</strong> Please note that system adds the suffix (k) to current name even it contained the same suffix before.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= names.length &lt;= 5 * 10^4</code></li>
	<li><code>1 &lt;= names[i].length &lt;= 20</code></li>
	<li><code>names[i]</code> consists of lower case English letters, digits and/or round brackets.</li>
</ul></div>