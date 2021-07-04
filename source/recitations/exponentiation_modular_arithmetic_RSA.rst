RSA
===

You’ll probably need extra paper. Check your work carefully!

1.  As a team, go through the beforehand steps.

	a.  Choose primes p and q to be relatively small, say in the range 5-15.
		In practice, p and q might contain several hundred digits, but small numbers are easier to handle with pencil and paper.

	b.  Calculate n = pq. This number will be used to encrypt and decrypt your messages.

	c.  Find an :math:`e > 1` such that :math:`gcd(e,(p − 1)(q − 1)) = 1`.
		The pair (e, n) will be your public key.
		This value will be broadcast to other groups, and they will use it to send you messages.

	d.  Now you will need to find a d such that :math:`de ≡ 1\ (mod\ (p − 1)(q − 1))`.

		-   Explain how this could be done using the Pulverizer. (Do not carry out the computations!)
		-   Find d using Euler’s Theorem given in yesterday’s lecture.
			The pair (d, n) will be your secret key. Do not share this with anybody!

When you’re done, write your public key and group members’ names on the board.

.. raw:: html

	<hr>

First pick p and q. I'm going to choose lucky number 7 and unlucky 13. Perfectly balanced.

.. math::

	p = 7, q = 13

Now calculate the product of those primes;

.. math::

	n = 7 \cdot 13 = 91

Next find a value for e,

.. math::

	gcd \big( e, (7 - 1)(13 - 1) \big) = 1

	gcd(e, 72) = 1

	e = 31

Now we have to find a secret d,

.. math::

	d \cdot 31 ≡ 1\ (mod\ 72)

	d = 7