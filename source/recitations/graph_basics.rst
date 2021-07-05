Graph Basics
============

Let :math:`G = (V, E)` be a graph. Here is a picture of a graph.

.. graph:: G
	:align: center

	A -- B
	A -- C
	B -- D
	D -- C
	C -- E
	E -- F
	E -- G

Recall that the elements of V are called vertices, and those of E are called edges.
In this example the vertices are :math:`\{A, B, C, D, E, F, G\}` and the edges are

.. math::

	\{A—B, B—D, C—D, A—C, E—F, C—E, E—G\}

Deleting some vertices or edges from a graph leaves a subgraph.

Formally, a subgraph of :math:`G = (V, E)` is a graph :math:`G' = (V', E')`,
where :math:`V'` is a nonempty subset of V and :math:`E'` is a subset of E.
Since a subgraph is itself a graph, the endpoints of every edge in :math:`E'` must be vertices in :math:`V'`.
For example, :math:`V' = \{A, B, C, D\}` and :math:`E' = \{A—B, B—D, C—D, A—C\}` forms a subgraph of G.

In the special case where we only remove edges incident to removed nodes,
we say that :math:`G'` is the subgraph induced on :math:`V'` if :math:`E' = \{( x—y \mid x, y \in V' \text{ and } x—y \in E\}`.
In other words, we keep all edges unless they are incident to a node not in :math:`V'`.
For instance, for a new set of vertices :math:`V' = \{A, B, C, D\}`,
the induced subgraph :math:`G'` has the set of edges :math:`E' = \{A—B, B—D, C—D, A—C\}`.

Problem 1
---------

An undirected graph G has **width** w if the vertices can be arranged in a sequence

.. math::

	v_1, v_2, v_3, \dots , v_n

such that each vertex :math:`v_i` is joined by an edge to at most :math:`w` preceding vertices.
(Vertex :math:`v_j` precedes :math:`v_i` if :math:`j < i`.)
Use induction to prove that every graph with width at most :math:`w` is :math:*(w + 1)-colorable*.

(Recall that a graph is k-colorable iff every vertex can be assigned one of k colors so that adjacent vertices get different colors.)

.. raw:: html

	<hr>

Let :math:`P(n)` be the proposition defined as a graph, G, of n vertices, for some positive integer n.
The graph has a width of w (as defined above), for some :math:`w \in \Bbb N_+` where :math:`0 \le w \le n - 1`

**Theorem**: G is *(w + 1)-colourable*

**Base Case**: We start with P(1), because for this class we don't allow empty graphs.
:math:`P(1)` is true because there is one vertex and zero edges (since we don't allow loops), which means w is also zero.
It follows then, that the graph is :math:`w + 1` or 1-colourable.
Which is enough colours for the one vertex, so this proves the base case.

**Inductive Step**: Let G be any *(n+1)-node* graph.
Let w be the width of the graph (as defined above).

If we remove :math:`v_{n+1}` we are left with a graph :math:`G' = (v', e')`.
:math:`G'` has n vertices, so by P(n) we know it can be coloured with :math:`w+1` colours.

The vertex :math:`v_{n+1}` is adjacent to at most w other vertices.
This means w (or less) of the set of w+1 colours are used to colour its adjacent vertices.
Therefore, there exists at least one colour left that can be used to colour :math:`v_{n+1}`.

So G is *(w+1)-colourable*.
:math:`\blacksquare`

Problem 2
---------

A **planar graph** is a graph that can be drawn without any edges crossing.

1. **First, show that any subgraph of a planar graph is planar.**

.. raw:: html

	<hr>

A planar graph, :math:`G = (V, E)` has n nodes, and e edges (none of which cross).
Removing one node, :math:`v_n`, gives us a graph :math:`G' = (V', E')`.
Since :math:`E'` is a sub-set of E, and none of the edges in E cross, then none of the edges in :math:`E'` cross over either.
:math:`\square`

2. **Also, any planar graph has a node of degree at most 5.**
**Now, prove by induction that any planar graph can be colored in at most 6 colors.**

.. raw:: html

	<hr>

**Theorem**: Let P(n) be the predicate that any n-node planar graph, G, is colourable in 6 or less colours.

**Base Case**: P(1) is true, because a 1-node graph is actually 1-colourable, which is less than 6 colours.

**Inductive Step**: We must prove P(n+1) is true, assuming P(n) is true.
For P(n+1) we have an (n+1)-node graph, G.
Removing a node, :math:`v_{n+1}` leaves us with an n-node graph :math:`G'`
By the inductive hypothesis we know an n-node graph is 6 colourable.

In G, :math:`v_{n+1}` is adjacent to at most 5 nodes (by nature of it being a planar graph).
This leaves us with at least 1 colour to use on :math:`v_{n+1}` for a maximum of 6 colours.

By induction we can conclude any n-node planar graph is at most 6-colourable.
:math:`\blacksquare`
