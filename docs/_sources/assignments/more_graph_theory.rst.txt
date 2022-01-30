More Graph Theory
=================


Problem 1
---------

.. admonition:: Introduction

	Recall that a tree is a connected acyclic graph.
	In particular, a single vertex is a tree.
	We define a Splitting Binary Tree, or SBTree for short, as either the lone vertex, or a tree with the following properties:

		1. exactly one node of degree 2 (called the root).

		2. every other node is of degree 3 or 1 (called internal nodes and leaves, respectively).

	For the case of one single vertex (see above), that vertex is considered to be a leaf.


a)
^^

.. admonition:: Question

	Show if an SBTree has more than one vertex, then the induced subgraph obtained by removing the unique root consists of two disconnected SBTrees.
	You may assume that by removing the root you obtain two separate connected components,
	so all you need to prove is that those two components are SBTrees.


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

b)
^^

.. admonition:: Question

	Prove that two SBTrees with the same number of leaves must also have the same total number of nodes.
	Hint: As a conjecture, guess an expression for the total number of nodes in terms of the number of leaves N (l).
	Then use induction to prove that it holds for all trees with the same l

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


Problem 2
---------

.. admonition:: Introduction

	In ”Die Hard: The Afterlife”, the ghosts of Bruce and Sam have been sent by the evil Simon
	on another mission to save midtown Manhattan. They have been told that there is a bomb
	on a street corner that lies in Midtown Manhattan, which Simon defines as extending from
	41st Street to 59th Street and from 3rd Avenue to 9th Avenue. Additionally, the code that
	they need to defuse the bomb is on another street corner. Simon, in a good mood, also tosses
	them two carrots:

	 - He will have a helicopter initially lower them to the street corner where the bomb is.
	 - He promises that the code is placed only on a corner of a numbered street and a
	   numbered avenue, so they don’t have to search Broadway.

	The map of midtown Manhattan is an example of an :math:`N \times M` (undirected) grid.
	In particular, midtown Manhattan is a :math:`19 \times 7` grid.
	Bruce and Sam need to check all :math:`19 \cdot 7 = 133` street corners for the code in 133 steps or less.

a)
^^

.. admonition:: Question

	Show that they cannot do it – that is, more generally, show that if both N and M are odd,
	then the :math:`N \times M` grid is not Hamiltonian.

First we will show that any :math:`N \times M` grid is bipartite.
We can do this by considering the fact that any step in the graph must either be horizontally or vertically,
since it is a 2-dimensional grid - there are no loops backs or diagonals.

Therefore, any step vertically must have a counterpart step vertically in the opposite direction to return to the same avenue.
By symmetry the same is true for horizontal steps.

This means for any cycle, there will be an even number (since any number mutiplied by 2 is even) number of steps.
As we showed in :ref:`graph theory <graph-theory>` problem 1, a graph is bipartite if and only if it is comprised of paths and even cycles.
As we've just shown an :math:`N \times M` grid has only even cycles, this means that it is also bipartite.

Next we must show that if both N and M are odd, the grid is not Hamiltonian.
Each step along a Hamiltonian path must travel to a new node, and since the graph is bipartite,
this means each node will be the opposite colour to the previous one.

However, if N and M are both odd, this means the total number of nodes is odd.
Therefore if the node we started as was coloured blue, the last node we arrive at will also be blue.
But since the graph is bipartite then cannot be a connection between the first and last node.

Therefore to arrive back at the first node we must revisit at least one of the nodes,
which contradicts the properties of a Hamiltonian graph.

Therefore if N and M are both odd, the :math:`N \times M` grid is not Hamiltonian.
:math:`\blacksquare`

b)
^^

.. admonition:: Intro

	Suppose Simon defined Midtown in the more standard way as extending from 40th Street to 59th Street
	and from 3rd Avenue to 9th Avenue (that is suppose Midtown Manhattan was a 20 × 7 grid),
	and gave them another 7 minutes.

1.
""

.. admonition:: Question

	Show that if either N is even and :math:`M > 1` or M is even and :math:`N > 1`,
	then the :math:`N \times M` grid is Hamiltonian.

**Proof** By Induction

Let P(n) be the predicate, where n is any positive integer greater than 1,
such that :math:`N = 2n`, and M is any any positive integer greater than 1.
We will show that any combination of :math:`N \times M` grid is Hamiltonian.

**Base Case**: n = 1

This is trivially Hamiltonian as illustrated below,

.. image:: ../images/hamiltonian-2xM.png
	:align: center

As you can see, the path can travel down one side and back up the other for any value of M.
This completes a cycle visiting each node, and so it is Hamiltonian.

**Inductive Step**:

Next we must show that :math:`P(n + 1)` is true, given that :math:`P(n)` is true.

We assume that the grid for :math:`P(n)` is arranged as follows,

.. image:: ../images/hamiltonian-NxM.png
	:align: center

Note that this pattern would not be possible where M = 2, but by symmetry,
if M = 2 an :math:`N \times 2` grid has the same properties as a :math:`2 \times M` grid,
which as we showed in the base case is Hamiltonian.

Note also the subsection from the :math:`2^{nd}` to the :math:`M^{th}` row is also
a :math:`2 \times M - 1` grid, and similar to the base case is also Hamiltonian,
so the pattern holds for any value of M.

Notice that any time we increase n by 1, the :math:`N \times M` grid increases in size by 2 (so that N remains an even number).
Therefore, for :math:`P(n+1)` the pattern is as follows,

.. image:: ../images/hamiltonian-N+1xM.png
	:align: center

This creates a path through all new nodes, plus the existing nodes in the :math:`P(n)` grid.
Thus the theory holds for :math:`P(n+1)`.
So by induction we can conclude that for an even N greater 1 one,
and any value of M, the :math:`N \times M` grid is Hamiltonian.

By symmetry the same is true if M is even and greater than 1.
:math:`\blacksquare`

2.
""

.. admonition:: Question

	Explain why your proof breaks down when N and M are odd.

If N and M are both odd, then the assumption above about :math:`P(n+1)` is no longer true.
That is, the pattern becomes this,

.. image:: ../images/hamiltonian-odd-N.png
	:align: center

This is invalid because there is no connection between :math:`(N+1, M)` and :math:`(2, N)`.
:math:`\blacksquare`

Any other pattern would also run into a similar issue, trust me :)
:math:`\blacksquare`

3.
""

.. admonition:: Question

	Would they survive? Does it depend on where the bomb is placed?

Yes, they would survive, and it does not matter where the bomb is placed.
Since at least one dimension of the :math:`20 \times 7` grid is even, by part 1 the grid is hamiltonian.
That means every node can be visited once (and only once) on a round trip from the starting location.

By the rules of the exercise, they start at the location of the bomb,
and have :math:`133 + 7 = 140` steps to return with 2 minutes spare to defuse.
Since we have a :math:`20 \times 7` hamiltonian grid, and :math;`20 \cdot 7 = 140`,
they have exactly enough time to visit every node once and return to the start to defuse the bomb.
:math:`\blacksquare`

Problem 3
---------

.. admonition:: Introduction

	An :math:`n-node` graph is said to be tangled if there is an edge leaving every set of :math:`\lceil {n \over 3} \rceil` or fewer vertices.
	As a special case, the graph consisting of a single node is considered tangled.

a)
^^

.. admonition:: Question

	Find the error in the proof of the following claim.


.. admonition:: Claim

	Every non-empty, tangled graph is connected.

	**Proof**. The proof is by strong induction on the number of vertices in the graph.
	Let :math:`P(n)` be the proposition that if an :math:`n-node` graph is tangled,
	then it is connected.

	In the base case, :math:`P(1)` is true because the graph consisting of a single node is defined to be tangled and is trivially connected.

	In the inductive step, for :math:`n \ge 1` assume :math:`P(1), \dots , P(n)` to prove :math:`P(n + 1)`.
	That is, we want to prove that if an :math:`(n + 1)-node` graph is tangled, then it is connected.

	Let :math:`G` be a tangled, :math:`(n + 1)-node` graph.
	Arbitrarily partition G into two pieces so that the first piece contains exactly :math:`\lceil {n \over 3} \rceil` vertices,
	and the second piece contains all remaining vertices.

	Note that since :math:`n \ge 1`, the graph :math:`G` has a least two vertices,
	and so both pieces contain at least one vertex.

	By induction, each of these two pieces is connected.
	Since the graph G is tangled, there is an edge leaving the first piece, joining it to the second piece.
	Therefore, the entire graph is connected.

	This shows that :math:`P(1), \dots , P(n)` imply :math:`P(n + 1)`, and the claim is proved by strong induction.
	:math:`\square`

The error is with the statement *'By induction each of these two pieces is connected'*.
We cannot assume that every subgraph of a tangled graph is also tangled, and by extension cannot infer that they are connected.

b)
^^

.. admonition:: Question

	Draw a tangled graph that is not connected.

The following is a :math:`6-node` tangled graph,

.. image:: ../images/tangled-not-connected.png
	:align: center

To be tangled it must have an edge leaving any set of :math:`\lceil {6 \over 3} \rceil = 2` or fewer nodes.
Since the minimum degree on each node is 1, any set of 1 nodes will have an edge leaving it.

Within the graph there are two components, each with 3 nodes connected.
For any set of 2 nodes within a component, the third node in the component has an edge leaving the set.
See below, the red edge gives it the property of being tangled.

.. image:: ../images/tangled-set-2-of-component.png
	:align: center

For any set of nodes between components (i.e. one node per component), there will also be edges leaving the set.

.. image:: ../images/tangled-set-2-between-components.png
	:align: center

However there are no edges between the components, so it is not connected.

c)
^^

.. admonition:: Question

	An :math:`n-node` graph is said to be **mangled** if there is an edge leaving every set of :math:`\lceil {n \over 2} \rceil` or fewer vertices.
	Again, as a special case, the graph consisting of a single node is considered mangled.
	Prove the following claim. *Hint: Prove by contradiction.*

.. admonition:: Claim

	Every non-empty, mangled graph is connected.

**Proof**: By contradiction

Let :math:`G` be a non-empty, mangled graph that is not connected.
Since :math:`G` is mangled, every node must have a degree of at least 1 in order to meet the requirement that every set of 1 node (the smallest set) has an edge leaving it.
Since :math:`G` is not connected, then it can be grouped into two components, :math:`G'\ and\ G''`, such that there is no connection between the them.

Since :math:`G` is mangled, we know the size of both components must be greater than :math:`\lceil {n \over 2} \rceil`,
in order for there to be an edge leaving the largest possible set size to meet the criteria of being mangled,
but also that edge must connect to a node in the same component, to meet the criteria of not being connected to each other.

However, by simple arithmetic we also know that :math:`\lceil {n \over 2} \rceil \ge {|G| \over 2}`.
That is, both components need to be larger than the largest set size, but the largest set size is at least half the total size of the graph.
(They can't both be larger than half the size of the total).

This is a contradiction, so we can conclude that the edge leaving any given largest set must connect to a node in the other component, thus connecting the graph.
Therefore every non-empty, mangled graph is connected.
:math:`\blacksquare`

Problem 4
---------

a)
^^

.. admonition:: Question

	Suppose that G is a simple, connected graph of n nodes.
	Show that G has exactly :math:`n − 1` edges iff G is a tree.

First we will show the forward relation.

**Proof**: By induction.

Let :math:`P(n)` be the predicate that if G has exactly :math:`n - 1` nodes then it is a tree,
where n is the number of nodes in G

**Base Case**: P(1) is true because a graph of 1 node has 0 edges, and :math:`1 - 1 = 0`.

**Inductive Step**: Assuming P(n) is true, let's consider an :math:`(n+1)-node` tree, T.
We know that any graph with at least 2 nodes has at least 2 leaves, so we can choose one of these leaves, :math:`l`.
If we remove :math:`l` and the edge associated with it (by definition a leaf has only 1 edge),
we are left with an :math:`n-node` graph, :math:`T'`.

Since we removed a leaf we know :math:`T'` remains connected,
and we also know that any connected subgraph of a tree is also a tree.
:math:`T'` is, then, an :math:`n-node` tree, which by induction has :math:`n - 1` edges.

So we can conclude T has :math:`(n - 1) + 1` edges (:math:`n-1` from :math:`T'`, and 1 from :math:`l`).
:math:`(n - 1) + 1 = n` which proves the inductive hypothesis for :math:`P(n+1)`.
:math:`\square`

Next we must show the reverse is also true, that is if a connected graph has :math:`n - 1` edges then it is a tree.

**Proof**: By contradiction.

Consider a connected graph, :math:`G`, that has :math:`n - 1` edges but is not a tree.
Since it is connected, then there must exist a path from any given node to any other node in the graph.
Since it is not a tree, then it must contain a cycle.

We also know that the minimum number of edges for an :math:`n-node` graph to be connected in :math:`n - 1`.
That is, removing an edge from it would make it disconnected.

However, as we concluded above, there is a cycle in G.
This means there exists two nodes, :math:`u` and :math:`v`, that are part of a cycle.
However, since they're part of a cycle, we can remove an edge in the cycle and :math:`u` will still be connected to :math:`v` in the other direction of the cycle.

.. image:: ../images/trees-cycle-contradiction.png
	:align: center

As illustrated, we can remove an edge from path :math:`p_0` and :math:`u` will still be connected :math:`v` by path :math:`p_1`

This contradicts :math:`n - 1` edges being the minimum number of edges for an :math:`n-node` graph to be connected,
so we can conclude there are no cycles.

Since there are no cycles, and the graph is connected, then it is a tree.
:math:`\square`

Thus we have shown the question stated, G has exactly :math:`n − 1` edges iff G is a tree,
holds in both logical directions directions, and so the theory holds.
:math:`\blacksquare`

b)
^^

.. admonition:: Question

	Prove by induction that any connected graph has a spanning tree.

Let P(n) be our predicate where if :math:`G` is an :math:`n-node` connected graph, then it has a spanning tree.

**Proof**: By induction.

**Base Case**: :math:`P(1)` is trivially true because a single node is considered connected, and also a tree.

**Inductive Step**: Given :math:`P(n)` is true, we must show :math:`P(n+1)` is true.

Suppose we remove one node, :math:`v`, and any adjacent edges, from :math:`G` such that we are left with a connected subgraph, :math:`G'`.
We know such a node exists because if we consider :math:`v`'s neighbour, :math:`u`, then there are only two options (note: they are not mutually exclusive);

1. :math:`u` is part of a cycle :math:`v — u \dots — v`.
   But then removing the edge :math:`v — u` means any nodes can travel the other direction of the cycle and still connect to :math:`u`
2. :math:`u` is part of path, which by definition must have at least two ends, one of which is :math:`v`

By the inductive hypothesis we know :math:`G'` has a spanning tree, :math:`T'`.

When we add :math:`v` back to :math:`G'` it must have at least one edge, since :math:`G` is connected,
between :math:`v` and a node in :math:`T'`.

This makes :math:`v` a leaf of a new spanning tree, :math:`T`.
This proves :math:`P(n+1)` and so the theorem is true.
:math:`\blacksquare`

Problem 5
---------

.. admonition:: Introduction

	The adjacency matrix of a graph is given below.

	.. math::

		\left\lbrack \begin{matrix}
		0 & 1 & 1 & 1 & 0 & 1 \\
		1 & 0 & 0 & 1 & 1 & 1 \\
		1 & 0 & 0 & 1 & 1 & 1 \\
		1 & 1 & 1 & 0 & 1 & 0 \\
		0 & 1 & 1 & 1 & 0 & 1 \\
		1 & 1 & 1 & 0 & 1 & 0
		\end{matrix} \right\rbrack

a)
^^

.. admonition:: Question

	Draw the graph defined by this adjacency matrix.
	Label the vertices of your graph :math:`1, 2, \dots , 6` so that vertex i corresponds to row and column i of the matrix.

Given the above labelling of verices;

.. graph:: adjacency

    1 -- 2
    1 -- 3
    1 -- 4
    1 -- 6

    2 -- 4
    2 -- 5
    2 -- 6

    3 -- 4
    3 -- 5
    3 -- 6

    4 -- 5

    5 -- 6

b)
^^

.. admonition:: Question

	In a graph, we define the distance between to vertices to be the length of the shortest path between them.
	We define the diameter of a graph to be the largest distance between any two nodes.
	What is the diameter of this graph? Explain why

The diameter of this graph is 2.

It cannot be shorter than 2 because the following edges do not exist,
:math:`\{1, 5\}, \{2, 3\}, \{4, 6\}`, so there must be a path of at least 2 to connect these nodes.

It cannot be longer than 2 because every node has a degree of 4,
so including the node itself that makes 5 nodes.
There are only 6 nodes in the graph, so for any given node,
the only possible longer path is to the :math:`6^{th}` node,
which would be of length 2.

c)
^^

.. admonition:: Question

	Find a cycle in this graph of maximum length and explain why it has maximum length.

A cycle of maximum length is : math:`1, 6, 5, 3, 4, 2, 1` which has a length of 6.
It is maximum length because it contains every node in the graph, so it cannot possibly be longer.
Since it traverses every node in the graph, this is also called a hamiltonian cycle.

d)
^^

.. admonition:: Question

	Give a coloring of the vertices that uses the minimum number of colors.
	Prove that this a minimum coloring.

.. graph:: colouring

    1, 5[color=indianred style=filled]
    2[color=lightblue style=filled]
    3[color=palegreen style=filled]
    4, 6[color=peachpuff style=filled]

    1 -- 2
    1 -- 3
    1 -- 4
    1 -- 6

    2 -- 4
    2 -- 5
    2 -- 6

    3 -- 4
    3 -- 5
    3 -- 6

    4 -- 5

    5 -- 6

4 is the minimum number of colours because every node has a degree of 4.

Problem 6
---------

.. admonition:: Introduction

	Let G be a graph.
	In this problem we show every vertex of odd degree is connected to at least one other vertex of odd degree in G.

a)
^^

.. admonition:: Question

	Let v be an odd degree node.
	Consider the longest walk starting at v that does not repeat any edges (though it may omit some).
	Let w be the final node of that walk. Show that :math:`w \ne v`.

Suppose we choose any node, :math:`x`,  along the path of :math:`(v— \dots —x— \dots —v)`, where :math:`x \ne v`.
The node x may be crossed any number of times, but each time it does so,
there is an edge going in to the node, and an edge leading out of the node,
meaning the number of edges is even.

With this principle we know for any node starting a cycle, e.g. :math:`(x— \dots —x)`,
the degree of that node is even.

By our criteria, :math:`v` is an odd degree node so cannot end the walk where we started,
because that would make :math:`v` have even degree, so :math:`w` cannot be :math:`v`

However, suppose there is another edge leading out of :math:`v` to give it even degree that we haven't crossed yet.
But then, that contradicts our assumption that this is the longest walk,
because there would be another edge to cross, making the walk longer.
So the hypothesis still stands.

b)
^^

.. admonition:: Question

	Show that w must also have odd degree

Similar to the last part of the previous question,
suppose we arrive at :math:`w` at the end of the longest walk.
We may have crossed :math:`w` any number of times already, across a multiple of 2 edges,
But suppose we arrive at the end of the longest walk and there is another edge leading out that we haven't crossed yet.

But then that contradicts the assumption that this is the longest walk,
because we could travel along that edge to the node it is connected to.
So :math:`w` must have odd degree.
