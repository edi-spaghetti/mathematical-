Number Theory
=============

Problem 1
---------

Define a *3-chain* to be a (not necessarily contiguous) subsequence of three integers,
which is either monotonically increasing or monotonically decreasing.
We will show here that any sequence of five distinct integers will contain a *3-chain*.
Write the sequence as :math:`a_1, a_2, a_3, a_4, a_5`.
Note that a monotonically increasing sequences is one in which each term is greater than or equal to the previous term.
Similarly, a monotonically decreasing sequence is one in which each term is less than or equal to the previous term.
Lastly, a subsequence is a sequence derived from the original sequence by deleting some elements without changing the location of the remaining elements.

a) Assume that :math:`a_1 < a_2`. Show that if there is no *3-chain* in our sequence,
   then :math:`a_3` must be less than :math:`a_1`. (Hint: consider :math:`a_4`!)

Since the integers are distinct, we know :math:`a_x \ne a_y` for any item x and y in the sequence.

If :math:`a_3` is greater than :math:`a_2` then we have a monotonically increasing *3-chain* of :math:`(a_1,a_2,a_3)` already,
so :math:`a_3` cannot be greater than :math:`a_2`.

If :math:`a_3` is between :math:`a_1` and :math:`a_2` then :math:`a_4` has two options.

1. if :math:`a_3 < a_4` then :math:`a_1 < a_3 < a_4` which is a monotonically increasing *3-chain*,
    so :math:`a_4` cannot be greater than :math:`a_3`.
2. if :math:`a_3 > a_4` then :math:`a_2 > a_3 > a_4` which is a monotonically decreasing *3-chain*,
    so :math:`a_4` cannot be less than :math:`a_3`

Therefore, :math:`a_3` cannot be greater than :math:`a_1`.

b) Using the previous part, show that if :math:`a_1 < a_2` and there is no *3-chain* in our sequence,
   then :math:`a_3 < a_4 < a_2`.

If :math:`a_4` is greater than :math:`a_2`, then we have a monotonically increasing *3-chain* of :math:`(a_1,a_2,a_4)` already,
so :math:`a_4` cannot be greater than :math:`a_2`.

From part (a) we already established :math:`a_3 < a_2`, so if :math:`a_4` is less than :math:`a_3`,
then we have a monotonically decreasing *3-chain* of :math:`(a_2,a_3,a_4)`, so :math:`a_4` cannot be less than :math:`a_3`.

Therefore, :math:`a_4` must be between :math:`a_2` and :math:`a_3`.

c) Assuming that :math:`a_1 < a_2 \text{ and } a_3 < a_4 < a_2`,
   show that any value of :math:`a_5` must result in a *3-chain*.

From part (a) and part (b) we established :math:`a_2` and :math:`a_3` are the highest and lowest numbers respectively.

If :math:`a_4` is greater than :math:`a_1` then :math:`a_5` has two options;

1. If :math:`a_5 > a_4` then :math:`(a_3,a_4,a_5)` is a monotonically increasing *3-chain*
2. If :math:`a_5 < a_4` then :math:`(a_2,a_4,a_5)` is a monotonically decreasing *3-chain*

If :math:`a_4` is less than :math:`a_1` then :math:`a_5`, again, has two options;

1. If :math:`a_5 > a_4` then :math:`(a_3,a_4,a_5)` is a monotonically increasing *3-chain*
2. If :math:`a_5 < a_4` then :math:`(a_2,a_4,a_5)` is a monotonically decreasing *3-chain*

In every case we have a *3-chain*, therefore any value of :math:`a_5` results in a *3-chain*

d) Using the previous parts, prove by contradiction that any sequence of five distinct integers must contain a *3-chain*.

**Theorem**: Any sequence of five distinct integers must contain a *3-chain*

**Proof**: By contradiction.
We shall try to prove the proposition that there exists a sequence of five distinct integers that does not contain a *3-chain*.

The question establishes the integers in the sequence are distinct, so we don't need to consider :math:`a_x = a_y`.
This is a necessity, because if :math:`a_x = a_y` then there is always a *3-chain*.
This is because no matter if :math:`a_z` is higher, lower or equal, it will create the third item in the chain.

As we saw in (a) (b) and (c) there is always a *3-chain* if :math:`a_1 < a_2`.
So if our proposition holds then :math:`a_1 > a_2`.

If :math:`a_1 > a_2` then no subsequent number can be less than :math:`a_2`
because it would complete a monotonically decreasing *3-chain* of :math:`(a_1, a_2, a_n)`

If :math:`a_3 < a_1` then :math:`a_4` has 2 options:

1. :math:`a_4 > a_3`, but then we get :math:`(a_2, a_3, a_4)` increasing
2. :math:`a_4 < a_3`, but then we get :math:`(a_1, a_3, a_4)` decreasing

So :math:`a_3 > a_1`.
This means :math:`a_4 < a_3` because otherwise we'd get :math:`(a_1, a_3, a_4)` increasing.

So :math:`a_4 < a_3` and :math:`a_2 < a_4 < a_3`.

This leaves 2 options for :math:`a_5`;

1. :math:`a_5 > a_4`, but then we get :math:`(a_2, a_4, a_5)` increasing.
2. :math:`a_5 < a_4`, but then  we get :math:`(a_3, a_4, a_5)` decreasing.

This gives us a *3-chain* in all cases, which contradicts our proposition.
So the theory must be true - any sequence of five distinct integers must contain a *3-chain*.
:math:`\blacksquare`


Problem 2
---------

Prove by either the Well Ordering Principle or induction that for all nonnegative integers, n:

.. math::

	\sum_{i=0}^n i^3 = \bigg( {n(n+1) \over 2} \bigg)^2

**Proof**. By induction.

Let P(n) be the predicate defined like so,

.. math::

	P(n)\ ::=\ \forall n \in \Bbb Z^+. n^3 = \bigg( {n(n+1) \over 2} \bigg)^2

**Theorem**: :math:`P(n) \Rightarrow P(n + 1)`

**Base Case**: P(0) is true, because both sides equal 0 when n = 0

.. math::

	\begin{aligned}

	0^3 &= \bigg( {0(0+1) \over 2} \bigg)^2 \cr

	0^3 &= \bigg( {0 \cdot 1 \over 2} \bigg)^2 \cr

	0^3 &= \bigg( {0 \over 2} \bigg)^2 \cr

	0^3 &= 0^2 \cr

	0 &= 0

	\end{aligned}

**Inductive Step**: Assuming P(n) is true, we prove P(n + 1) is true;

.. math::

	\begin{aligned}

	0^3 + 1^3 + 2^3 + \dots + (n + 1)^3 &= \bigg( {n(n + 1) \over 2} \bigg)^2 + (n + 1)^3
		\qquad && \text{(by inductive step)} \cr

	&= { n^4 + 2n^3 + n^2 \over 4} + n^3 + 3n^2 + 3n + 1
		\qquad && \text{(bracket expansion)} \cr

	&= { n^4 + 2n^3 + n^2 \over 4} + {4n^3 + 12n^2 + 12n + 4 \over 4 }
		\qquad && \text{(multiply up to common denominator)} \cr

	&= { n^4 + 6n^3 + 13n^2 + 12n + 4 \over 4 }
		\qquad && \text{(add numerators)} \cr

	&= { (n + 1)(n^3 + 5n^2 + 8n + 4) \over 4 }
		\qquad && \text{(factor out n + 1)} \cr

	&= { (n + 1)(n + 2)(n^2 + 3n + 2) \over 4 }
		\qquad && \text{(factor out n + 2)} \cr

	&= { (n + 1)(n + 2)(n + 1)(n + 2) \over 4 }
		\qquad && \text{(factor out another n + 1)} \cr

	&= { \big( (n + 1)(n + 2) \big)^2 \over 2^2 }
		\qquad && \text{(simplify power of fraction)} \cr

	&= \bigg( { (n + 1)(n + 2) \over 2 } \bigg)^2
		\qquad && \text{(simplify power of fraction again)} \cr

	\end{aligned}

This proves P(n + 1), so by the principle of induction it follows that P(n) is true for all non-negative integers n.
:math:`\blacksquare`

Problem 3
---------

During 6.042, the students are sitting in an n × n grid.
A sudden outbreak of beaver flu (a rare variant of bird flu that lasts forever;
symptoms include yearning for problem sets and craving for ice cream study sessions)
causes some students to get infected.
Here is an example where n = 6 and infected students are marked x.

.. table::

	+---+---+---+---+---+---+
	| x | o | o | o | x | o |
	+---+---+---+---+---+---+
	| o | x | o | o | o | o |
	+---+---+---+---+---+---+
	| o | o | x | x | o | o |
	+---+---+---+---+---+---+
	| o | o | o | o | o | o |
	+---+---+---+---+---+---+
	| o | o | x | o | o | o |
	+---+---+---+---+---+---+
	| o | o | o | x | o | x |
	+---+---+---+---+---+---+


Now the infection begins to spread every minute (in discrete time-steps).
Two students are considered adjacent if they share an edge
(i.e., front, back, left or right, but NOT diagonal);
thus, each student is adjacent to 2, 3 or 4 others.
A student is infected in the next time step if either
-  the student was previously infected (since beaver flu lasts forever), or
- the student is adjacent to at least two already-infected students.
In the example, the infection spreads as shown below.

.. list-table::

	* - .. table::

		+---+---+---+---+---+---+
		| x | x |   |   | x |   |
		+---+---+---+---+---+---+
		| x | x | x |   |   |   |
		+---+---+---+---+---+---+
		|   | x | x | x |   |   |
		+---+---+---+---+---+---+
		|   |   | x |   |   |   |
		+---+---+---+---+---+---+
		|   |   | x | x |   |   |
		+---+---+---+---+---+---+
		|   |   | x | x | x | x |
		+---+---+---+---+---+---+

	  - .. table::

		+---+---+---+---+---+---+
		| x | x | x |   | x |   |
		+---+---+---+---+---+---+
		| x | x | x | x |   |   |
		+---+---+---+---+---+---+
		| x | x | x | x |   |   |
		+---+---+---+---+---+---+
		|   | x | x | x |   |   |
		+---+---+---+---+---+---+
		|   |   | x | x | x |   |
		+---+---+---+---+---+---+
		|   |   | x | x | x | x |
		+---+---+---+---+---+---+

	  - .. table::

		+---+---+---+---+---+---+
		| x | x | x | x | x |   |
		+---+---+---+---+---+---+
		| x | x | x | x | x |   |
		+---+---+---+---+---+---+
		| x | x | x | x |   |   |
		+---+---+---+---+---+---+
		| x | x | x | x | x |   |
		+---+---+---+---+---+---+
		|   | x | x | x | x | x |
		+---+---+---+---+---+---+
		|   |   | x | x | x | x |
		+---+---+---+---+---+---+

	* - 1
	  - 2
	  - 3

In this example, over the next few time-steps, all the students in class become infected.

*Theorem. If fewer than n students in class are initially infected, the whole class will never
be completely infected.*

Prove this theorem.

First, we look at how the infection can be spread.
We used x to represent an infected position, and other letters to represent adjacent positions.
For any given infected position there are 4 possible adjacent positions to infect;

.. list-table::

	* - .. table::

		+---+---+---+---+
		|   | 1 | 2 | 3 |
		+===+===+===+===+
		| 1 |   | a |   |
		+---+---+---+---+
		| 2 | d | x | b |
		+---+---+---+---+
		| 3 |   | c |   |
		+---+---+---+---+

	* - fig. 1

In figure 1, we can see the four positions: above (a), right (b), bottom (c) and left (d).
For consistency I'll label all example edges clockwise from the top.

These form the boundary of infection spread from any given time step.
Note that for the purposes of counting the length of the boundary,
an edge is considered *from* an infected position *to* a vacant one.
So overlapping edges count twice, occupied positions don't count,
and positions are considered vacant even if they are off the board.

.. list-table::

	* - .. table::

		+---+---+---+---+---+---+
		|   |   | 1 | 2 | 3 |   |
		+===+===+===+===+===+===+
		| 1 |   | a |   | e |   |
		+---+---+---+---+---+---+
		| 2 | d | x |b h| x | f |
		+---+---+---+---+---+---+
		| 3 |   | c |   | g |   |
		+---+---+---+---+---+---+

	  - .. table::

		+---+---+---+---+---+
		|   |   | 1 | 2 | 3 |
		+===+===+===+===+===+
		| 1 |   | a | b |   |
		+---+---+---+---+---+
		| 2 | f | x | x | c |
		+---+---+---+---+---+
		| 3 |   | e | d |   |
		+---+---+---+---+---+

	* - fig. 2

	  - fig. 3

As you can see from figure 2, the position at (2, 2) has two edges (b and h),
one from the left x, and one from the right x - making the total length of the boundary 8.
Also note edges d and f spread outside the original board where n=3.

In figure 3 you can see the infected positions at (1, 2) and (2, 2) are adjacent,
so there are only 6 edges in the boundary in total.

**Theorem 1**: The boundary length never increases.

**Proof**: By cases.

Let's look at how the boundary changes when infection spreads.
Per the rules, a position only becomes infected if there are 2 or more adjacent infected positions.
Since there are maximum four adjacent positions, this means there are three different possibilities;
2, 3 or 4 adjacent infected positions.

*Case 1*: 2 adjacent infected positions

.. list-table::

	* - .. table::

		+---+---+---+---+---+---+
		|   |   | 1 | 2 | 3 |   |
		+===+===+===+===+===+===+
		| 1 |   | a |   | e |   |
		+---+---+---+---+---+---+
		| 2 | d | x |b h| x | f |
		+---+---+---+---+---+---+
		| 3 |   | c |   | g |   |
		+---+---+---+---+---+---+

	  - .. table::

		+---+---+---+---+---+---+
		|   |   | 1 | 2 | 3 |   |
		+===+===+===+===+===+===+
		| 1 |   | a | i | e |   |
		+---+---+---+---+---+---+
		| 2 | d | x | x | x | f |
		+---+---+---+---+---+---+
		| 3 |   | c | j | g |   |
		+---+---+---+---+---+---+

	* - fig. 4a

	  - fig. 4b

In figure 4a there are 8 edges in the boundary (a-h).
One time step later, in figure 4b, 2 edges (b and h) have been removed, and 2 have been added (i and j).
This gives us no net change in boundary length, there are still 8 edges,
so the boundary has not increased.

*Case 2*: 3 adjacent infected positions

.. list-table::

	* - .. table::

		+---+---+---+---+---+---+
		|   |   | 1 | 2 | 3 |   |
		+===+===+===+===+===+===+
		|   |   |   | i |   |   |
		+---+---+---+---+---+---+
		| 1 |   |a l| x |e j|   |
		+---+---+---+---+---+---+
		| 2 | d | x |bhk| x | f |
		+---+---+---+---+---+---+
		| 3 |   | c |   | g |   |
		+---+---+---+---+---+---+

	  - .. table::

		+---+---+---+---+---+---+
		|   |   | 1 | 2 | 3 |   |
		+===+===+===+===+===+===+
		|   |   |   | i |   |   |
		+---+---+---+---+---+---+
		| 1 |   |a l| x |e j|   |
		+---+---+---+---+---+---+
		| 2 | d | x | x | x | f |
		+---+---+---+---+---+---+
		| 3 |   | c | m | g |   |
		+---+---+---+---+---+---+

	* - fig. 5a

	  - fig. 5b

In figure 5a there are 12 edges in the boundary (a-k).
On time step later in figure 5b, we lose 3 (b, h and k), but gain 1 (m).
This gives us a net loss of 2 edges, so the boundary has not increased.

.. note::

	positions (1, 1) and (3, 1) also have overlapping edges, so would spread the infection on the time step.
	However, they are just variations on case 1, so I didn't consider them in figure 5b,
	because we have already demonstrated 2 adjacent infections results in no net gain of boundary length.


*Case 3*: 4 adjacent infected positions

.. list-table::

	* - .. table::

		+---+---+---+----+---+---+
		|   |   | 1 | 2  | 3 |   |
		+===+===+===+====+===+===+
		|   |   |   | i  |   |   |
		+---+---+---+----+---+---+
		| 1 |   |a l| x  |e j|   |
		+---+---+---+----+---+---+
		| 2 | d | x |bhkm| x | f |
		+---+---+---+----+---+---+
		| 3 |   |c p| x  |g n|   |
		+---+---+---+----+---+---+
		|   |   |   | o  |   |   |
		+---+---+---+----+---+---+

	  - .. table::

		+---+---+---+---+---+---+
		|   |   | 1 | 2 | 3 |   |
		+===+===+===+===+===+===+
		|   |   |   | i |   |   |
		+---+---+---+---+---+---+
		| 1 |   |a l| x |e j|   |
		+---+---+---+---+---+---+
		| 2 | d | x | x | x | f |
		+---+---+---+---+---+---+
		| 3 |   |c p| x |g n|   |
		+---+---+---+---+---+---+
		|   |   |   | o |   |   |
		+---+---+---+---+---+---+

	* - fig. 6a

	  - fig. 6b

In figure 6a there are 16 edges in the boundary (a-p).
In figure 6b (on time step later) we lose 4 edges (b, h, k and m) and gain no new edges.
This gives us a net loss of 4 edges, so again, the boundary length has not increased.

.. note::

	As before, the overlapping edges in (1, 1), (3, 1), (1, 3) and (3, 3) are the same as case 1,
	which we have shown doesn't result in any net gain to boundary length.

In each case, the boundary did not increase so theory holds that the boundary length cannot increase.
:math:`\blacksquare`

**Theorem**: If fewer than n students in class are initially infected,
the whole class will never be completely infected.

As shown in figure 1, the maximum adjacent edges to any position is 4.
If less than n students are initially infected, then the maximum length the boundary can be is 4(n - 1).

As shown in figure 2 and 3, edges only count towards boundary length if they are outside the original board, or if the position is not already infected.
Therefore, length of the boundary when every position is infected is 4n.

As proved in theorem 1, the length of the boundary cannot increase.
Since 4(n - 1) < 4n, if there are fewer than n initially infected,
the boundary length can never reach the boundary length where every position is infected.
Therefore, the whole class will never be completely infected.
:math:`\blacksquare`


Problem 4
---------

Find the flaw in the following bogus proof that :math:`a^n = 1` for all nonnegative integers n, whenever a is a nonzero real number.

**Proof**. The *bogus* proof is by induction on n, with hypothesis

.. math::

	P(n) ::= \forall k \le n. a^k = 1

where k is a nonnegative integer valued variable.

**Base Case**: P(0) is equivalent to :math:`a^0 = 1`, which is true by definition of :math:`a^0`.
(By convention, this holds even if a = 0.)

**Inductive Step**: By induction hypothesis, :math:`a^k = 1` for all :math:`k \in \Bbb N` such that :math:`k \le n`.
But then

.. math::

	a^{n+1} = {a^n \cdot a^n \over a^{n-1}} = {1 \cdot 1 \over 1} = 1,

which implies that P(n + 1) holds.
It follows by induction that P(n) holds for all :math:`n \in \Bbb N`,
and in particular, :math:`a^n = 1` holds for all :math:`n \in \Bbb N`.

.. raw:: html

	<hr>

Firstly, the proof introduces an additional variable k in the definition of P.
It also does not specify that a is a nonzero real number.
It should be;

.. math::

	P(n) ::= \forall a \in \Bbb R_{\ne 0}. \forall n \in \Bbb N^{+}. a^n = 1

Next, in the base case, they show that P(0) holds even if a = 0, which contradicts 'a' being a *nonzero* real number.

Then in the inductive step they use the reasoning that :math:`a^k = 1` where k is less than or equal to n.
However, they then prove :math:`a^{n+1} = a^k` - but :math:`n+1 \ne k` because k must be equal or less than n.
