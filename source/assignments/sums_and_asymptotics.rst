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
