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

The definition for bi-partite is that nodes can be partitioned into two subsets of nodes,
:math:`V_L` and :math:`V_R`, where :math:`V = V_L \cup V_R`,
so that all edges connect a node in :math:`V_L` to a node in :math:`V_R` (or vice versa).

Suppose this is our graph, :math:`G = (V, E)`

.. graph:: G
	:align: center

	A -- B
	A -- D
	C -- B
	C -- D
	E -- D

Now let two matchings of G be defined as,

.. math::

	M_1 = \{A—B, C—D\}

	M_2 = \{A—D, C—D\}

Note in both cases, we can't have :math:`E—D` because both matchings already have D connected to other nodes.
By the question, no two edges in M are incident on a common vertex.

This then creates our :math:`\ G' = (V, M_1 \cup M_2)`,

.. math::

.. graph:: G
	:align: center

	A -- B
	A -- D
	C -- B
	C -- D
	E

But then, how can this graph be bipartite if E is connected by no edges?
No matter how we partition the nodes, E will never connect to a node in the other partition.

So G is not always bi-partite.

.. note::

	Either I've misunderstood something or there's something wrong with this question.
	Regardless, I don't know how else to answer it with the information provided.


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
When we count the degree of :math:`v_a` we get :math:`d_a`, which includes the edge :math:`{v_a—v_b}`
When we come to count the degree of :math:`v_b` we get :math:`d_b`, and this includes the edge :math:`{v_b—v_a}`.

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