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
