More Graph Theory
=================


Problem 1
---------

Recall that a tree is a connected acyclic graph.
In particular, a single vertex is a tree.
We define a Splitting Binary Tree, or SBTree for short, as either the lone vertex, or a tree with the following properties:

	1. exactly one node of degree 2 (called the root).

	2. every other node is of degree 3 or 1 (called internal nodes and leaves, respectively).

For the case of one single vertex (see above), that vertex is considered to be a leaf.


**(a) Show if an SBTree has more than one vertex, then the induced subgraph obtained by removing the unique root consists of two disconnected SBTrees.**
**You may assume that by removing the root you obtain two separate connected components,**
**so all you need to prove is that those two components are SBTrees.**

.. raw:: html

	<hr>

An SBTree is a recursive structure that has one transition, split.
Split can only be applied to nodes with at most one edge.
Suppose we have a node, n, that we apply the split transition to.

.. graph:: split_before
	:align: center

	r [style=invis]
	n [color=lightblue style=filled]

	r -- n [style=dotted]

Notice that n may or may not be connected to another node at a level higher.
This is because if n is the root node, then no such edge exists, but the split transition can still be applied to it.

The split transition adds 2 new nodes to the graph, o and p,
and then adds an edge between them and n.

.. graph:: split_after
	:align: center

	r [style=invis]
	n [color=lightblue style=filled]
	o, p [color=indianred style=filled]

	r -- n [style=dotted]
	n -- o
	n -- p

If n was the root node, then the dotted edge does not exist, and it now has a degree of 2.
If n wasn't the root node, then it has a degree of 3.
Either way, its degree is higher than 1, so it can no longer be further split.

Notice also that the new nodes, o and p, has a degree of 1, so they can be split further.
When we do so, splitting does not remove any edges, only increases the total number of edges by 2.

An invariant of the SBTree is that the total number of edges always has even parity.
Our base case is the root node, which has parity 0, which is even.
As we showed above, applying the split transition increases the number of edges by 2,
so will always result in an even total number of edges.


Suppose n was the root node. If we were to remove it, and the incident edges, we would be left with o and p.

.. graph:: remove_root
	:align: center

	n [color=lightblue style=invis]
	o, p [color=indianred style=filled]

	n -- o [style=invis]
	n -- p [style=invis]

As you can see, both o and p have degree less than 1, so they could be split, following the same process as above.
Notice also, they have degree 0, and so maintains our invariant of even parity for total number of edges.
Thus o and p are both SBTrees.

Suppose the graph has had any number of transitions applied after this transition.
As showed above, the total number of nodes increases by 2 for each split.
Since the split can only be applied to a leaf node on one 'branch',
the total number of edges in that branch will increase by 2 (maintaining parity),
and the other branch will not increase (also maintaining parity).
This, after any number of transitions, each branch is also an SBTree.


**(b) Prove that two SBTrees with the same number of leaves must also have the same total number of nodes.**
**Hint: As a conjecture, guess an expression for the total number of nodes in terms of the number of leaves N (l).**
**Then use induction to prove that it holds for all trees with the same l**

.. raw:: html

	<hr>

For any SBTree, T, the total number of nodes is equal to twice the total number of leaves minus 1,
where total number of leaves is no less than 1. We define P(L) then as;

.. math::

	\forall T(V, E) \in SBTree, L = |\{ v \in V \mid deg(v) \le 1 \}|. |V| \ge 1 \Rightarrow |V| = 2L - 1

**Theorem**: The theory holds for P(L) as defined above.

**Proof**: By structural induction.

**Base Case**: P(1) is true, because when there is only one node, per the definition of a PBTree above, it is considered a leaf node.
So the total number of leaf nodes is 1, and :math:`2 \cdot 1 - 1 = 1`.

**Constructor Case**: There is one case to consider, that of splitting a leaf node.
Per the hypothesis, an SBTree, T has N nodes, where :math:`N = 2L - 1`.
When we split a node the number of leaf nodes is reduced by 1 (because the node we're splitting is now no longer a leaf node),
and then increased by 2 (for the two new nodes we add as part of the split).

This works out as,

.. math::

	\begin{aligned}

	N &= 2(L - 1) - 1 + 2

	&= 2L - 2 - 1 + 2

	&= 2L - 1

	\end{aligned}

This proves the constructor case. By structural induction this proves P(L) for any SBTree.
:math:`\blacksquare`
