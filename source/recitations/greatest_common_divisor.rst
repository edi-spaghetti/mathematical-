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
