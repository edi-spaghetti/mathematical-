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
