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

Problem 5
---------

Let the sequence :math:`G_0, G_1, G_2, \dots` be defined recursively as follows:
:math:`G_0 = 0, G_1 = 1`, and :math:`G_n = 5G_{n−1} − 6G_{n−2}`, for every :math:`n \in \Bbb N, n \ge 2`.
Prove that for all :math:`n \in N, G_n = 3^n − 2^n`.

.. raw:: html

	<hr>

The recursive data type G of non-negative integers over :math:`\Bbb N`, are defined as follows,

- **Base Case**:

  1. :math:`G_0` is 0

  2. :math:`G_1` is 1

- **Constructor Case**: if :math:`n - 1 \in G` and :math:`n - 2 \in G` then :math:`G_n = 5 \cdot (n - 1) - 6 \cdot (n - 2)`

Let P(n) be the predicate, defined as follows,

.. math::

	P(n) = 5G_{n-1} - 6G_{n-2} = 3^n - 2^n

**Theorem**: P(n) holds for all n :math:`\in \Bbb N`

**Proof**. By structural induction on the definition that :math:`n \in G`, using P(n) as the induction hypothesis.

**Base Case**: There are two base cases which we will demonstrate.

1. P(0)

   .. math::

	  \begin{aligned}

	  0 &= 3^0 - 2^0

	  &= 1 - 1

	  \end{aligned}

   By convention, any real number to the power 0 is 1.

2. P(1)

   .. math::

	   \begin{aligned}

	   1 &= 3^1 - 2^1

	   &= 3 - 2

	   \end{aligned}

**Constructor Case**: We must show P(n) holds given that P(n-1) and P(n-2) hold.

.. math::

	\begin{aligned}

	5(3^{n-1} - 2^{n-1}) - 6(3^{n-2} - 2^{n-2}) &= 3^n - 2^n
		\qquad && \text{(by inductive hypothesis)} \cr

	5({3^n \over 3^1}) - 5({2^n \over 2^1}) - 6({3^n \over 3^2}) - 6(-{2^n \over 2^2}) &=
		\qquad && \text{(by quotient rule)} \cr

	{12 \cdot 5 \cdot 3^n \over 36} - {18 \cdot 5 \cdot 2^n) \over 36} -
	{4 \cdot 6 \cdot 3^n \over 36} - \bigg( - {9 \cdot 6 \cdot 2^n \over 36} \bigg) &=
		\qquad && \text{(multiply up to common factor)} \cr

	{12 \cdot 5 \cdot 3^n \over 36} - {18 \cdot 5 \cdot 2^n) \over 36} -
	{4 \cdot 6 \cdot 3^n \over 36} + {9 \cdot 6 \cdot 2^n \over 36} &=
		\qquad && \text{(remove double negative)} \cr

	{60 \cdot 3^n - 90 \cdot 2^n - 24 \cdot 3^n + 54 \cdot 2^n \over 36} &=
		\qquad && \text{(add and simplify)} \cr

	{\bcancel{36} \cdot 3^n - \bcancel{36} \cdot 2^n \over \bcancel{36}} &=
		\qquad && \text{(remove common divisor)} \cr

	3^n - 2^n &=

	\end{aligned}

This proves P(n) holds as required, completing the constructor case.
By structural induction we conclude that P(n) holds of all :math:`n \in \Bbb N. \blacksquare`

Problem 6
---------

In the 15-puzzle, there are 15 lettered tiles and a blank square arranged in a 4 × 4 grid.
Any lettered tile adjacent to the blank square can be slid into the blank.
For example, a sequence of two moves is illustrated below:

.. list-table::

	* - .. table::

		+-----+-----+-----+-----+
		|  A  |  B  |  C  |  D  |
		+-----+-----+-----+-----+
		|  E  |  F  |  G  |  H  |
		+-----+-----+-----+-----+
		|  I  |  J  |  K  |  L  |
		+-----+-----+-----+-----+
		|  M  |  O  |  N  |     |
		+-----+-----+-----+-----+

	  - :math:`\rightarrow`

	  - .. table::

		+-----+-----+-----+-----+
		|  A  |  B  |  C  |  D  |
		+-----+-----+-----+-----+
		|  E  |  F  |  G  |  H  |
		+-----+-----+-----+-----+
		|  I  |  J  |  K  |  L  |
		+-----+-----+-----+-----+
		|  M  |  O  |     |  N  |
		+-----+-----+-----+-----+

	  - :math:`\rightarrow`

	  - .. table::

		+-----+-----+-----+-----+
		|  A  |  B  |  C  |  D  |
		+-----+-----+-----+-----+
		|  E  |  F  |  G  |  H  |
		+-----+-----+-----+-----+
		|  I  |  J  |     |  L  |
		+-----+-----+-----+-----+
		|  M  |  O  |  K  |  N  |
		+-----+-----+-----+-----+

In the leftmost configuration shown above, the O and N tiles are out of order.
Using only legal moves, is it possible to swap the N and the O, while leaving all the other tiles in their original position and the blank in the bottom right corner?
In this problem, you will prove the answer is “no”.

**Theorem**. No sequence of moves transforms the board below on the left into the board below on the right.

.. list-table::

	* - .. table::

		+-----+-----+-----+-----+
		|  A  |  B  |  C  |  D  |
		+-----+-----+-----+-----+
		|  E  |  F  |  G  |  H  |
		+-----+-----+-----+-----+
		|  I  |  J  |  K  |  L  |
		+-----+-----+-----+-----+
		|  M  |  O  |  N  |     |
		+-----+-----+-----+-----+

	  - :math:`\rightarrow`

	  - .. table::

		+-----+-----+-----+-----+
		|  A  |  B  |  C  |  D  |
		+-----+-----+-----+-----+
		|  E  |  F  |  G  |  H  |
		+-----+-----+-----+-----+
		|  I  |  J  |  K  |  L  |
		+-----+-----+-----+-----+
		|  M  |  N  |  O  |     |
		+-----+-----+-----+-----+

(a) We define the “order” of the tiles in a board to be the sequence of tiles on the board reading from the top row to the bottom row and from left to right within a row.
For example, in the right board depicted in the above theorem, the order of the tiles is A, B, C, D, E, etc.
Can a row move change the order of the tiles? Prove your answer.

.. raw:: html

	<hr>

If we take a tile in position p where :math:`p \in \{\Bbb N | 1 \le n \le n^2\}` and :math:`n = 4`,
then we can define a row move as,

1. :math:`p_1 = p_0 - 1`, move left one tile within a row

2. :math:`p_1 = p_0 + 1`, move right one tile within a row

By the rules of the game, a tile can only move to an empty position,
so between positions :math:`p_0 \rightarrow p_1` there are zero tiles.

This means in :math:`p_1` the tile has not moved before or after any other tiles, so the order is not changed.
More formally, the number of pairs of letters :math:`L_1` and :math:`L_2` in which :math:`L_1` is before :math:`L_2` in the order of the tiles before the move,
and later in the order of the tiles after the move, remains the same.
:math:`\blacksquare`

(b) How many pairs of tiles will have their relative order changed by a column move?
More formally, for how many pairs of letters :math:`L_1` and :math:`L_2` will :math:`L_1` appear earlier in the order of the tiles than :math:`L_2` before the column move and later in the order after the column move?
Prove your answer correct.

.. raw:: html

	<hr>

We can define a column move as

1. :math:`p_1 = p_0 - n`, move left 4 tiles (up one row within a column)

2. :math:`p_1 = p_0 + n`, move right 4 tiles (down one row within a column)

By the rules of the game, a tile can only move to an empty position,
so between positions :math:`p_0 \rightarrow p_1` there are :math:`n - 1` tiles where :math:`n = 4`, so 3 tiles.

When any given pair of tiles changes order there are two cases,

1. :math:`L_1` was before :math:`L_2`, and is now after :math:`L_2` after the move (+1 inversion)

2. :math:`L_1` was after :math:`L_2`, and is now before :math:`L_2` after the move (-1 inversion)

Since there are two cases for change in number of inversions, there are 8 possibilities with 3 tiles,

.. list-table::

	* - tile 1
	  - tile 2
	  - tile 3
	  - total change

	* - -1
	  - -1
	  - -1
	  - -3

	* - -1
	  - -1
	  - +1
	  - -1

	* - -1
	  - +1
	  - -1
	  - -1

	* - -1
	  - +1
	  - +1
	  - +1

	* - +1
	  - -1
	  - -1
	  - -1

	* - +1
	  - -1
	  - +1
	  - +1

	* - +1
	  - +1
	  - -1
	  - +1

	* - +1
	  - +1
	  - +1
	  - +3

As you can see, the sum change in number of inversions is :math:`\pm 1 \text{ or } \pm 3`.
More formally, the number of pairs of letters :math:`L_1` and :math:`L_2` in which :math:`L_1` is before :math:`L_2` in the order of the tiles before the move,
and later in the order of the tiles after the move, increases or decreases by 1 or 3.
:math:`\blacksquare`

(c) We define an inversion to be a pair of letters :math:`L_1` and :math:`L_2` for which :math:`L_1` precedes :math:`L_2` in the alphabet,
but :math:`L_1` appears after :math:`L_2` in the order of the tiles.
For example, consider the following configuration:

.. table::

	+-----+-----+-----+-----+
	|  A  |  B  |  C  |  E  |
	+-----+-----+-----+-----+
	|  D  |  H  |  G  |  F  |
	+-----+-----+-----+-----+
	|  I  |  J  |  K  |  L  |
	+-----+-----+-----+-----+
	|  M  |  N  |  O  |     |
	+-----+-----+-----+-----+

There are exactly four inversions in the above configuration: E and D, H and G, H and F, and G and F.
What effect does a row move have on the parity of the number of inversions?
Prove your answer.

.. raw:: html

	<hr>

As shown in part (a) a row move does not increase or decrease the number of inversions.
Therefore, a column move has no effect on the parity of the number of inversions.
:math:`\blacksquare`

(d) What effect does a column move have on the parity of the number of inversions?
Prove your answer.

.. raw:: html

	<hr>

As shown in part (b), a row move increases or decreases the number of inversions by 1 or 3.
1 and 3 are both odd numbers, and adding any number to an odd number changes the parity.
So a row move changes the parity of the number of inversions every time.
:math:`\blacksquare`

(e) The previous problem part implies that we must make an odd number of column moves in order to exchange just one pair of tiles (N and O, say).
But this is problematic, because each column move also knocks the blank square up or down one row.
So after an odd number of column moves, the blank can not possibly be back in the last row, where it belongs!
Now we can bundle up all these observations and state an invariant, a property of the puzzle that never changes, no matter how you slide the tiles around.

**Lemma**. In every configuration reachable from the position shown below,
the parity of the number of inversions is different from the parity of the row containing the blank square.

.. table::

	+----+-----+-----+-----+-----+
	|row1|  A  |  B  |  C  |  D  |
	+----+-----+-----+-----+-----+
	|row2|  E  |  F  |  G  |  H  |
	+----+-----+-----+-----+-----+
	|row3|  I  |  J  |  K  |  L  |
	+----+-----+-----+-----+-----+
	|row4|  M  |  O  |  N  |     |
	+----+-----+-----+-----+-----+

Prove this lemma.

.. raw:: html

	<hr>

First, we define the row number containing the black square as,

.. math::

	r = \left\lceil {p_b \over n} \right\rceil

where :math:`p_b` is the position of the blank square.

When we do a row move, :math:`p_b \pm 1`.
However, per the rules of the game, this is within the bounds of the grid.
This means the row number cannot change for a row move, thus the parity of the row number cannot change for a row move.

As shown in part (d), a row move does not change the number of inversions, and thus doesn't change the parity of the number of inversions.

For a column move, :math:`p_b \pm n`, again, within the bounds of the grid.
Per the ceiling calculation, increasing or decreasing by n will change r by 1.
Since 1 is an odd number, this changes the parity of the row number for a column move.

As shown in part (c) every column move changes the parity of the number of inversions.
So any row move will flip the parity of both r and the number of inversions.

Therefore, in every configuration reachable from the position shown above,
the parity of the number of inversions is always different to the parity of r.
:math:`\blacksquare`

(f) Prove the theorem that we originally set out to prove.

.. raw:: html

	<hr>

In the initial configuration the row number is 4, which is even.
There is one inversion (O and N), which is odd.

In the desired configuration the row number containing the blank square is 4, which is even.
There are no inversions, i.e. 0, which is even.

As shown in part (e), for any given move, the parity of the row number containing the blank square and the number of inversions will either stay the same or both will change.

Therefore, no sequence of moves transforms the initial configuration into the desired configuration.
:math:`\blacksquare`

Problem 7
---------

There are two types of creature on planet Char, Z-lings and B-lings.
Furthermore, every creature belongs to a particular generation.
The creatures in each generation reproduce according to certain rules and then die off.
The subsequent generation consists entirely of their offspring.

The creatures of Char pair with a mate in order to reproduce.
First, as many Z-B pairs as possible are formed.
The remaining creatures form Z-Z pairs or B-B pairs, depending on whether there is an excess of Z-lings or of B-lings.
If there are an odd number of creatures, then one in the majority species dies without reproducing.
The number and type of offspring is determined by the types of the parents

- If both parents are Z-lings, then they have three Z-ling offspring.

- If both parents are B-lings, then they have two B-ling offspring and one Z-ling offspring.

- If there is one parent of each type, then they have one offspring of each type.

There are 200 Z-lings and 800 B-lings in the first generation.
Use induction to prove that the number of Z-lings will always be at most twice the number of B-lings

.. raw:: html

	<hr>

First we define,

.. math::

	z_n ::= \text{ the number of z-lings at generation n}

	b_n ::= \text{ the number of b-lings at generation n}

where n is any non-negative integer.
The calculation for the number of z-lings or b-lings in the next generation is split into 3 cases,

1. :math:`z_n = b_n`

   .. math::

       z_{n+1} = z_n

       b_{n+1} = b_n

2. :math:`z_n > b_n`

   .. math::

       z_{n+1} = 3 \cdot \left\lfloor {z_n - b_n \over 2} \right\rfloor

       b_n = b_n

3. :math:`z_n < b_n`

   .. math::

       z_{n+1} = \left\lfloor {b_n - z_n \over 2} \right\rfloor

       b_{n+1} = 2 \cdot \left\lfloor {b_n - z_n \over 2} \right\rfloor

**Theorem**:

.. math::

	\forall n \in \Bbb N. z_0 = 200, b_0 = 800. z_n \le b_n

That is, the number of Z-lings is less than or equal to the number of B-lings,
for any non-negative integer generation n, with a starting population of 200 Z-lings and 800 B-lings.

**Proof**. By strong induction, letting the induction hypothesis P(n) be defined as follows,

.. math::

	P(n) ::= z_0 \le b_0 \text{ and } z_1 \le b_1 \text{ and } \dots \text{ and } z_n \le b_n

**Base Case**: P(0) is true because :math:`200 \le 800`.

**Inductive Step**: Assuming P(n) is true, we must prove P(n + 1) is also true.

There are two cases to consider.

If :math:`z_{n} = b_{n}` then, per the constructor, :math:`z_{n+1} = z_{n}`,
and :math:`b_{n+1} = b_{n+1}`, so :math:`z_{n+1} \le b_{n+1}` and the theory holds in this case.

If :math:`z_n < b_n` then, per the constructor,

.. math::

	\begin{aligned}

	z_{n+1} &= \left\lfloor {b_n - z_n \over 2} \right\rfloor \cr

	b_{n+1} &= 2 \cdot \left\lfloor {b_n - z_n \over 2} \right\rfloor \cr

	\end{aligned}

So by inductive hypothesis,

.. math::

	 \left\lfloor {b_n - z_n \over 2} \right\rfloor \le 2 \cdot \left\lfloor {b_n - z_n \over 2} \right\rfloor

Since :math:`z_n < b_n` then :math:`b_n - z_n` must be a non-negative integer.

.. math::

	\begin{aligned}

	i &::= \text{ a non-negative integer} \cr

	\left\lfloor {i \over 2} \right\rfloor &\le 2 \cdot \left\lfloor {i \over 2} \right\rfloor \cr

	\end{aligned}

Dividing a non-negative integer by 2 gives a non-negative real number.

.. math::

	\begin{aligned}

	r &::= \text{ a non-negative real number} \cr

	\left\lfloor r \right\rfloor &\le 2 \cdot \left\lfloor r \right\rfloor \cr

	\end{aligned}

Flooring a non-negative real number gives a non-negative integer.

.. math::

	i \le 2 \cdot i

An integer multiplied by an integer > 1 (in this case, 2) will result in a larger integer.
This proves P(n + 1), so by the principle of induction it follows that P(n) for any non-negative integer n.

If :math:`z_n \le b_n` then :math:`z_n` must be less than :math:`2 b_n`, so the theory holds.
:math:`\blacksquare`
