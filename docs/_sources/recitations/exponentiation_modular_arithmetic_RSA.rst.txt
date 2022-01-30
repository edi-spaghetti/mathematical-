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

	d.  Now you will need to find a d such that :math:`de ≡ 1\ \big( mod\ (p − 1)(q − 1) \big)`.

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

	\begin{aligned}

	gcd \big( e, (7 - 1)(13 - 1) \big) &= 1

	gcd(e, 72) &= 1

	e &= 31

	\end{aligned}

Now we have to find a secret d. With division theorem, we can rewrite :math:`de ≡ 1\ \big( mod\ (p − 1)(q − 1) \big)` into,

.. math::

	\begin{aligned}

	de - 1 &= k \cdot (p - 1)(q - 1) && \exists k \in \Bbb Z \cr

	d \cdot e - k \cdot (p - 1)(q - 1) &= 1

	\end{aligned}

This gives a linear combination of e and :math:`(p-1)(q-1)` where d is the multiplicative inverse of e.
Since we already know :math:`gcd(e,(p − 1)(q − 1)) = 1`, we know it exists.

Using the pulverizer we can find the coefficient of that linear combination.
If it is negative, we can apply,

.. math::

	1 = (s - y) \cdot x + (x - t) \cdot y

In our equation that looks like,

.. math::

	1 = (s - (p − 1)(q − 1)) \cdot e + (e - t) \cdot (p − 1)(q − 1)

However, as it turns out, this is not necessary, because the pulveriser yields,

.. math::

	\begin{aligned}

	1 &= 7 \cdot e - 3 \cdot (p - 1)(q - 1)

	&= \boxed{7} \cdot 31 - 3 \cdot 72

	&= 217 - 216

	\end{aligned}

The value for d is boxed.

Using Euler's Theorem instead, and the fact e and :math:`(p - 1)(q - 1)` are relatively prime, we know that,

.. math::

	e^{\phi \big( (p - 1)(q - 1) \big)} ≡ 1 \ (mod\ (p − 1)(q − 1))

From this, it follows that the inverse of e (mod :math:`(p − 1)(q − 1)`) is d.
It can be calculated as,

.. math::

	\begin{aligned}

	e^{\phi \big( (p - 1)(q - 1) \big) - 1} \cdot e &≡ 1 \ (mod\ (p − 1)(q − 1))

	d &= 31^{\phi(72) - 1} \ (mod\ 72)

	\end{aligned}

We can then work out Euler's totient function as follows,

.. math::

	\begin{aligned}

	\phi(72) - 1 &= (2^3 - 2^2)(3^2 - 3^1) - 1 \qquad && \text{factorisation of 72}

	&= (2^3 - 2^2)(3^2 - 3^1) - 1

	&= 2 \cdot 3 - 1

	&= 5

	\end{aligned}

This could be be an extremely large number, but we can reduce it by applying repeated squaring.

.. math::

	\begin{aligned}

	31^2 &≡ 25 \ (mod\ 72)

	31^4 &≡ 49

	\end{aligned}

Well, doesn't look like repeated squaring helps us much here...
Anyway,

.. math::

	31^5 \ (mod\ 72) = 7

Which is the same answer we got from the pulveriser. Hurray!

2.  **Now ask your recitation instructor for a message to encrypt and send to another team using their public key.**

	The messages m correspond to statements from the codebook below:

	2 = Greetings and salutations!

	3 = Wassup, yo?

	4 = You guys are slow!

	5 = All your base are belong to us.

	6 = Someone on our team thinks someone on your team is kinda cute.

	7 = You are the weakest link. Goodbye

.. raw:: html

	<hr>

My wife chose 6. Coincidence? Maybe...

3. **Encode the message you were given using another team’s public key.**

.. raw:: html

	<hr>

.. math::

	\begin{aligned}

	m &= 6

	m` &= rem(m^e, n)

	&= rem(6^31, 91)

	6^2 = 36,\ &mod\ 91 = 36

	6^4 = 1296,\ &mod\ 91 = 22

	6^8 = 1679616,\ &mod\ 91 = 29

	&= 6^{8+8+8+4+2+1} \ (mod\ 91)

	&= 29^3 \cdot 22 \cdot 36 \cdot 6 \ (mod\ 91)

	&= 1 \cdot 22 \cdot 36 \cdot 6 \ (mod\ 91)

	&= 4752 \ (mod\ 91)

	&= 20

	\end{aligned}

4. **Now decrypt the message sent to you and verify that you received what the other team sent!**

.. raw:: html

	<hr>

Since I don't have any classmates, I'll just decode my own message :')

.. math::

	\begin{aligned}

	m &= rem((m`)^d, n)

	&= rem(20^7, 91)

	20^2 = 400,\ &mod\ 91 = 36

	20^4 = 160000,\ &mod\ 91 = 22

	&= 20^{4+2+1} \ (mod\ 91)

	&= 22 \cdot 36 \cdot 20 \ (mod\ 91)

	&= 15840 \ (mod\ 91)

	&= 6

	\end{aligned}

Huzzah! Someone on my team thinks someone on my team is kinda cute ;)

5. **Explain how you could read messages encrypted with RSA if you could quickly factor large numbers.**

.. raw:: html

	<hr>

If you can factor n back into p and q, you can work out the rest following the steps we've just gone through.