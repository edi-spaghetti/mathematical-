Sums and Asymptotics
====================

Problem 1
---------

.. admonition:: Question

	Express

	.. math::

		\sum\limits_{i=0}^{n} i^2 x^i

	as a closed-form function of n.

First, I tried the perturbation method, by multiplying the original expression by x.

.. math::

	\begin{aligned}

	S = \sum\limits_{i=0}^{n} i^2 x^i &= (0^2 \cdot x^0) + (1^2 \cdot x^1) + (2^2 \cdot x^2) + \dots + (n^2 \cdot x^n)

	&= x + 4x^2 + \dots + n^2x^n

	xS &= x^2 + 4x^3 + \dots + (n-1)^2x^n + n^2n^{n+1}

	\end{aligned}

The subtracting one from the other gives us;

.. math::

	\begin{aligned}

	(1-x)S &= x + 4x^2 + \dots + n^2x^n

	-& \qquad x^2 + 4x^3 + \dots + (n-1)^2x^n + n^2n^{n+1} \cr

	&= x + 3x^2 + 5x^3 + \dots + (n^2x^n - (n-1)^2x^n) - n^2x^{n+1}

	\end{aligned}

However, this doesn't cancel out neatly, so next I tried the differential method;

Starting with the closed form of the sum of increasing exponents (which was proved in the lecture);

.. math::

	\sum\limits_{i=0}^{n} x^i = {1 - x^{n+1} \over 1 - x}

To get the desired form, we can iteratively take the derivative, then multiply up by x;

.. math::

	\begin{aligned}

	{\delta \over \delta x}\left[ \sum\limits_{i=0}^{n} x^i \right] &= \sum\limits_{i=0}^{n} ix^{i-1} \qquad &&\text{power rule} \cr

	x \cdot \sum\limits_{i=0}^{n} ix^{i-1} &= \sum\limits_{i=0}^{n} ix^i \qquad &&\text{multiply by x} \cr

	{\delta \over \delta x}\left[ \sum\limits_{i=0}^{n} ix^i \right] &= \sum\limits_{i=0}^{n} i^2x^{i-1} \qquad &&\text{take deriv again} \cr

	x \cdot \sum\limits_{i=0}^{n} i^2x^{i-1} &= \sum\limits_{i=0}^{n} i^2x^i \qquad &&\text{multiply by x again} \cr

	\end{aligned}

If we apply this to the other side of the equation we get;

.. math::

	\begin{aligned}

	{\delta \over \delta x}\left[ {1 - x^{n+1} \over 1 - x} \right] &= {\delta \over \delta x}\left[ (1 - x^{n+}) \cdot (1 - x)^{-1} \right]

	\end{aligned}

By separating the terms and applying the product rule we get two functions of x,
of which we can find their derivatives;

.. math::

	\begin{aligned}

	g(x) &= 1 - x^{n+1}

	g'(x) &= {\delta \over \delta x}\left[ 1 \right] - {\delta \over \delta x}\left[ x^{n+1} \right]

	&= 0 - (n+1)x^n

	h(x) &= (1 - x)^{-1}

	&\text{this require u substitution,}

	u &= 1 - x

	{\delta \over \delta x}\left[ 1 - x \right] &= {\delta \over \delta x}\left[ 1 \right] - {\delta \over \delta x}\left[ x \right]

	&= 0 - 1

	\delta u &= - \delta x

	h(x) &= u^{-1}

	h'(x) &= - {\delta \over \delta u}\left[ u^{-1} \right]

	&= - (- u ^ {-2})

	&= (1 - x)^{-2}

	\end{aligned}

We can then apply the product rule to finish the first closed form,

.. math::

	\begin{aligned}

	{\delta \over \delta x}\left[ (1 - x^{n+1}) \cdot (1 - x)^{-1} \right] &= -(n+1)x^n \cdot (1 - x)^{-1} + (1 - x^{n+1}) \cdot (1-x)^{-2}

	&= {-(n+1)x^n \over 1 - x} + {1 - x^{n+1} \over (1 - x)^ 2}

	&= {-(1-x)(n+1)x^n \over (1 - x)^{-2}} + {1 - x^{n+1} \over (1 - x)^ 2}

	&= {-(1-x)(n+1)x^n + 1 - x^{n+1} \over (1 - x)^2}

	&= {-((n+1)x^n - (n+1)x^{n+1}) + 1 - x^{n+1} \over (1 - x)^2}

	&= {1 - (n+1)x^n + nx^{n+1} \over (1 - x)^2}

	\end{aligned}

Then we need to multiply by x to get,

.. math::

	i(x) = {x - (n+1)x^{n+1} + nx^{n+2} \over (1 - x)^2}

Now we need to take the derivative again,

.. math::

	\begin{aligned}

	j(x) &= x - (n+1)x^{n+1} + nx^{n+2}

	j'(x) &= {\delta \over \delta x}\left[ x \right] - {\delta \over \delta x}\left[ (n+1)x^{n+1} \right] + {\delta \over \delta x}\left[ nx^{n+2} \right]
	\cr \cr

	&\text{first term is trivial}

	{\delta \over \delta x}\left[ x \right] &= 1
	\cr \cr

	&\text{second term requires applying the power rule}

	k(x) &= (n+1)x^{n+1}

	&l(x) = n + 1 \qquad l'(x) = 0

	&m(x) = x^{n+1} \qquad m'(x) = (n+1)x^n

	k'(x) &= 0 \cdot x^{n+1} + (n+1) \cdot (n+1)x^n

	&= (n+1)^2x^n
	\cr \cr

	&\text{third term also requires applying power rule}

	o(x) &= nx^{n+2}

	&p(x) = n \qquad p'(x) = 0

	&q(x) = x^{n+2} \qquad q'(x) = (n+2)x^{n+1}

	o'(x) &= 0 \cdot x^{n+2} + n \cdot (n+2)x^{n+1}

	&= (n^2 + 2n)x^{n+1}
	\cr \cr

	&\text{now we can put it all together}

	j'(x) &= 1 - (n+1)^2x^n + (n^2 + 2n)x^{n+1}
	\cr \cr

	&\text{now we work out the derivative of the second term of i'(x)}

	r(x) &= (1 - x)^{-2}

	&u = 1 - x \qquad \delta u = - \delta x

	r'(x) &= 2(1-x)^{-3}
	\cr \cr

	&\text{and now finally we can apply the power rule to get i'(x)}

	i'(x) &= j'(x) \cdot r(x) + j(x) \cdot r'(x)
	\cr

	&= (1 - (n+1)^2x^n + (n^2 + 2n)x^{n+1}) \cdot (1 - x)^{-2} + (x - (n+1)x^{n+1} + nx^{n+2}) \cdot 2(1-x)^{-3}
	\cr

	&= {(1 - (n+1)^2x^n + (n^2 + 2n)x^{n+1})(1 - x) \over (1 - x)^3} + {2(x - (n+1)x^{n+1} + nx^{n+2}) \over (1 - x)^3}
	\cr

	&= {(1 - (n+1)^2x^n + (n^2 + 2n)x^{n+1}) - (x - (n+1)^2x^{n+1} + (n^2 + 2n)x^{n+2}) + (2x - 2(n+1)x^{n+1} + 2nx^{n+2}) \over (1 - x)^3}
	\cr

	&= {1 + x - (n+1)^2x^n + (2n^2 + 2n - 1)x^{n+1} - n^2x^{n+2} \over (1 - x)^3}

	\end{aligned}

Finally, multiply up by x one last time to get the end result

.. math::

	\begin{aligned}

	\sum\limits_{i=0}^{n} i^2x^i &= x \cdot i'(x)
	\cr

	&= \boxed{{x + x^2 - (n+1)^2x^{n+1} + (2n^2 + 2n - 1)x^{n+2} - n^2x^{n+3} \over (1 - x)^3}}

	\end{aligned}

Problem 2
---------

.. admonition:: (a)

	What is the product of the first n odd powers of two: :math:`\prod\limits_{k=1}^{n} 2^{2k-1}`

.. math::

	\begin{aligned}

	\prod\limits_{k=1}^{n} 2^{2k-1} &= 2^1 \cdot 2^3 + \dots \cdot 2^{2n-1}

	&= 2^{\sum\limits_{j=1}^{n} 2j - 1}

	&= 2^{\sum\limits_{i=1}^{2n - 1} \left[ i \right] - \sum\limits_{h=1}^{n - 1} \left[ 2h \right]}

	&= 2^{{(2n - 1)2n \over 2} - 2({(n-1)n \over 2})}

	&= 2^{4n^2 - 2n - 2(n^2 - n) \over 2}

	&= 2^{2n^2 \over 2}

	&= 2^{n^2}

	\end{aligned}

.. admonition:: (b)

	Find a closed expression for

	.. math::

		\sum\limits_{i=0}^{n} \sum\limits_{j=0}^{m} 3^{i+j}

We already know the closed form of the sum of increasing exponents;

.. math::

	\sum\limits_{i=0}^{n} x^i = {1-x^{n+1} \over 1 - x}

We can use this to solve the closed form,

.. math::

	\begin{aligned}

	\sum\limits_{i=0}^{n} \sum\limits_{j=0}^{m} 3^{i+j} &=
		\sum\limits_{i=0}^{n} \left[ 3^i \cdot {1 - 3^{m+1} \over 1 - 3} \right]
		\qquad && \text{apply sum of increasing exponents formula to inner sum}

	&= {1 - 3^{m+1} \over 1 - 3} \cdot \sum\limits_{i=0}^{n} 3^i
		\qquad && \text{closed sum is no longer bound to i}

	&= {1 - 3^{m+1} \over 1 - 3} \cdot {1 - 3^{n+1} \over 1 - 3}
		\qquad && \text{apply the SIE formula again}

	&= {1 - 3^{n+1} - 3^{m+1} + 3^{n+m+2} \over 4}
		\qquad && \text{tidy up}

	\end{aligned}

.. admonition:: (c)

	Find a closed expression for

	.. math::

		\sum\limits_{i}^{n} \sum\limits_{j}^{n} (i + j)

We already know the sum of incrementing integers,

.. math::

	\sum\limits_{i=1}^n i = {n(n+1) \over 2}

We can apply this first to the innner sum, then work outwards;

.. math::

	\begin{aligned}

	\sum\limits_{i}^{n} \sum\limits_{j}^{n} (i + j) &= \sum\limits_{i=1}^{n} \left[ in + {n(n+1) \over 2}\right]

	&= n({n(n+1) \over 2}) + \sum\limits_{i=1}^n in

	&= {n^3 + n^2 \over 2} + {n^3 + n^2 \over 2}

	&= n^3 + n^2

	\end{aligned}

.. admonition:: (d)

	Find a closed expression for

	.. math::

		\prod\limits_{i=1}^n \prod\limits_{j=1}^n 2^i \cdot 3^j

.. math::

	\begin{aligned}

	\prod\limits_{i=1}^n \prod\limits_{j=1}^n 2^i \cdot 3^j &=
		\prod\limits_{i=1}^n \left[ 2^{ni} \cdot \prod\limits_{j=1}^n 3^j \right]
		\cr

	&= \prod\limits_{i=1}^n \left[ 2^{ni} \cdot 3^{n(n+1) \over 2} \right]
		\cr

	&= \prod\limits_{i=1}^n \left[ 2^{ni} \right] \cdot (3^{n(n+1) \over 2})^n
		\cr

	&= 2^{\sum\limits_{i=1}^n ni} \cdot 3^{n^3 + n^2 \over 2}
		\cr

	&= 2^{n({n(n+1) \over 2})} \cdot 3^{n^3 + n^2 \over 2}
		\cr

	&= 2^{n^3 + n^2 \over 2} \cdot 3^{n^3 + n^2 \over 2}

	\end{aligned}


Problem 3
---------

.. admonition:: (a)

	Use integration to find upper and lower bounds that differ by at most 0.1 for the following sum.
	(You may need to add the first few terms explicitly and then use integrals to bound the sum of the remaining terms.)

	.. math::

		\sum\limits_{i=1}^{\infty} {1 \over (2i + 1)^2}

First we can find the limit as the function approaches infinity;

.. math::

	\lim\limits_{n \rightarrow \infty} {1 \over (2n + 1)^2} = 0

Since the function is decreasing and converges at zero, we can apply the following bounds,

.. math::

	f(\infty) + \int_1^\infty f(x)\delta x \le \sum\limits_{i=1}^{\infty} {1 \over (2i + 1)^2} \le f(1) + \int_1^\infty f(x)\delta x

We know :math:`f(\infty)` approaches zero so this term is insignificant.
We can also trivially solve :math:`f(1) = {1 \over 9}`.
We can then solve the integral to get our bounds,

.. math::

	\begin{aligned}

	\int_1^\infty {1 \over (2x + 1)^2} \delta x & \qquad \text{requires u-substitution}
		\cr

	u = 2x + 1 & \qquad \delta u = 2 \delta x
		\cr

	&= {1 \over 2} \left( \int_9^\infty u^{-2} \delta u \right)
		\cr

	&= {1 \over 2} \left( {-1 \over u} \Bigm|_9^\infty \right)
		\cr

	&= {1 \over 2}\left( {-1 \over \infty} - {-1 \over 9} \right)
		\cr

	&= {1 \over 2} \left( {1 \over 9} \right)
		\cr

	&= {1 \over 18}

	\end{aligned}

So our bounds are,

.. math::

	{1 \over 18} \le \sum\limits_{i=1}^{\infty} {1 \over (2i + 1)^2} \le {1 \over 18} + {1 \over 9}

However, since the bounds differ by :math:`1 \over 9`, this is not accurate enough.
We can reduce the error by increasing the lower bound;

.. math::

	f(1) + \int_2^\infty f(x)\delta x \le f(1) + \sum\limits_{i=2}^{\infty} {1 \over (2i + 1)^2} \le f(1) + f(2) + \int_2^\infty f(x)\delta x

Again, we can calculate the integral to determine our error,

.. math::

	\begin{aligned}

	\int_2^\infty f(x)\delta x &= \int_2^\infty {1 \over (2x + 1)^2} \delta x
		\cr

	u = 2x + 1 & \qquad \delta u = 2 \delta x
		\cr

	&= {1 \over 2} \left( \int_25^\infty u^{-2} \delta u \right)
		\cr

	&= {1 \over 2} \left( {-1 \over u} \Bigm|_25^\infty \right)
		\cr

	&= {1 \over 2}\left( {-1 \over \infty} - {-1 \over 25} \right)
		\cr

	&= {1 \over 2} \left( {1 \over 25} \right)
		\cr

	&= {1 \over 50}

	\end{aligned}

This gives us the following bounds,

.. math::

	{1 \over 9} + {1 \over 50} \le \sum\limits_{i=1}^{\infty} {1 \over (2i + 1)^2} \le {1 \over 9} + {1 \over 25} + {1 \over 50}
		\cr

	{59 \over 450} \le \sum\limits_{i=1}^{\infty} {1 \over (2i + 1)^2} \le {59 \over 450} + {1 \over 25}

This gives us an error of only :math:`{1 \over 25}` and so solves the question.
