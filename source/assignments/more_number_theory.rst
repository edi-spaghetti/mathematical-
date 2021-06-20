More Number Theory
==================

Problem 1 - Warmup Exercises
----------------------------

For the following parts, a correct numerical answer will only earn credit if accompanied by it’s derivation.
Show your work.

**(a) Use the Pulverizer to find integers s and t such that 135s + 59t = gcd(135, 59).**

.. raw:: html

	<hr>

.. math::

	\begin{aligned}

	&gcd(x, y) \qquad && rem(x, y) \qquad &&& = a - qb

	&gcd(135, 59) \qquad && 17 \qquad &&& = 135 - 2 \cdot 59

	& \qquad &&	 \qquad				&&& = a - 2 \cdot b

	&gcd(59, 17) \qquad && 8 \qquad &&& = 59 - 3 \cdot 17

	& \qquad &&	 \qquad				&&& = b - 3 \cdot ( a - 2 \cdot b )

	& \qquad &&	 \qquad				&&& = -3a + 7b

	&gcd(17, 8) \qquad && 1 \qquad &&& = 17 - 2 \cdot 8

	& \qquad &&	 \qquad				&&& = a - 2 \cdot b - 2 \cdot ( -3a + 7b )

	& \qquad &&	 \qquad				&&& = \boxed{7a - 16b}

	&gcd(8, 1) \qquad && 0

	\end{aligned}

By application of the pulveriser, for :math:`135s + 59t = gcd(135, 59)`, s = 7 and t = -16.
:math:`\blacksquare`

**(b) Use the previous part to find the inverse of 59 modulo 135 in the range {1, . . . , 134}.**

.. raw:: html

	<hr>

.. math::

	\begin{aligned}

	& a = qb + r \qquad && p_i = p_{i-2} - p_{i-1} \cdot q_{i-2} \text{(mod b)}

	& 135 = 2 \cdot 59 + 17 && p_0 = 0

	& 59 = 3 \cdot 17 + 8 && p_1 = 1

	& 17 = 2 \cdot 8 + 1 && 0 - 1 \cdot 2 \text{ mod 135 } = 133

	& 8 = 8 \cdot 1 + 0 && 1 - 133 \cdot 3 \text{ mod 135 } = 7

						&& 133 - 7 \cdot 2 \text{ mod 135 } = \boxed{119}

	\end{aligned}

Reading through the book, I also discovered you can apply the General Principle of Remainder Arithmetic;

.. math::

	\begin{aligned}

	sa + tb &= 1 = 7a - 16b

	rem(s, a) \cdot rem(a, a) + rem(t, a) \cdot rem(b, a) &= 1 \text{ (mod a) }

	rem(t, a) \cdot b &= 1 \text{ (mod a) }, \qquad && rem(t, a) \text{ is the inverse of b}

	rem(-16, 135) \cdot 59 &= 1 \text{ (mod 135) } \qquad && \text{(plugging the numbers in)}

	\boxed{119} \cdot 59 &= 1 \text{ (mod 135) }

	\end{aligned}

**(c) Use Euler’s theorem to find the inverse of 17 modulo 31 in the range {1, . . . , 30}.**

.. raw:: html

	<hr>

By Euler's theorem :math:`gcd(k, n) = 1 \rightarrow k^{\phi (n) - 1}` is the inverse of k (mod n).
17 and 31 are both prime numbers, so by definition the gcd = 1,
so we can a calculate the inverse, i, as :math:`17^{\phi(31) - 1}`;

.. math::

	\begin{aligned}

	i &= 17^{\phi(31) - 1} \text{ (mod 31) }

	&= 17^{(30^1 - 30^0) - 1} \text{ (mod 31) }

	&= 17^{29} \text{ (mod 31) }

	&= 11

	\end{aligned}

The inverse of 17 modulo 31 is 11.
:math:`\blacksquare`

**(d) Find the remainder of :math:`34^{82248}` divided by 83. (Hint: Euler’s theorem.)**

First we need to check that 83 is prime, which we can do by checking each integer in :math:`[2..\lfloor \sqrt{83} \rfloor]`.
We can find the upper bound is 9, because 83 is between :math:`9^2 = 81` and :math:`10^2 = 100`
83 is not divisible by 2, 3, 4, 5, 6, 7, 8 or 9 so we can conclude 83 is prime.

.. math::

	34^{\phi(83)} &≡ 1 \text{ (mod 83) } \qquad && \text{(by Euler's theorem)}

	\phi(83) &= (83^1 - 83^0) \qquad && \text{(because 83 is prime)}

	&= 82

	34^{82} &≡ 1 (mod 83)

	r &≡ 34^{82246} \cdot 34^2 \text{ (mod 83) }

	&≡ 34^{(82)(1003)} \cdot 34^2 \text{ (mod 83) } && \qquad \text{82246 is a factor of 82}

	&≡ 1 \cdot 34^2 \text{ (mod 83) } \qquad && \text{and so congruent to the above}

	&≡ 1156 \text{ (mod 83) }

	&≡ 77

77 is the remainder of :math:`34^{82248}` divided by 83.
:math:`\blacksquare`
