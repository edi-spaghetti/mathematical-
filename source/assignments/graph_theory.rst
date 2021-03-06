.. _graph-theory:

Graph Theory
============

Problem 1
---------

**Let** :math:`\ G = (V, E)\ ` **be a graph.**
**A matching in G is a set** :math:`\ M \subset E\ ` **such that no two edges in M are incident on a common vertex.**

**Let** :math:`\ M_1, M_2\ ` **be two matchings of G.**
**Consider the new graph** :math:`\ G' = (V, M_1 \cup M_2)`
**(i.e. on the same vertex set, whose edges consist of all the edges that appear in either** :math:`\ M_1` **or** :math:`\ M_2` **).**

**Show that** :math:`\ G'\ ` **is bipartite.**

**Helpful definition: A connected component is a subgraph of a graph consisting of some vertex and every node and edge that is connected to that vertex.**

.. raw:: html

	<hr>

Suppose we have two subsets of nodes, :math:`V_L` and :math:`V_R`, where :math:`V = V_L \cup V_R`.
:math:`G'` is bipartite if every node can be added to either :math:`V_L` or :math:`V_R` without sharing an edge with an existing node in that set.

By definition, a matching produces a bipartite graph, because no two edges are incident to a common vertex.
A graph produced from a matching also has a maximum degree of 1, for the same reason.

If :math:`G'` has a degree of 1, then it is trivially bipartite.
So we must show that :math:`G'` is bipartite if it has a degree higher than 1.

**Lemma 1**: :math:`G'` has a maximum degree of 2.

**Proof**: By contradiction.
Suppose we have a node, v, in :math:`G'` incident to edges :math:`e_t` where :math:`\ t > 2`.
By definition of a matching, the vertex (and the edge it is matched with) can appear once and only once per matching.
We also know the edges in :math:`G'` are a union of exactly two matchings.

So, if t is greater than 2, :math:`e_1` and :math:`e_2` could come from :math:`M_1` and :math:`M_2` respectively,
but :math:`e_3` could not come from either, which is a contradiction.

So we can conclude a graph produced from two matchings will have, at most, degree of 2.
:math:`\square`

Next, let's consider the connected component of any node in :math:`G'`.
Suppose we have a node, v, connected by the shortest number of edges to another node, u.
We start by adding v to :math:`V_L`, and for every node in the same component we recursively add every adjacent node to the opposite partition.
This means the number of edges from v to any node in :math:`V_L` will be even, and the number of edges from v to any node in :math:`V_R` will be odd.

A path is bipartite, because each node is present only once, and there are no cycles.
So each node can be grouped by the opposite of its neighbours.

Suppose two adjacent nodes, w and x are both connected to v, forming a cycle :math:`v???...w???x???...v`.

If the parity of :math:`v???..w` and :math:`v???...x` is different,
then by the above, w and x are in opposite partitions, so the cycle is bipartite.

.. note::

	The sum of numbers of opposite parity is odd, plus 1 (for the edge :math:`w???x`),
	meaning this is a cycle of even length.

If the parity of :math:`v???..w` and :math:`v???...x` is the same, then w and x would be in the same partition.
But since they share an edge they can't be added to the same partition, and so the graph cannot be bipartite.

.. note::

	The sum of any two numbers of the same parity is always even.

Since v and w are adjacent, the parity of the number of edges in the the cycle :math:`v???...w???x???...v` is odd.
So we must prove that :math:`G'` cannot have any cycles of odd length.

**Lemma 2**: :math:`G'` cannot have any cycles of odd length

**Proof**: By contradiction.
Assume :math:`G'` has a cycle of length i, where i is an odd number.
Suppose we walk around the cycle. Since the edges in :math:`G'` are a union of matchings,
each step must travel along an edge, e, such that :math:`e_j` and :math:`e_{j+1}` are from the opposite matching,
for some integer :math:`j \in \Bbb Z`.

This is because matchings cannot contain edges connected to a node more than once.
So if a node has more than one edge, they must come from different matchings.

.. note::

	By lemma 1, we know there are at most 2 edges for every node in :math:`G'`.
	So edges are from either :math:`M_1` or :math:`M_2`.

This means, for any :math:`k,m \in \Bbb Z`, if :math:`\ k\ mod\ i\ ` and :math:`\ m\  mod\ i\ ` are both even, then they must come from the same matching.
However, since i is odd, :math:`\ 0\ mod\ i\ ` and :math:`\ i-1\ mod\ i\ ` are both even, which would put two adjacent edges in the same matching.
This is a contradiction, so we can assume there are no cycles of odd length in :math:`G'`
:math:`\square`

By lemma 2, we know :math:`G'` can only be comprised of paths and even cycles, which as we showed, both result in a bipartite graph.
Therefore, :math:`G'` is bipartite.
:math:`\blacksquare!`


Problem 2
---------

**Let** :math:`\ G = (V, E)\ ` **be a graph.**
**Recall that the degree of a vertex** :math:`v \in V\ ` **, denoted** :math:`\ d_v\ ` **, is the number of vertices w such that there is an edge between v and w.**

**(a) Prove that**

.. math::

	2 |E| = \sum_{v \in V} d_v

.. raw:: html

	<hr>

Every edge in a graph connects one node to another.
In all of these examples we are also assuming simple graphs, i.e. no loops or multi-edges.

Let's say one of the nodes in G, :math:`v_a`, is connected by an edge to another node, :math:`v_b`.
When we count the degree of :math:`v_a` we get :math:`d_a`, which includes the edge :math:`{v_a???v_b}`
When we come to count the degree of :math:`v_b` we get :math:`d_b`, and this includes the edge :math:`{v_b???v_a}`.

In this way, each edge is counted twice.
Therefore the sum of all the degrees of :math:`v \in V` is equal to the number of edges multiplied by two.

**(b) At a 6.042 ice cream study session (where the ice cream is plentiful and it helps you study too) 111 students showed up.**
**During the session, some students shook hands with each other**
**(everybody being happy and content with the ice-cream and all).**
**Turns out that the University of Chicago did another spectacular study here,**
**and counted that each student shook hands with exactly 17 other students.**
**Can you debunk this too?**

.. raw:: html

	<hr>

Let :math:`G = (V, E)` be a graph representing the ice cream sticky study shakey handathon session.
Where each node in V represents a student, and each edge in E represents students :math:`v_a` and :math:`v_b` shaking hands with each other.

**Theorem**: There cannot exist a graph where each node in V is connected by 17 edges.

**Proof**: By contradiction.

Suppose each student shook hands with 17 other students.
There are 111 students in total multiplied by 17 students = 1887 hand shakes in total.
But a handshake is reciprocal, so to avoid counting it twice we must divide by 2.
But we can't divide 1887 by 2 because it's an odd number.
This is contradiction, so we can conclude that the theorem holds.
:math:`\blacksquare`

**(c) And on a more dull note, how many edges does** :math:`\ K_n\ ` **, the complete graph on n vertices, have?**

.. raw:: html

	<hr>

In an n-node complete graph, every node is connected to every other node.
Again, we're only considering simple graphs, so no loops or multi-edges.

This means for each node there are :math:`n - 1` edges.
Since there are n nodes, then there are :math:`n \cdot (n - 1)` edges.
However, that would count edges going both ways, so we need to divide by 2,
giving us :math:`{n^2 - n \over 2}`.

**Theorem**: Let P(n) be the predicate, defined as follows,

.. math::

	P(n) ::= \forall n \in N_+.\ |E| = {n^2 - n \over 2}

That is, for any n-node complete graph :math:`G = (V, E)`, the number of edges is calculated as above.

**Base Case**: P(1) is true because, there is only one node and we don't allow loops so there can be zero edges

.. math::

	{1^2 - 1 \over 2} = 0

**Inductive Step**: We must show :math:`P(n + 1)`, assuming :math:`P(n)` is true.
First, if we take out the :math:`(n+1)^{th}` node, and all its edges, we are left with a n-node graph.
By P(n) we can assume how many edges it has.
When we add the :math:`(n+1)^{th}` node back in, it must be connect to all existing nodes to make a complete graph.
There are n existing nodes, so we can calculate the number of edges as,

.. math::

	\begin{aligned}

	|E| &= {n^2 - n \over 2} + n \qquad && \text{ (by inductive hypothesis) } \cr

	&= {n^2 - n \over 2} + {2n \over 2} \qquad && \text{ (multiply to common factor)} \cr

	&= {n^2 - n + 2n \over 2} \cr

	&= {(n+1) \cdot n \over 2} \cr

	\end{aligned}

This proves :math:`P(n+1)`, and so by induction we can assume the hypothesis is true for all :math:`n \in N_+`.
:math:`\blacksquare`

Problem 3
---------

**Two graphs are isomorphic if they are the same up to a relabeling of their vertices (see Definition 5.1.3 in the book).**
**A property of a graph is said to be preserved under isomorphism if whenever G has that property,**
**every graph isomorphic to G also has that property.**
**For example, the property of having five vertices is preserved under isomorphism:**
**if G has five vertices then every graph isomorphic to G also has five vertices.**

**Some properties of a simple graph, G, are described below.**
**Which of these properties is preserved under isomorphism?**

1.  **G has an even number of vertices.**

	.. raw:: html

		<hr>

	Preserved, because isomorphism is a bijection between sets of vertices, so the number of vertices cannot change.
	If the graph has an even number before applying to function, it will have an even number after applying.

2.  **None of the vertices of G is an even integer.**

	.. raw:: html

		<hr>

	Not preserved, because the graph isomorphism could be to simply add one, making it odd.

3.  G has a vertex of degree 3.

	.. raw:: html

		<hr>

	Preserved, because the function applied to each vertex is also applied to each vertex adjacent to it.

4. G has exactly one vertex of degree 3.

	.. raw:: html

		<hr>

	Preserved, for the same reason as in question 3

**Determine which among the four graphs pictured in the Figures are isomorphic.**
**If two of these graphs are isomorphic, describe an isomorphism between them.**
**If they are not, give a property that is preserved under isomorphism such that one graph has the property, but the other does not.**
**For at least one of the properties you choose, prove that it is indeed preserved under isomorphism (you only need prove one of them).**

.. image:: ../images/assignment-4-problem-3-part-b.png
	:align: center

Graphs a and c are isomorphic.

Here is an isomorphism from a to c:

.. math::

	f(1) = 1

	f(2) = 2

	f(3) = 3

	f(4) = 8

	f(5) = 9

	f(6) = 10

	f(7) = 4

	f(8) = 5

	f(9) = 6

	f(10) = 7

To make this a bit more visual, I've labelled these with colours:

.. image:: ../images/assignment-4-problem-3-part-b-coloured.png
	:align: center

Graph b is not isomorphic to any other, because it has a max degree of 4, but the others all have a max degree of 3.

Graph d is not isomorphic to any other because it has a cycle of length 4, but neither a nor b have a cycle of length 4.
(We already showed b is not isomorphic to d because of the max degree).


The formal definition of isomorphism between two graphs G and H is a bijection :math:`\ f\ :\ V(G) \rightarrow V(H)` such that,

.. math::

	\langle u ??? v \rangle \in E(G) \Leftrightarrow \langle f(u) ??? f(v) \in E(H) \rangle

for all :math:`u, v \in V(G)`

This means an isomorphic function is applied to any given node in G to get the corresponding node in H.
It also means the edge between any two nodes in G is also preserved in H.

That is to say, if u is adjacent to v in G, then :math:`f(u)` is adjacent to :math:`f(v)` in H.
This means the number of edges does not increase or decrease while performing the isomorphism.

Since the number of edges does not change, it follows that the max degree must also remain the same.

Problem 4
---------

**Recall that a coloring of a simple graph is an assignment of a color to each vertex such that no two adjacent vertices have the same color.**
**A k-coloring is a coloring that uses at most k colors.**

**False Claim. Let** :math:`\ G\ ` **be a (simple) graph with maximum degree at most** :math:`\ k\ `.
**If** :math:`\ G\ ` **also has a vertex of degree less than** :math:`\ k\ ` **, then** :math:`\ G\ ` **is k-colorable.**

a)  **Give a counterexample to the False Claim when k = 2.**

	.. raw:: html

		<hr>

	.. graph:: counterexample

	    A [style=filled color=blue]
	    B [style=filled color=red]
	    C [style=filled color=green]
	    D [style=filled color=blue]

	    A -- B
	    A -- C
	    C -- D
	    B -- C

	As you can see, maximum degree is 2, and D has a degree less than 2,
	but because we have a cycle A-B-C, the graph is not 2-colourable

b)  **Consider the following proof of the False Claim:**

	**Proof. Proof by induction on the number n of vertices:**

	**Induction hypothesis: P(n) is defined to be: Let G be a graph with n vertices and maximum degree at most k.**
	**If G also has a vertex of degree less than k, then G is k-colorable.**

	**Base case: (n=1) G has only one vertex and so is 1-colorable. So P(1) holds.**

	**Inductive step: We may assume** :math:`\ P(n)`.
	**To prove** :math:`\ P(n + 1)` **, let** :math:`\ G_{n+1}\ ` **be a graph with** :math:`\ n + 1\ ` **vertices and maximum degree at most k.**
	**Also, suppose** :math:`\ G_{n+1}\ ` **has a vertex, v, of degree less than k.**
	**We need only prove that** :math:`\ G_{n+1}\ ` **is k-colorable.**

	**To do this, first remove the vertex** :math:`\ v\ ` **to produce a graph,** :math:`\ G_n\ ` **, with n vertices.**
	**Removing v reduces the degree of all vertices adjacent to v by 1.**
	**So in** :math:`\ G_n\ ` **, each of these vertices has degree less than k.**
	**Also the maximum degree of** :math:`\ G_n\ ` **remains at most k.**
	**So** :math:`\ G_n\ ` **satisfies the conditions of the induction hypothesis P(n).**
	**We conclude that** :math:`\ G_n\ ` **is k-colorable.**

	**Now a k-coloring of** :math:`\ G_n\ ` **gives a coloring of all the vertices of** :math:`\ G_{n+1}` **, except for v.**
	**Since v has degree less than k, there will be fewer than k colors assigned to the nodes adjacent to v.**
	**So among the k possible colors, there will be a color not used to color these adjacent nodes,**
	**and this color can be assigned to v to form a k-coloring of** :math:`\ G_{n+1}`.
	:math:`\square`


	**Identify the exact sentence where the proof goes wrong**

	.. raw:: html

		<hr>

	In :math:`P(n)`, k is assumed but not defined. For an n-node graph, k scales with n, such that k is at most :math:`n-1`,
	because each node can be adjacent to at most :math:`n-1` other nodes (since loops are not allowed in simple graphs).

	This means the base case has not been proved because we don't know what k is.
	If we were assume it was :math:`n-1`, then P(1) would have to prove the graph is 0-colourable, which is impossible.

Problem 5
---------

**Prove or disprove the following claim: for some** :math:`\ n \ge 3\ ` **(n boys and n girls, for a total of 2n people),**
**there exists a set of boys??? and girls??? preferences such that every dating arrangement is stable.**

.. raw:: html

	<hr>

For any set of preferences, there exists at least one unstable matching.

Suppose we have a set of preferences, there exists at least one matching where a boy is matched with a girl
such that the boy is not the girl's least favourite, and the girl is not the boy's least favourite.

Within the same set of preferences, there also exists a matching between the boy with his least favourite and the girl with her least favourite.
The boy and the girl then form a rogue couple because they like each other more than their least favourites.

This matching, then, is not stable, which contradicts the claim that every dating arrangement is stable.

Problem 6
---------

**Let** :math:`\ (s_1, s_2, \dots, s_n)\ ` **be an arbitrarily distributed sequence of the number** :math:`\ 1, 2, \dots, n ??? 1, n`.
**For instance, for** :math:`n = 5`, **one arbitrary sequence could be** :math:`(5, 3, 4, 2, 1)`.

Define the graph :math:`G = (V,E)` **as follows:**

1.  :math:`V = \{v1, v2, \dots, v_n\}`

2. :math:`e = (v_i, v_j ) \in E` **if either:**

	**(a)** :math:`\ j = i + 1, \text{ for } 1 \le i \le n ??? 1`

	**(b)** :math:`\ i = s_k, \text{ and } j = s_{k+1} \text{ for } 1 \le k \le n ??? 1`

(a) **Prove that this graph is 4-colorable for any** :math:`\ (s1, s2, \dots, s_n)`.

	**Hint: First show that a line graph is 2-colorable.**
	**Note that a line graph is defined as follows:**
	**The n-node graph containing n ??? 1 edges in sequence is known as the line graph** :math:`\ L_n`.

	Considering case (a) only, results in a line graph :math:`L_n`.
	:math:`s_1` and :math:`s_n` have a degree of 1, while all nodes in :math:`(s_2, \dots, s_{n-1})` have a degree of 2.

	Since this forms a path, it is 2-colourable, because nodes are either odd or even, which forms two groups.

	When we consider case (b), the graph G has a degree of at most 4.
	For any given item in the sequence, :math:`s_i`, if :math:`s_i - 1` is greater than 0, and earlier in the sequence,
	then :math:`s_i` will be connected to :math:`s_i - 1`.
	If i is greater than 1, then :math:`s_{i-1}` will also be connected, because :math:`s_i` is not the first item of the sequence.
	By symmetry, edges are also added if :math:`s_i + 1` is less than :math:`s_i`, or if :math:`i+1 \le n` (i.e. we haven't reached the end of the sequence)

	In other words, up to 2 edges are added each for numerical and sequential ordering.

	So when we added edges by sequential ordering, there are at most 3 existing edges.
	Up to 2 from the numerical ordering, and 1 from :math:`v_{s_k}`.
	Therefore we need at most 1 more colour to colour :math:`v_{s_{k+1}}`, making 4 colours.

(b) **Suppose** :math:`\ (s_1, s_2, \dots, s_n) = (1, a_1, 3, a_2, 5, a_3, ...)\ ` **where** :math:`\ a_1, a_2\ ` **is an arbitrary distributed sequence of the even numbers in** :math:`\ 1, \dots, n ??? 1`.
	**Prove that the resulting graph is 2-colorable.**

	By case (b) we add one edge by sequential ordering, resulting in a line graph.

	Then for each number in numerical order, it must be an odd number of places away in the sequence (due to how the sequence is structured).
	Therefore the edge added by numerical ordering creates a loop of even length (odd + 1 = even).

	As we've shown in problem 1, a graph with only cycles of an even length is bipartite, and therefore 2-colourable.
