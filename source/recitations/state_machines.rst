State Machines
==============

`problems <link https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/recitations/MIT6_042JF10_rec03.pdf>`_
`solution <link https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/recitations/MIT6_042JF10_rec03_sol.pdf>`_

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


The Temple of Forever
---------------------

Each monk entering the Temple of Forever is given a bowl with 15 red beads and 12 green beads.
Each time the Gong of Time rings, a monk must do one of two things:

1. Exchange: If he has at least 3 red beads in his bowl, then he may exchange 3 red beads for 2 green beads.
2. Swap: He may replace each green bead in his bowl with a red bead and replace each red bead in his bowl with a green bead.
   That is, if he starts with i red beads and j green beads, then after he performs this operation, he will have j red beads and i green beads.

A monk may leave the Temple of Forever only when he has exactly 5 red beads and 5 green beads in his bowl.
Let’s look at how we can represent this problem as a state machine.

**What do the states of the machine look like?**

.. raw:: html

	<br>

The states are pairs (i, j) where;

.. math::

	i = \text{ the number of red beads}

	j = \text{ the number of green beads}

**Start-State**: A sequence (i, j) where i = 15 and j = 12

**Use the notation you developed above to represent the allowable transitions in the
state machine.**

.. raw:: html

	<hr>

**Transitions**:

1. Exchange

   .. math::

       (i, j) \rightarrow (i - 3, j + 2), i \ge 3

2. Swap

   .. math::

       (i, j) \rightarrow (j, i)

**Expand the state machine diagram to the first three or four levels.
Label the transitions according to the operation type (E for exchange or S for swap).**

.. raw:: html

	<hr>

::

	(15, 12)
	├── (12, 14)            E
	│   ├── (14, 12)        S
	│   │   ├── (11, 14)    E
	│   │   └── (12, 14)    S
	│   └── (9, 16)         E
	│       ├── (16, 9)     S
	│       └── (6, 18)     E
	└── (12, 15)            S
	    ├── (15, 12)        S
	    │   ├── (12, 14)    E
	    │   └── (12, 15)    S
	    └── (9, 17)         E
	        ├── (17, 9)     S
	        └── (6, 19)     E

Now we’ll show that no monk can ever escape the Temple of Forever because the state :math:`(5, 5)` violates an invariant of the Temple of Forever machine.

**Theorem 1**. No one ever leaves the Temple of Forever.

Prove this theorem by induction.
Begin by searching for an invariant that holds initially and is maintained by each operation,
but would be violated by the condition required for departure.

.. raw:: html

	<hr>

**Invariant**: let P(n) be the proposition that after n transitions,

.. math::

	P(n) ::= i,j,a \in \Bbb N. b \in {2,3}. i - j = 5a + b

That is, the number of red beads minus number of green beads is equal to :math:`5a + b` where a is any integer and b is 2 or 3.

.. note::

	I didn't figure out this invariant myself, I had to check the notes.
	Honestly, I have no idea how it could have been worked out and the notes don't explain it either.

**Base Case**: P(0) is true as shown,

.. math::

	\begin{aligned}

	15 - 12 &= 5a + b

	3 &= 5 \cdot 0 + 3, \text{ where } k = 0, b = 3

	\end{aligned}

**Inductive Step**: Assuming P(n) is true, we must show that P(n + 1) is true.
Per the transitions we must consider two cases;

1. Exchange.

   .. math::

       \begin{aligned}

       (i - 3) - (j + 2) &= 5a + b

       (i - j) - 5 &=

       &= 5(a - 1) + b

       \end{aligned}

   .. note::

       I had to check the notes again here, because they used 5(a - 1) + b as a proof that this is true of P(n + 1), but don't explain why.
       They also don't explain how they make the jump from :math:`(i - j) - 5` to :math:`5(a - 1) + b`.
       It seems wrong because :math:`5(a - 1) + b \ne 5a + b`, so clearly I've missed something.

2. Swap.

   Here the signs change, but the numbers remain the same so,

   .. math::

       \begin{aligned}

       j - i &= 5(-a) - b

       \text{if b = 3}

       &= 5(a - 1) + 2 \qquad && \text{(from the notes)}

       \text{else if b = 2}

       &= 5(a - 1) + 3 \qquad && \text{(from the notes)}

       \end{aligned}

   .. note::

       I also couldn't work this one out.
       Think I may have missed a chapter because some of these explanations seem to be coming from nowhere.

Therefore P(n) implies P(n + 1).

Per the rules of the temple, the state required to leave is (5, 5).
However as we can see, (5, 5) violates P(n),

.. math::

	\begin{aligned}

	5 - 5 &= 5a + b

	\text{if b = 2}

	0 &= 5a + 2

	5a &= -2

	a &= {-2 \over 5} \qquad && \text{ -2 divide 5 is not an integer}

	\text{if b = 3}

	0 &= 5a + 3

	5a &= -3

	a &= {-3 \over 5} \qquad && \text{ -3 divide 5 is not an integer}

	\end{aligned}

Therefore the state of (5, 5) is unreachable, so no-one can leave the temple.
:math:`\blacksquare`

**Theorem 2**. There is a finite number of reachable states in the Temple of Forever machine.
Prove this theorem.
(Hint: First find an invariant that suggests an upper bound on the number of reachable states.
Be sure to prove the invariant.)

.. raw:: html

	<hr>

**Invariant**: Let P(n) be the predicate, defined as,

.. math::

	P(n) ::= \lnot(i + j > 27)

In other words, the total number of beads cannot be larger than the sum of beads at the start state (15 + 12 = 27).

**Base Case**: P(0) is trivially true because 15 + 12 is not larger than 27.

**Inductive Step**: There are two transitions to consider,

1.  Exchange.

	.. math::

		(i - 3) + (j + 2) \le 27

		(i + j) - 1 \le 27

		\text{by P(n) we know } i + j \le 27

	So P(n + 1) is true for exchange.

2.  Swap.

	.. math::

		j + i \le i + j

	So P(n) is true for swap.

That proves P(n), so by the inductive hypothesis we know it is true for P(n + 1).

Given the initial state of (15, 12), the total number of beads is 27.
The number of combinations for any total, t is t + 1
Exchanging decreases the number of beads by 1, and there is no way for the total number of beads to increase.
Therefore, disregarding unreachable states, there are a finite number of states shown below,

.. math::

	s ::=\text{ total number of reachable states}

	s <= \sum^{27}_{i=0} i + 1

	s <= 406

:math:`\blacksquare`

Inside the Temple of Forever, the Gong of Time rings on.
As you may well imagine, the monks begin to recognize that no matter how many ways they try to exchange or swap their beads,
they always seem to end up in some state they’ve already been in before!
For one or two monks, this realization is all they need to propel them instantly into a state of enlightenment.

For the overwhelming majority, however, this knowledge does nothing but weaken their resolve.
They just get depressed. Taking note of the mental state of this second group,
the Keeper of the Temple makes an unannounced appearance and proclaims to the group,
“From now on, any monk who is able to visit 108 (108 being the mystical number that encompasses all of existence)
unique states will be allowed to leave the Temple of Forever.”

Do the monks have any chance of leaving the Temple of Forever?

**Theorem 3**. *It is not possible to visit 108 unique states in the Temple of Forever machine.*

.. raw:: html

	<hr>

**Proof**: By contradiction.

Assuming it is possible to reach 108 states, we consider the transitions.
As shown in theorem 2, every exchange transition decreases the total number of beads by 1.
With a start state of (15, 12) there are 27 total beads.
Also, per the rules, an exchange can only be done if there are more than 3 beads.
So there are a maximum of 27 - 2 = 25 exchange transitions possible.

Each swap transition creates a unique state once per pair.
Since there are 25 exchange transitions possible there are 25 swaps that will create a unique state.
A swap can be done at the start state so this gives an additional unique state for 26 states from swaps.

Then the start-state itself is a unique state, so an additional 1.

In total this gives 25 + 26 + 1 = 52 unique states.

However this contradicts our proposition that 108 states are reachable,
so we can conclude 108 are not reachable, and that the monks still have no chance to leave.
:math:`\blacksquare`
