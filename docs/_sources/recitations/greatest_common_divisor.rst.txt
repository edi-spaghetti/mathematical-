Greatest Common Divisors
========================

`problems <link https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/recitations/MIT6_042JF10_rec04.pdf>`_
`solutions <link https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/recitations/MIT6_042JF10_rec04_sol.pdf>`_

The Pulverizer!
---------------

**There is a pond. Inside the pond there are n pebbles, arranged in a cycle.**
**A frog is sitting on one of the pebbles.**
**Whenever he jumps, he lands exactly k pebbles away in the clockwise direction, where 0 < k < n.**
**The frog’s meal, a delicious worm, lies on the pebble right next to his, in the clockwise direction.**

**(a) Describe a situation where the frog can’t reach the worm.**

.. raw:: html

	<hr>

If n and k are not relatively prime, then the frog will not be able to reach the worm.
This is because only steps divisible by the gcd are reachable, and the only number that divides 1 is 1.
:math:`\blacksquare`

**(b) In a situation where the frog can actually reach the worm, explain how to use the Pulverizer to find how many jumps the frog will need.**

.. raw:: html

	<hr>

If the frog is able to reach the worm, then it can do so in j hops,
which is equivalent to m hops around the circle plus 1, for some integers j, m.

.. math::

	\begin{aligned}

	jk &= mn + 1

	1 &= (-m)n + jk

	\end{aligned}

This means 1 is a linear combination of of k and n.
We also know the the gcd is a linear combination of k and n,
and since there can't be any smaller linear combination of k and n than 1, we can conclude gcd(k, n) = 1.

This means we can use the pulverizer to find a linear combination of k and n.
This linear combination is not guaranteed to have the required signs of -m and +j though.
But we can get this by applying the following,

.. math::

	1 = (m - k)n + (n - j)k

**(c) Compute the number of jumps if n = 50 and k = 21. Anything strange? Can you fix it?**

.. math::

	\begin{aligned}

	&gcd(n, k) \qquad && rem(n, k) \qquad &&& = n - jk \cr

	&gcd(50, 21) \qquad && 8 \qquad &&& = 50 - 2 \cdot 21

	& \qquad &&	 \qquad				&&& = n - 2k \cr

	&gcd(21, 8) \qquad && 5 \qquad &&& = 21 - 2 \cdot 8

	& \qquad &&	 \qquad				&&& = k - 2 \cdot (n - 2k)

	& \qquad &&	 \qquad				&&& = -2n + 5k \cr

	&gcd(8, 5) \qquad && 3 \qquad &&& = 8 - 1 \cdot 5

	& \qquad &&	 \qquad				&&& = (n - 2k) - 1 \cdot (-2n + 5k)

	& \qquad &&	 \qquad				&&& = 3n - 7k \cr

	&gcd(5, 3) \qquad && 2 \qquad &&& = 5 - 1 \cdot 3

	& \qquad &&	 \qquad				&&& = (-2n + 5k) - 1 \cdot (3n - 7k)

	& \qquad &&	 \qquad				&&& = -5n + 12k \cr

	&gcd(3, 2) \qquad && 1 \qquad &&& = 3 - 1 \cdot 2

	& \qquad &&	 \qquad				&&& = 3n - 7k - 1 \cdot (-5n + 12k)

	& \qquad &&	 \qquad				&&& = \boxed{8n - 19k}

	\end{aligned}

This would imply -19 jumps, or 19 jumps in the counter-clockwise direction.
However, the rules state that the frog can only jump clockwise.

19 jumps, in fact, get the frog one stone short of the original position,

.. math::

	8 \cdot 50 = 19 \cdot 21 - 1

Since there are 50 stones in total, each set of 19 jumps moved the frog 1 stone counter-clockwise.
So to move 49 stones counter-clockwise (which is the same as 1 stone clockwise) the frog needs :math:`19 \cdot 49 = 931` jumps.
:math:`\blacksquare`

The Fibonacci numbers
---------------------

**The Fibonacci numbers are defined as follows:**

.. math::

	F_0 = 0 \qquad F_1 = 1 \qquad F_n = F_{n−1} + F_{n−2} \text{ (for n ≥ 2).}

**Give an inductive proof that the Fibonacci numbers** :math:`\ F_n\ ` **and** :math:`\ F_{n+1}\ ` **are relatively prime for all** :math:`\ n \ge 0`.

.. raw:: html

	<hr>

Let P(n) be the predicate, defined as follows,

.. math::

	\forall n \in \Bbb N. gcd(F_n, F_{n+1}) = 1

that is, for all integers greater than or equal to 0, the fibonacci number at :math:`F_n` is relatively prime to the fibonacci number at :math:`F_{n+1}`.

**Theorem** P(n) holds for all n :math:`\in \Bbb N`

**Proof**: By induction.

**Base Case**: P(0) is trivially true,

.. math::

	F_0 = 0

	F_1 = 1

	gcd(0, 1) = 1

**Inductive Step**: We must show P(n+1) holds, given P(n) holds.

Suppose :math:`F_{n+1}` and :math:`F_{n+2}` are not relatively prime.
Then there exists a common divisor, d, such that :math:`d > 1`.
Since it's a common divisor, it also divides a linear combination,

.. math::

	\begin{aligned}

	d & \mid F_{n+2} - F_{n+1}

	& \mid (F_{n+1} + \cancel{F_n}) - (\cancel{F_n} + F_{n-1})

	& \mid F_{n+1} - F_{n-1}

	& \mid F_n \qquad && \text{ proof?}

	\end{aligned}

But by the inductive hypothesis :math:`gcd(F_n, F_{n+1}) = 1`, so d cannot divide :math:`F_n` if d is greater than 1.
This is a contradiction, so we can conclude that :math:`F_{n+1}` and :math:`F_{n+2}` are relatively prime,
and thus by induction P(n) is true for all n.
:math:`\blacksquare`

Power of 3
----------

Let N be a number whose decimal expansion consists of :math:`3^n` identical digits.
Show by induction that :math:`3^n \mid N`. For example:

.. math::

	3^2 \mid \underbrace{777777777}_{3^2\ =\ 9 \text{ digits}}

.. raw:: html

	<hr>

**Corollary**: :math:`3 \mid N`

The decimal representation of N is a sequence of digits, a, of length :math:`3^n`,

.. math::

	\begin{aligned}

	N_{a,n} = \sum_{i=0}^{3^n - 1} a_{3^n - i} \cdot 10^i

	\end{aligned}

Since :math:`10 \text{ mod 3 } = 1`, and any power of 10 mod 3 also equals 1,
We can conclude that for any :math:`a_i \in N`,

.. math::

	\begin{aligned}

	a_i \cdot 10^i &≡ \text{ (mod 3) }

	a_i \cdot 1 &≡ \text{ (mod 3) }

	a_i &≡ \text{ (mod 3) }

	\end{aligned}

So each item in the sequence N (mod 3) is equal to :math:`a_i`.
In our case, each item :math:`a_i` is the same integer, so,

.. math::

	\begin{aligned}

	{a \cdot 3^n \over 3} &≡ 0 \text{ (mod 3) }

	3 (a \cdot 3^{n-1}) &≡ 0 \text{ (mod 3) }

	\end{aligned}

So we can conclude N is divisible by 3 for any value of a and n :math:`\square`.

**Theorem**: :math:`\forall n \in \Bbb N_+. \forall a \in [1..9]. 3^n \mid N_{a,n}`.

That is, for all n greater than 0, and any single digit a (except 0), :math:`3^n` divides :math:`N_{a,n}` as defined in the question.

**Base Case**: P(0) can be calculated as follows,

.. math::

	\begin{aligned}

	3^0 &\mid \sum_{i=0}^{3^0 - 1} a \cdot 10^i

	1 &\mid \sum_{i=0}^0 a \cdot 10^i

	1 &\mid 0 \qquad &&\text{0 terms to sum, so total is 0}

	\end{aligned}

Since zero is divisible by anything, this proves the base case.

**Inductive Step**: We must show P(n+1) holds given than P(n) holds.

.. math::

	\begin{aligned}

	N_{a,n+1} &= \sum_{i=0}^{3^n - 1} a_{3^n - i} \cdot 10^i + \sum_{j=3^n}^{3^{n+1} - 1} a_{3^{n+1}} \cdot 10^j \cr

	\exists b \in \Bbb N_+,

	&= 3^n \cdot b + \sum_{j=3^n}^{3^{n+1} - 1} a_{3^{n+1}} \cdot 10^j
		\qquad && \text{ (by inductive hypothesis)} \cr

	\exists c \in \Bbb N_+,

	&= 3^n \cdot b + 3 \cdot c
		\qquad && (3^{n+1} - 3^n = 3) \cr

	\exists d \in \Bbb N_+,

	&= 3^{n+1} \cdot d

	\end{aligned}

That is, we know the first term (reduced to b) is divisible by :math:`3^n` from the inductive hypothesis.
The second term (reduced to c) is divisible by 3, because there are a multiple of 3 terms to sum from :math:`3^n \text{ to } 3^{n+1}`)

So in total, the terms added together (reduced to d) are divisible by :math:`3^{n+1}`.
This proves P(n+1).

By induction, P(n) is true for for all :math:`n \ge 0`.
:math:`\blacksquare`
