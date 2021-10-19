Doubles
=======

1. The L-tower problem
----------------------

.. admonition:: Introduction

	Observe the structures shown in Figure 1. One has 2 L-shapes, the other 5 L-shapes.
	Consider a tower with k L-shapes.
	Assume that the blocks are all of size :math:`x \times 1` where :math:`x > 1`.
	As the picture indicates, if k is too small then the tower falls to the left.
	On the other hand, if k is too large the tower would fall to the right.
	Will the tower be stable for some k?
	Prove there is at least one value of k for which the L-tower is stable.
	Assume that a structure is stable if and only if its center of gravity is not hanging in the air horizontally.
	The L-tower is stable if and only if each of its subparts is stable.

	*Hint*: Show the tower is stable if and only if :math:`{3x - 3 \over 2} \le k \le {3x - 1 \over 2}`.

	.. image:: ../images/L-tower.png
		:align: center

First, consider a single L-shape.

.. image:: ../images/L1.png
	:align: center

If we calculate from the bottom left corner being zero, its horizontal center of mass is an average of the two blocks.
The horizontal block has a center at :math:`{x \over 2}`.
The vertical block has a center at :math:`{1 \over 2}` since the block is defined as having a width of 1.

As an average this works out to;

.. math::

	\begin{aligned}

	c_1 &= {{x \over 2} + {1 \over 2} \over 2}

	c_1 &= {x + 1 \over 4}

	\end{aligned}

Now consider an L-shape above the first L-shape.

.. image:: ../images/L2.png
	:align: center

We can calculate the combined horizontal center of mass as follows;

.. math::

	\begin{aligned}

	c_2 &= {x \over 2} + {1 \over 2} + \big( 1 + {x \over 2} \big) + \big( 1 + {1 \over 2} \big)

	c_2 &= {x + 3 \over 4}

	c_2 &= c_1 + {1 \over 2}

	\end{aligned}

Note that center of mass has increased by :math:`{1 \over 2}` to the right.
Any L-shapes above the first one must have their combined center of mass less than or equal to x,
otherwise they will fall to the right.

In general, the center of mass for a k L-shape configuration, :math:`c_k`,
can be calculated as follows,

.. math::

	\begin{aligned}

	c_k &= {\sum\limits_{i=1}^{k} (i - 1) + {x \over 2} + (i - 1) + {1 \over 2} \over 2k}

	&= {k \cdot \big( {x + 1 \over 2} \big) + [0, 1, 2, \dots, k - 1] \over 2k}

	&= {k \cdot \big ( {x + 1 \over 2} \big ) + k \cdot (k - 1) \over 2k}

	&= {{x + 1 \over 2} + k - 1 \over 2}

	&= {x + 1 \over 4} + {k - 1 \over 2}

	\end{aligned}

For the k L-shape not to fall to the left, the center of mass must not to be further left than the left edge of the initial vertical block,
and to not fall to the right the center of mass must not be further than the right edge.
This can be expressed as the condition,

.. math::

	x - 1 \le c_k \le x

An increase in k moves the center of mass :math:`{1 \over 2}` to the right,
so we can calculate :math:`c_{k - 1}` as,

.. math::

	c_{k - 1} = {x + 1 \over 4} + {k - 1 \over 2} - {1 \over 2}

For any stable k L-tower, we can then say

.. math::

	c_{k - 1} \le x - 1

	{x + 1 \over 4} + {k - 1 \over 2} - {1 \over 2} \le x - 1

	{x + 1 \over 4} + {k - 1 \over 2} \le x - {1 \over 2}

	c_k \le x - {1 \over 2}

This is a stricter upper bound on :math:`c_k`, which gives us,

.. math::

	x - 1 \le c_k \le x - {1 \over 2}

That can be solved for k as follows,

.. math::

	\begin{aligned}

	x - 1 &\le {x + 1 \over 4} + {k - 1 \over 2} &&\le x - {1 \over 2}

	x - 1 &\le {x + 2k - 1 \over 4} &&\le x - {1 \over 2}

	4x - 4 &\le x + 2k - 1 &&\le 4x - 2

	4x - 3 &\le x + 2k &&\le 4x - 1

	3x - 3 &\le 2k &&\le 3x - 1

	{3x - 3 \over 2} &\le k && \le {3x - 1 \over 2}

	\end{aligned}

We can then work out the difference between the upper and lowers bounds,

.. math::

	\begin{aligned}

	{3x - 1 \over 2} - {3x - 3 \over 2} &= 1

	{2 \over 2} &= 1

	\end{aligned}

If x is an odd integer, then stable values for k are the lower bound, the midpoint and the upper bound,
or :math:`\lbrack x - 1, x - {1 \over 2}, x \rbrack`,
because the bounds will evaluate to an even number, y.

.. math::

	\begin{aligned}

	y &= {3x - 3 \over 2}

	&= {3 \cdot odd - 3 \over 2}

	&= {odd - 3 \over 2}

	&= {even \over 2}

	&= even

	\end{aligned}

If x is anything else, however, then there are two stable values for k,
:math:`\lbrack y, z \rbrack`, where :math:`x - 1 < y < x - {1 \over 2}` and :math:`z = y + {1 \over 2}`.

Double Sums
-----------

.. admonition:: Intro

	Sometimes we have to evaluate sums of sums, otherwise known as double summations.
	It’s good to know how to tame these beasts!
	Here’s an example of a double summation:

	.. math::

		\sum\limits_{i=1}^{n} \sum\limits_{j=1}^{i} j

	It looks ferocious...all those sharp teeth!
	But actually, this double summation is just a sheep in wolf’s clothing:
	to evaluate it, we can just evaluate the inner sum, replace it with a closed form we already know,
	and then evaluate the outer sum which no longer has a summation inside it.

.. admonition:: Question

	Evaluate the summation. (Hint: :math:`\sum (a + b) = \sum a + \sum b`.)

.. math::

	\begin{aligned}

	\sum\limits_{i=1}^{n} {i(i+1) \over 2} \qquad & \text{ replace inner sum with closed form} \cr

	\sum\limits_{i=1}^{n} {i^2 + i \over 2} \qquad & \text{ multiply out parentheses } \cr

	{1 \over 2} \cdot \sum\limits_{i=1}^{n} i^2 + i \qquad & \text{ multiply by common factor} \cr

	{1 \over 2} \cdot \big( \sum\limits_{i=1}^{n} i^2 + \sum\limits_{i=1}^{n} i \big) \qquad & \text{ separate summations} \cr

	{1 \over 2} \cdot \big( {n^3 \over 3} + {n^2 \over 2} + {n \over 6} + {n(n+1) \over 2} \big ) \qquad & \text{ replace with known closed forms} \cr

	{1 \over 2} \cdot \big( {n^3 \over 3} + {n^2 \over 2} + {n \over 6} + {n^2 \over 2} + {n \over 2} \big) \qquad & \text{ multiply out inner parenthesis} \cr

	{1 \over 2} \cdot \big( {2n^3 \over 6} + {3n^2 \over 6} + {n \over 6} + {3n^2 \over 6} + {3n \over 6} \big) \qquad & \text{ multiply up to common factor} \cr

	{1 \over 2} \cdot \big( {2n^3 + 6n^2 + 4n \over 6} \big) \qquad & \text{ add fractions} \cr

	{1 \over 2} \cdot \big( {n^3 + 3n^2 + 2n \over 3} \big) \qquad & \text{ simplify} \cr

	\end{aligned}

.. admonition:: Intro

	Unfortunately, not all summations are so docile.
	Fortunately, we have ways to deal with this.
	There’s a special trick that is often extremely useful for sums, and that is to exchange the order of summation.
	We’ll go through an example here.
	For the remainder of the problem we’ll wrestle with the sum of the harmonic numbers:

	.. math::

		\sum\limits_{k=1}^{n} H_k

	At first glance, it looks like just a single summation, but do not be deceived.

.. admonition:: Question

	First, write it as a double summation.

.. math::

	\sum\limits_{k=1}^{n} \sum\limits_{j=1}^{k} {1 \over j}

.. admonition:: Question

	Now try to gain some intuition for exactly what you’re up against by integrating the summation in its less threatening single-summation form.
	You may use :math:`H_k \approx \ln k`.

The given solution is;

.. math::

	\sum\limits^{n}_{k=1} \ln k = \int^{n}_{k=1} \ln n = n \ln n - n + 1

However, if we use :math:`n = 3`

	\sum\limits^{3}_{k=1} \ln k = \ln 1 + \ln 2 + \ln 3 = 0 + 0.69... + 1.09... = 1.79...

	n \ln n - n + 1 = 3 \ln 3 - 3 + 1 = 1.29...

So I don't understand how they got their solution, and their solution appears to be incorrect anyway.
It's obviously wrong because :math:`H_1 = 1`, but :math:`\ln 1 = 0`, which is nowhere near approximately correct.


.. admonition:: Question

	Finally, we’ll look for an exact answer.
	If we think about the pairs (k, j) over which we are summing, they form a triangle in the table below.
	The values in the cells of the table correspond to the terms in the double summation.
	The first two rows have been filled in for you.
	Complete the remaining three rows to see the pattern.

.. list-table:: Sample list table
	:widths: 10 10 10 10 10 10 10
	:header-rows: 1
	:stub-columns: 1

	* - :math:`{j \over k}`
	  - 1
	  - 2
	  - 3
	  - 4
	  - ...
	  - n
	* - 1
	  - 1
	  -
	  -
	  -
	  -
	  -
	* - 2
	  - 1
	  - :math:`{1 \over 2}`
	  -
	  -
	  -
	  -
	* - 3
	  - 1
	  - :math:`{1 \over 2}`
	  - :math:`{1 \over 3}`
	  -
	  -
	  -
	* - 4
	  - 1
	  - :math:`{1 \over 2}`
	  - :math:`{1 \over 3}`
	  - :math:`{1 \over 4}`
	  -
	  -
	* - ...
	  -
	  -
	  -
	  -
	  -
	  -
	* - n
	  - 1
	  - :math:`{1 \over 2}`
	  - :math:`{1 \over 3}`
	  - :math:`{1 \over 4}`
	  -
	  - :math:`{1 \over n}`

.. admonition:: Question

	The summation above is summing each row and then adding the row sums.
	But we can tame this beast if, instead, we first sum the columns and then add the column sums.
	Use the table to rewrite the double summation.
	The inner summation should sum over k, and the outer summation should sum over j.

.. math::

	\sum\limits^{n}_{j=1} \sum\limits^{n}_{k=j} {1 \over j}

.. admonition:: Question

	Now simplify the summation to derive a closed form in terms of *n* and :math:`H_n`.

.. math::

	\begin{aligned}

	\sum\limits^{n}_{j=1} \sum\limits^{n}_{k=j} {1 \over j} &= \sum\limits^{n}_{j=1} {1 \over j} \cdot \sum\limits^{n}_{k=j} 1 \cr

	&= \sum\limits^{n}_{j=1} {1 \over j} \cdot (n - j + 1) \cr

	&= \sum\limits^{n}_{j=1} {n + 1 \over j} - 1 \cr

	&= \sum\limits^{n}_{j=1} {n \over j} + \left ( \sum\limits^{n}_{j=1} {1 \over j} \right ) - n \cr

	&= n(H_n) + H_n - n \cr

	&= (n + 1)H_n - n \cr

	\end{aligned}
