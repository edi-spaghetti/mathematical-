Propositions and Proofs
=======================

Problem 1
---------

*Using the following definitions, convert English sentences into predicate logic,*

::

	X is the set of people
	S(x) ::= x has been a student of 6.042
	A(x) ::= x got an A on 6.042
	T(x) ::= x is a TA on 6.042
	E(x,y) ::= x and y are the same person

a) *There are people who have taken 6.042 and have gotten A’s in 6.042*

.. math:: \exists \in  X. S(x) \land A(x)

b) *All people who are 6.042 TA’s and have taken 6.042 got A’s in 6.042*

.. math:: \exists \in X. T(x) \land A(x)

c) *There are no people who are 6.042 TA’s who did not get A’s in 6.042*

.. math:: \forall\ x \in X.\ \lnot A(x) \Rightarrow A(x)

d) *There are at least three people who are TA’s in 6.042 and have not taken 6.042*

.. math:: \exists x,\exists y,\exists z \in X.
			\lnot E(x,y) \land \lnot E(x,z) \land \lnot E(y,z)
			\land (T(x) \land \lnot S(x))
			\land (T(y) \land \lnot S(y))
			\land (T(z) \land \lnot S(z))

Problem 2
---------

*Use a truth table to prove or disprove the following statements:*

a) :math:`\lnot (P \lor (Q \land R)) = (\lnot P) \land (\lnot Q \lor \lnot R)`

.. list-table::
	:header-rows: 1

	* - P
	  - Q
	  - R
	  - :math:`\lnot (P \lor (Q \land R))`
	  - :math:`\lnot (P) \land (\lnot Q \lor \lnot R)`
	* - F
	  - F
	  - F
	  - T
	  - T
	* - F
	  - F
	  - T
	  - T
	  - T
	* - F
	  - T
	  - F
	  - T
	  - T
	* - F
	  - T
	  - T
	  - F
	  - F
	* - T
	  - F
	  - F
	  - F
	  - F
	* - T
	  - F
	  - T
	  - F
	  - F
	* - T
	  - T
	  - F
	  - F
	  - F
	* - T
	  - T
	  - T
	  - F
	  - F

They're all the same, so they are equal. For fun I ran this in python to verify.

.. code-block:: python

	from itertools import product
	X = product([True, False], repeat=3)
	result = 'Proved'
	for P, Q, R in X:
		if not (P or (Q and R)) != (not P) and (not Q or not R):
			print((P, Q, R))
			result = 'Disproved'
	print(result)
	# >>> Proved

b) :math:`\lnot (P \land (Q \lor R)) = \lnot P \lor (\lnot Q \lor \lnot R)`

.. list-table::
	:header-rows: 1

	* - P
	  - Q
	  - R
	  - :math:`\lnot (P \land (Q \lor R))`
	  - :math:`\lnot P \lor (\lnot Q \lor \lnot R)`
	* - F
	  - F
	  - F
	  - T
	  - T
	* - F
	  - F
	  - T
	  - T
	  - T
	* - F
	  - T
	  - F
	  - T
	  - T
	* - F
	  - T
	  - T
	  - T
	  - T
	* - T
	  - F
	  - F
	  - T
	  - T
	* - T
	  - F
	  - T
	  - **F**
	  - **T**
	* - T
	  - T
	  - F
	  - **F**
	  - **T**
	* - T
	  - T
	  - T
	  - F
	  - F

Two discrepancies at TFT and TTF. I ran it through python again, to check my answers.

.. code-block:: python

	from itertools import product
	X = product([True, False], repeat=3)
	result = 'Proved'
	for P, Q, R in X:
		if not (P and (Q or R)) != (not P or (not Q or not R)):
			print((P, Q, R))
			result = 'Disproved'
	print(result)
	# >>> (True, True, False)
	# >>> (True, False, True)
	# >>> Disproved


Problem 3
---------

a) *Find equivalent expressions using only* :math:`\barwedge` *(nand) and* :math:`\lnot` *(not).*

i) :math:`A \land B`

.. math:: \lnot (A \barwedge B)

ii) :math:`A \lor B`

.. math:: (\lnot A) \barwedge (\lnot B)

iii) :math:`A \Rightarrow B`

.. math:: \lnot A \barwedge (\lnot B)

b) *Find an equivalent expression for (* :math:`\lnot` *A) using only nand and grouping parentheses*

.. math:: (A \barwedge A)

c) *The constants true and false themselves may be expressed using only nand.*

i) *Construct an expression using an arbitrary statement A and nand that evaluates to true regardless of whether A is true or false*

.. math:: (A \barwedge A) \barwedge A

ii) *Construct a second expression that always evaluates to false*

.. math:: ((A \barwedge A) \barwedge A) \barwedge ((A \barwedge A) \barwedge A)

Problem 4
---------

*12 coins and a balance scale, one coin is fake.
All real coins weigh the same, but the fake coin weighs less than the rest.
In at most 3 weighings, give a strategy that detects the fake coin.*


Reliable Strategy
"""""""""""""""""

(guaranteed to find fake in exactly 3 weighings)

1. 6 on each side of the scale, discard the heavier side
2. 3 on each side of scale, discard the heavier side
3. 1 on each side, if balanced, the third coin is fake, else the lighter side is the fake

High Risk - High Reward Strategy
""""""""""""""""""""""""""""""""

(could find fake on first try, might not find it at all)

1. Randomly pick two coins and place on each side of scale. If unbalanced, the lighter side is the fake else discard both coins.
2. Repeat until fake is found or 3 weighings

Best Strategy
"""""""""""""

(could find fake in 2 weighings, definitely in 3)

1. 4 on each side, with 4 remainder. If balanced, discard both, as fake is in remainder else discard heavier side and remainder.
2. 1 on each side, 2 remainder. If unbalanced, the lighter side is the fake, else discard both.
3. (if necessary) 1 on each side the lighter side is the fake.

Problem 5
---------

*Prove the following statement by proving its contrapositive: if r is irrational, then* :math:`r^{1/5}` *is irrational.*

We define the following to write out our theorem:

.. centered:: P(r) ::= r is irrational

.. centered:: :math:`r^{1/5}` is irrational

**Theorem**: :math:`\forall r \in \Bbb R. P(r) \Rightarrow Q(r)`

**Proof**: we prove by contrapositive if :math:`r^{1/5}` is rational, then r is rational.
Assuming :math:`r^{1/5}` is rational, we can assume the following

**lemma 1**: `rational numbers are equal to a ratio of two integers <link https://proofwiki.org/wiki/Definition:Rational_Number>`_

.. math::

	\begin{aligned}

	\forall c \in \Bbb Q. \exists a \in \Bbb Z. \exists b \in \Bbb Z_{\ne 0}. c &= {a \over b}

	r^{1/5} &= {a \over b}

	r &= \sqrt[5]{{a \over b}}

	\end{aligned}

**lemma 2**: `the nth root of non-integers are irrational <link https://proofwiki.org/wiki/Nth_Root_of_Integer_is_Integer_or_Irrational>`_

If r is rational, then a / b must be an integer.
From lemma 1, a and b are coprime with gcd(a, b) = 1.
This means for :math:`{a \over b}` to be an integer, b must equal 1.

.. math::

	\begin{aligned}

	r &= {a^5 \over b^5}

	&= {a^5 \over 1^5}

	&= a^5

	\end{aligned}

Since a is an integer, :math:`a^5` is also an integer, because integers are closed under multiplication.
It therefore follows that r is also an integer, i.e. rational. :math:`\blacksquare`

Problem 6
---------

*Suppose that* :math:`w^2 + x^2 + y^2 = z^2` *, where w x y and z are positive integers.
Prove the proposition z is even if and only if w, x and y are even.*

First, we define the following:

.. centered:: The domain of discourse is all positive integers (:math:`\Bbb Z^+`)

.. centered:: E(n) ::= n is even

**Theorem**: :math:`\forall w,x,y \exists z. ((w^2 + x^2 + y^2 = z^2) \Rightarrow E(z)) \Leftrightarrow E(w) \land E(x) \land E(y)`

That is, given the formula :math:`w^2 + x^2 + y^2 = z^2`, where w, x, y and z are positive integers,
z is even if and only if w, x and y are all even.

**Proof**: We shall prove by cases

Lemma 1: All odd integers can be rewritten as :math:`2i + 1` where i is an integer.

.. math:: \forall k \exists i. \lnot E(k) \Rightarrow (2i + 1 = k)

All even integers can be rewritten as :math:`2j` where j is an integer.

.. math:: \forall k \exists j. E(k) \Rightarrow (2j = k)

Using lemma 1, in each case, w,x,y and z will be rewritten as multiple of integers a, b, c and d respectively.

**Case 1**: All three of :math:`\{x,y,z\}` are odd, i.e.

.. math:: \lnot E(w) \land \lnot E(x) \land \lnot E(y)

We can then rewrite the formula as follows,

.. math::

	\begin{aligned}

	(2a + 1)^2 + (2b + 1)^2 + (2c + 1)^2 &= (2d)^2 \qquad && \text{(by lemma 1)}

	4a^2 + 1 + 4b^2 + 1 + 4c^2 + 1 &= 4d^2 \qquad && \text{(by simple algebra)}

	4a^2 + 4b^2 + 4c^2 + 3 &= 4d^2

	{4a^2 + 4b^2 + 4c^2 + 3 \over 4} &= d^2

	a^2 + b^2 + c^2 + {3 \over 4} &= d^2

	\end{aligned}

a, b, c and d are integers, meaning their squares are also integers.
Integers added together result in an integer, so we get,

.. math:: integer + {3 \over 4} = integer

Adding 0.75 to any integer cannot result in an integer.
This is a contradiction, so w, x and y cannot all be odd.

**Case 2**: One of :math:`\{x,y,z\}` is even, the others are odd e.g.

.. math:: E(w) \land \lnot E(x) \land \lnot E(y)

We can then rewrite the formula as follows,

.. math::

	\begin{aligned}

	(2a)^2 + (2b + 1)^2 + (2c + 1)^2 &= (2d)^2 \qquad && \text{(by lemma 1)}

	4a^2 + 4b^2 + 1 + 4c^2 + 1 &= 4d^2 \qquad && \text{(by simple algebra)}

	4a^2 + 4b^2 + 4c^2 + 2 &= 4d^2

	{4a^2 + 4b^2 + 4c^2 + 2 \over 4} &= d^2

	a^2 + b^2 + c^2 + {1 \over 2} &= d^2

	\end{aligned}

Following the same reasoning as case 1, we end up with,

.. math:: integer + {1 \over 2} = integer

Adding 0.5 to any integer cannot result in an integer.
This is a contradiction, so one of :math:`\{w,x,y\}` cannot be even.

**Case 3**: Two out of :math:`\{w,x,y\}` are even, the other is odd e.g.

.. math:: E(w) \land E(x) \land \lnot E(y)

We can then rewrite the formula as follows,

.. math::

	\begin{aligned}

	(2a)^2 + (2b)^2 + (2c + 1)^2 &= (2d)^2 \qquad && \text{(by lemma 1)}

	4a^2 + 4b^2 + 4c^2 + 1 &= 4d^2 \qquad && \text{(by simple algebra)}

	4a^2 + 4b^2 + 4c^2 + 1 &= 4d^2

	{4a^2 + 4b^2 + 4c^2 + 1 \over 4} &= d^2

	a^2 + b^2 + c^2 + {1 \over 4} &= d^2

	\end{aligned}

Again, we end up with,

.. math:: integer + {1 \over 4} = integer

Adding 0.25 to any integer cannot result in an integer.
This is a contradiction, so two of :math:`\{w,x,y\}` cannot be even.

**Case 4**: They're all even i.e.

.. math:: E(w) \land E(x) \land E(y)

We can then rewrite the formula as follows,

.. math::

	\begin{aligned}

	(2a)^2 + (2b)^2 + (2c)^2 &= (2d)^2 \qquad && \text{(by lemma 1)}

	4a^2 + 4b^2 + 4c^2 &= 4d^2 \qquad && \text{(by simple algebra)}

	4a^2 + 4b^2 + 4c^2 &= 4d^2

	{4a^2 + 4b^2 + 4c^2 \over 4} &= d^2

	a^2 + b^2 + c^2 &= d^2

	\end{aligned}

As before, this gives us,

.. math:: integer\ =\ integer

Which is true, so the theorem holds true in this case.

Case 4 is the only case where the theorem can be true, thus proving the if and only if relationship.
:math:`\blacksquare`
