Asymptotic Notation
-------------------

.. admonition:: Question

	Which of these symbols:

	.. math::

		(\Theta, O, \Omega, o, \omega)

	Apply the following equations? List all that apply.

.. math::

	\begin{aligned}

	2n + \log n &= \boxed{ \Theta, O, \Omega} (n)

	Proof: \lim_{n \rightarrow \infty} {2n + \log n \over n} &= {2n \over n} + {\log n \over n} = 2 + 0 = 2 \cr

	\log n &= \boxed{ O, o } (n)

	Proof: \lim_{n \rightarrow \infty} {\log n \over n} &= 0 \cr

	\sqrt{n} &= \boxed{ \Omega, \omega } (\log^300 n)

	Proof: \lim_{n \rightarrow \infty} {\sqrt{n} \over \log^{300} n} &= \infty \cr

	n2^n &= \boxed{ \Omega, \omega } (n)

	Proof: \lim_{n \rightarrow \infty} {n2^n \over n} &= \infty \cr

	n^7 &= \boxed{ O, o } (1.01^n)

	Proof: \lim_{n \rightarrow \infty} {n^7 \over 1.01^n} &= 0 \cr

	\end{aligned}


Asymptotic Equivalence
----------------------

.. admonition:: Intro

	Suppose :math:`f, g: \Bbb Z+ \rightarrow \Bbb Z+` and :math:`f \backsim g`.

.. admonition:: 1

	Prove that :math:`2f \backsim 2g`

:math:`f \backsim g` implies :math:`\lim_{x \rightarrow \infty} {f(x) \over g(x)} = 1`.
If we compare f and g we get,

.. math::

	{ \bcancel{2}f(x) \over \bcancel{2}g(x)} = {f(x) \over g(x)} = 1

.. admonition:: 2

	Prove that :math:`f^2 \backsim g^2`.

.. math::

	\lim_{x \rightarrow \infty} {f(x)^2 \over g(x)^2} = {f(x) \over g(x)} \cdot {f(x) \over g(x)} = 1 \cdot 1 = 1

.. admonition:: 3

	Give examples of f and g such that :math:`2^f \cancel{\backsim} 2^g`.


.. admonition:: 4

	Show that :math:`\backsim` is an equivalence relation


It is reflexive, because :math:`\lim_{x \rightarrow \infty} {f(x) \over f(x)} = 1`, as long as :math:`f(x) \ne 0`.

It is transitive, because if :math:`\lim_{x \rightarrow \infty} {f(x) \over g(x)} = 1` and :math:`\lim_{x \rightarrow \infty} {g(x) \over h(x)} = 1`,
then we can multiply the limits to get,

.. math::

	\lim_{x \rightarrow \infty} {f(x) \over h(x)} = \lim_{x \rightarrow \infty} {f(x) \over g(x)} \cdot {g(x) \over h(x)} = 1 \cdot 1 = 1

It is symmetric, because if :math:`\lim_{x \rightarrow \infty} {f(x) \over g(x)} = 1`,
then the following is also true :math:`\lim_{x \rightarrow \infty} {g(x) \over f(x)} = 1` by limit laws of quotients,
as long as :math:`f(x) \ne 0` and :math:`g(x) \ne 0`.

Those are the properties required of equivalence relations, so :math:`\backsim` is an equivalence relation.


.. admonition:: 5

	Show that :math:`\Theta` is an equivalence relation

In order for the following to be true,

.. math::

	0 < \lim_{x \rightarrow \infty} {f(x) \over g(x)} < \infty

Then we know :math:`f(x)` can't be zero, because :math:`\forall x \in \Bbb R. {0 \over x}= 0`.
Since we know it's not zero, then it must be reflexive because :math:`\lim_{x \rightarrow \infty} {f(x) \over f(x)} = 1`,
which is between zero and infinity.

It is symmetric because if :math:`f = \Theta(g)` then :math:`\lim_{x \rightarrow \infty} {f(x) \over g(x)} = k`
where k is some constant between zero and infinity. :math:`\lim_{x \rightarrow \infty} {f(x) \over g(x)} = {1 \over k}`
then proves the symmetry.

It is transitive, because if :math:`f = \Theta(g)` and :math:`g = \Theta(h)` then
:math:`\lim_{x \rightarrow \infty} {f(x) \over g(x)} = k` where :math:`0 < k < \infty` and
:math:`\lim_{x \rightarrow \infty} {g(x) \over h(x)} = j` where :math:`0 < j < \infty`.
So by multiplying the limits we get,

.. math::

	\lim_{x \rightarrow \infty} {f(x) \over g(x)} \cdot \lim_{x \rightarrow \infty} {g(x) \over h(x)} = k \cdot j

Since both k and j are finite, then so is kj.