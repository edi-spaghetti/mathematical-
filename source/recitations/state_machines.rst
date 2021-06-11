State Machines
==============

`problems <link https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/recitations/MIT6_042JF10_rec03.pdf>`_
`<solution link https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/recitations/MIT6_042JF10_rec03_sol.pdf>`_

Breaking a Chocolate Bar
------------------------

We are given a chocolate bar with m × n squares of chocolate, and our task is to divide it into mn individual squares.
We are only allowed to split one piece of chocolate at a time using a vertical or a horizontal break.
For example, suppose that the chocolate bar is 2 × 2.
The first split makes two pieces, both 2 × 1.
Each of these pieces requires one more split to form single squares.
This gives a total of three splits.
Prove that the number of times you split the bar does not depend on the sequence of splits you make.

.. raw:: html

	<hr>

First we define a state machine,

**States**: A sequence of pairs (m, n) where,

.. math::

	\begin{aligned}

	m &= \text{ the number of horizontal squares}

	n &= \text{ the number of vertical squares}

	\end{aligned}

Each pair represents a block that may or may not be split further.

**Start-State**: ( (m, n) )

**Transitions**:

1. Split Horizontally

   .. math::

		...\ ::= \text{ all other existing pairs}

       ( (m, n),\ ... ) \rightarrow ( (m-a, n), (a, n), ... ), m > a \ge 1

2. Split Vertically

   .. math::

		...\ ::= \text{ all other existing pairs}

       ( (m, n),\ ... ) \rightarrow ( (m, n-b), (m, b), ... ), n > b \ge 1

.. note::

	A transition can be applied to one pair at a time.
	This results in 2 new pairs, plus every pair already in the current state.
	Therefore the cardinality of the state increases by 1 on each transition.
	This also gives us the property that the number of transitions is equal to the cardinality of the state,
	minus 1 for the start state.

Let P(t) be the predicate, defined as follows,

.. math::

	t = |state| - 1 \qquad \text{(number of transitions so far)}

	t + \bigg( \sum_{i=0}^t (m_i \cdot n_i) - 1 \bigg) = (m_{initial} \cdot n_{initial}) - 1

That is, at any given number of transitions t (a non-negative integer),
the sum of :math:`(m \cdot n) - 1` applied to each pair in the state plus the number of transitions t, never changes.

**Theorem1**: P(t) holds for all :math:`t \in \{ \Bbb N \mid t \le (m_{initial} \cdot n_{initial}) - 1\}`

**Proof**. By structural induction

**Base Case**: P(0) is trivially true because t = 0 and there is only one pair in the start state

.. math::

	0 + (m \cdot n) - 1 = (m \cdot n) - 1

**Inductive Step**: Now we must show P(t) is true after any transition given that the P(0) is true.
Per the transitions there are two cases to consider.

**Case 1**: Split Horizontally

.. math::

	\begin{aligned}

	t + ((m-a) \cdot n) - 1 + (a \cdot n) - 1 &= (m \cdot n) - 1

	t + mn - an - 1 + an - 1 &= mn - 1

	t + mn - 2 &= mn - 1

	t &= 1

	\end{aligned}

This proves P(t) after any single horizontal split, because the equation is balanced and the number of transitions has increased by 1.

**Case 2**: Split Vertically

.. math::

	\begin{aligned}

	t + (m \cdot n-b) - 1 + (m \cdot b) - 1 &= (m \cdot n) - 1

	t + mn - mb - 1 + mb - 1 &= mn - 1

	t + mn - 2 &= mn - 1

	t &= 1

	\end{aligned}

This proves P(t) after any single vertical split, because the equation is balanced and the number of transitions has increased by 1.

This proves P(t) holds as required, completing the constructor cases.
By structural induction we conclude that P(t) holds for all :math:`t \in \{ \Bbb N \mid t \le (m_{initial} \cdot n_{initial}) - 1\}`.

Now we must prove that :math:`m \cdot n - 1` is the maximum number of transitions.



**Theorem2**: :math:`t = m \cdot n - 1`.

**Proof**: By contradiction.

First, we will assume :math:`t > m \cdot n - 1`.

Starting with minimum values m=1 and n=1,
By the rules of the game, we cannot split an individual square (i.e. a 1 × 1 square) any further.
This means we can have no transitions, so :math:`t = 0`. However by our assumption,

.. math::

	t > m \cdot n - 1

	0 > 1 \cdot 1 - 1

	0 > 0

This is a contradiction, so t cannot be greater than :math:`m \cdot n - 1`.

Second, we can consider :math:`t < m \cdot n - 1`.
Using the same values for m and n, we should again find :math:`t = 0`. However,

.. math::

	t < m \cdot n - 1

	0 < 1 \cdot 1 - 1

	0 < 0

This is also a contradiction, to t cannot be less than :math:`m \cdot n - 1`.

The only possibility remaining then, is that :math:`t = m \cdot n - 1`.

From theorem 2 we showed that the number of total number of splits is equal to :math:`m \cdot n - 1`.
From theorem 1 we showed that with any arbitrary split, the value remains invariant.
This means no matter what sequence of splits is made, the total number of splits is always determined by the initial state.
:math:`\blacksquare`
