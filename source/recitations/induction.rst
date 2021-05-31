Induction
=========

`source <link https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/recitations/MIT6_042JF10_rec02.pdf>`_

`solution <link https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/recitations/MIT6_042JF10_rec02_sol.pdf>`_

A Geometric Sum
---------------

Use the well ordering principle, and then induction, to prove that this formula is correct for all real values :math:`r \ne 1`:

.. math:: 1 + r + r^2 + r^3 + ... r^n = {1 - r^{n+1} \over 1 - r}

**Theorem**: :math:`\forall r \in \Bbb R_{\ne 1}. \forall n \in \Bbb N. 1 + r + r^2 + r^3 + ... r^n = {1 - r^{n+1} \over 1 - r}`

**Proof**. by Well Ordering and contradiction

We assume the theorem is false and collect a set of counterexamples;

.. math::

	C ::= \{\ \forall r \in \Bbb R_{\ne 1}. \forall n \in \Bbb N \mid 1 + r + r^2 + r^3 + ... r^n \ne {1 - r^{n+1} \over 1 - r}\ \}

By our assumption that there can be counterexamples, C is a non-empty set.
By the well ordering principle, there should be a smallest element, which we shall refer to as c.

Since c is the smallest counterexample, the theorem should be false for n = c, but true for n < c.
If n is 0, the theorem is true;

.. math::

	\begin{aligned}

	1 &= {1 - r^{0+1} \over 1 - r}

	&= {1 - r \over 1 - r}

	&= 1

	\end{aligned}

So n must be larger than 0. This also means c - 1 must be a non-negative integer.
Since it is less that c, the theorem must be true for it;

.. math::

	1 + r + r^2 + r^3 + ... r^{c-1} = {1 - r^c \over 1 - r}

But then if we add :math:`r^c` to both sides we get;

.. math::

	\begin{aligned}

	1 + r + r^2 + r^3 + ... r^{c-1} + r^c &= {1 - r^c \over 1 - r} + r^c

	&= {1 - r^c + (1 - r) \dotsm r^c \over 1 - r}

	&= {1 - r^c + r^c - r^{c+1} \over 1 - r}

	&= {1 - r^{c+1} \over 1 - r}

	\end{aligned}

So the theorem holds for c after all. This is a contradiction, so the theorem must be true.
:math:`\blacksquare`

**Proof**. By induction

Let P(n) be the predicate defined like so,

.. math::

	P(n)\ ::=\ \forall r \in \Bbb R_{\ne 1}. \forall n \in \Bbb N. 1 + r + r^2 + r^3 + ... r^n = {1 - r^{n+1} \over 1 - r}

That is, for any non-negative integer 'n', with r being any real number not equal to 1,
:math:`1 + r + r^2 + r^3 + ... r^n` is equal to :math:`{1 - r^{n+1} \over 1 - r}`.

**Theorem**: :math:`P(n) \Rightarrow P(n + 1)`

**Base Case**: P(0) is true, because both sides equal 1 when n = 0

.. math::

	\begin{aligned}

	1 &= {1 - r^{0+1} \over 1 - r}

	&= {1 - r \over 1 - r}

	&= 1

	\end{aligned}

Inductive Step: Assuming P(n) is true, where n in a non-negative integer, then;

.. math::

	\begin{aligned}

	1 + r + r^2 + r^3 + ... r^n + r^{n+1} &= {1 - r^{n+1} \over 1 - r} + r^{n+1} \qquad &&\text{(by induction hypothesis)}

	&= {1 - r^{n+1} + ((1 - r) \dotsm r^{n+1}) \over 1 - r}

	& = {1 - r^{n+1} + r^{n+1} - r^{n+2} \over 1 - r}

	&= {1 - r^{n+2} \over 1 - r} \qquad &&\text{(by simple alegebra)}

	\end{aligned}

This proves P(n + 1), so by the principle of induction it follows that P(n) is true for all non-negative n.
:math:`\blacksquare`

Surveyor
--------

A group of m people are split into two subgroups, p and r.
If people in subgroup p learn they are in subgroup p, they leave the group at the end of the day.
People can see what subgroup other people belong to, but cannot see their subgroup.
On day 1, they are told 'There is at least one person in subgroup p'. What happens next?

**Answer**: All people in subgroup p leave at the end of the number of days equal to p

**Proof**. By induction

Let P(n) be the predicate, where the following are true after n number of days have passed;

.. centered:: If p > n, then no-one leaves

.. centered:: If p = n, then all people in subgroup p leave

.. centered:: If p < n, then either everyone leaves or no-one does (see notes below)

**Theorem**: P(n) ⇒ P(n + 1)

**Base Case**: P(1) is true, because it satisfies all three of the conditions in the predicate;

*If p > 1*, each person, regardless of their own subgroup, will see at least
one other person in subgroup p. So they cannot be sure of their own subgroup.
Furthermore, everyone will see that the others came to this conclusion,
so they also know that p > 1.

*If p = 1*, the person in subgroup p will see no others in p, so they have to conclude
that they themselves are in subgroup p. learning this, they must leave the group.
Additionally, the remainder of the group knows that person came to this conclusion,
so they are also able to conclude that there was 1 person in subgroup p,
and that they themselves are in subgroup r.

*If p < 1*, We assume they are told a true fact that there is at least one person
in subgroup p, but even so, is p were less than one that would mean
there are zero people in subgroup p, meaning everyone is in subgroup r,
so no-one learns they are in subgroup p, so no-one leaves.

.. note::

	If we cannot assume they are told a true fact, everyone, seeing only people in subgroup r,
	would (erroneously) conclude they themselves are in subgroup p, and they would all attempt to leave.
	Depending on how attempting to leave under a false conclusion is handled either everyone would leave, or no-one would.

**Inductive Step**: Assuming P(n) is true, we must prove P(n + 1) is also true.
To do this, we must prove that each of the conditions of the predicate are met;

*If p > n + 1*, each person, seeing that no-one left on day n knows that p > n.
A person in subgroup r will see p people in subgroup p and so cannot be sure of their own subgroup.
A person in subgroup p will see p - 1 people in subgroup p.
From what they know so far, it will also appear greater than n to them

.. math::

	p - 1 \ge n + 1 \land p - 1 > n

Seeing that everyone else came to this conclusion, they all know that p > n + 1

*If p = n + 1*, again, from the previous day, they know that p > n.
A person in subgroup r will see p people in subgroup p, and since n + 1 > n, they cannot be sure of their own subgroup.
A person in subgroup p will see p - 1 people in subgroup p.
Seeing this, the only way for p > n is for themselves to be in subgroup p.
Since they've all just learned they're in subgroup p, they all leave.

*If p < n + 1*, on the previous day, everyone learned that p = n, causing everyone in subgroup p to leave.
Because of this fact, everyone in subgroup r was also able to conclude that they were not in subgroup p, meaning they don't leave.

This proves P(n + 1), so by the principle of induction it follows that P(n) is true for all strictly positive n.
:math:`\blacksquare`
