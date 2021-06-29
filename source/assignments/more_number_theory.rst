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


Problem 2
---------

**(a) If** :math:`a \mid b` **, then** :math:`\forall c, a \mid bc`

.. raw:: html

	<hr>

**Theorem**: Let P(n) be the proposition defined as so,

.. math::

	P(n) ::= b = 0 \text{ (mod a) }\Rightarrow bn = 0 \text{ (mod a) }

That is, if a divide b with no remainder, then a also divides any multiple of b with no remainder.

**Proof.** By induction.

**Base Case**: We must prove P(0),

.. math::

	\begin{aligned}

	0 \cdot b &= 0 \text{ (mod a) }

	0 &= \text{ (mod a) }\qquad && \text{ zero divided by any number is zero}

	\end{aligned}

This proves P(0).

**Inductive Step**: Assuming P(n) is true, we must prove P(n + 1),

.. math::

	\begin{aligned}

	\big( n \cdot b + (n+1) \cdot b \big) &= 0 \text{ (mod a) }

	0 + (n+1) \cdot b &= \text{ (mod a) } && \qquad \text{(by inductive hypothesis)}

	nb + b &= \text{ (mod a) } && \qquad \text{(parameter expansion)}

	0 + b &= \text{ (mod a) } && \qquad \text{(by P(n))}

	0 &= \text{ (mod a) } && \qquad \text{(we assume a cleanly divides b)}

	\end{aligned}

This proves P(n+1), and so by the inductive method we can conclude the theorem is true.
:math:`\blacksquare`

**(b) If a | b and a | c, then a | sb + tc.**

.. raw:: html

	<hr>

We can rewrite :math:`a \mid sb + tc` as,

.. math::

	\big( sb \text{ (mod a) } + tc \text{ (mod a) } \big) \text{ (mod a) } = 0

As we showed in part (a), if :math:`a \mid b` then :math:`a \mid sb`,
and if :math:`a \mid c` then :math:`a \mid tc`, which leaves us with,

.. math::

	0 + 0 \text{ (mod a) } = 0

Which is trivially true.
:math:`\blacksquare`

**(c)** :math:`\forall c, a \mid b \Leftrightarrow ca \mid cb`

.. raw:: html

	<hr>

Since a divides b, then there exists some integer d such that :math:`{b \over a} = d`.
We can factor up :math:`{b \over a}` by c, giving us :math:`{cb \over ca} = d`.
:math:`\blacksquare`

**(d) gcd(ka, kb) = k gcd(a, b)**

.. raw:: html

	<hr>

From Euclid's algorithm, we know :math:`gcd(a, b) = gcd(b, rem(a, b))`.
From Division Theorem, we know :math:`a = qb + r`, where q is the quotient and r is the remainder.
This allows to calculate the remainder for the constructor case of Euclid's algorithm as,
:math:`r = a - qb`.

When we try to find the gcd of ka and kb, however, :math:`gcd(ka, kb) = gcd(kb, rem(ka, kb)`.
Here, the calculation for the remainder becomes :math:`r = ka - q(kb)`, which can be rewritten as,
:math:`r = k(a - qb)`. It is the same calculation as for :math:`gcd(a, b)`, except multiplied by k.
:math:`\blacksquare`

Problem 3.
----------

In this problem, we will investigate numbers which are squares modulo a prime number p.

(a) An integer n is a square modulo p if there exists another integer x such that :math:`n ≡ x^2 \text{ (mod p)}`.
Prove that :math:`x^2 ≡ y^2 \text{ (mod p)}` if and only if :math:`x ≡ y \text{ (mod p) or } x ≡ −y \text{ (mod p)}`.
(Hint: :math:`x^2 − y^2 = (x + y)(x − y)`)

.. raw:: html

	<hr>

First, define some propositions, P and Q,

.. math::

	\begin{aligned}

	P &::= x^2 ≡ y^2 \text{ (mod p)}

	Q &::= x ≡ y \text{ (mod p) or } x ≡ −y \text{ (mod p)}

	\end{aligned}

We can rewrite x and y mod p as a quotient of p plus a remainder.

.. math::

	\begin{aligned}

	x &= q_1 p + m

	y &= q_2 p + m

	\end{aligned}

Such that :math:`x^2` and :math:`y^2` are can be written as,

.. math::

	\begin{aligned}

	x^2 &= (q_1 p + m) \cdot (q_1 p + m)

	y^2 &= (q_2 p + m) \cdot (q_2 p + m)

	\end{aligned}

Since we're applying mod p, we can remove any factors of p,

.. math::

	\begin{aligned}

	(\cancel{q_1 p} + m) \cdot (\cancel{q_1 p} + m) &≡ (\cancel{q_2 p} + m) \cdot (\cancel{q_2 p} + m) \text{ (mod p) }

	m \cdot m &≡ m \cdot m \text{ (mod p) }

	\end{aligned}

This proves P implies Q where y is positive.
When x and y are squared they are always positive. If x or y are negative the equation becomes

.. math::

	\begin{aligned}

	(\cancel{(\pm q_1) p} + m) \cdot (\cancel{(\pm q_1) p} + m) &≡ (\cancel{(\pm q_2) p} + m) \cdot (\cancel{(\pm q_2) p} + m) \text{ (mod p) }

	m \cdot m &≡ m \cdot m \text{ (mod p) }

	\end{aligned}

Which still factors out because they're multiples of p.
This proves P implies Q where y is negative.
:math:`\blacksquare`

**(b) There is a simple test we can perform to see if a number n is a square modulo p. It states that**

*Theorem 1 (Euler’s Criterion). :*

1. If n is a square modulo p then :math:`n^{{p - 1 \over 2}}` ≡ 1 (mod p).

2. If n is not a square modulo p then :math:`n^{{p - 1 \over 2}}` ≡ −1 (mod p).

Prove the first part of Euler’s Criterion. (Hint: Use Fermat’s theorem.)

.. raw:: html

	<hr>

Fermat's theorem says that :math:`k^{p-1} ≡ 1 (mod p)` where p is a prime and k is not a multiple of p.
Since n is a square modulo p it can written as :math:`n = x^2 \text{ (mod p) }`

.. math::

	\begin{aligned}

	n^{{p - 1 \over 2}} &≡ 1 \text{ (mod p) }

	(x^\cancel{2})^{{p - 1 \over \cancel{2}}} &≡ 1 \text{ (mod p) }

	x^{p-1} &≡ 1 \text{ (mod p) }

	\end{aligned}

This gets us back to Fermat's theorem and so proves Euler's criterion.
:math:`\blacksquare`

**(c) Assume that** :math`p ≡ 3 \text{ (mod 4)}` **and** :math`n ≡ x^2 \text{ (mod p)}`.
**Given n and p, find one possible value of x.**
(Hint: Write p as p = 4k + 3 and use Euler’s Criterion.
You might have to multiply two sides of an equation by n at one point.)

.. raw:: html

	<hr>

.. math::

	\begin{aligned}

	p &≡ 3 \text{ (mod 4)}

	4k + 3 &≡ 3 \text{ (mod 4)}

	\text{ let's assume k = 0 }

	p &= 4 \cdot 0 + 3 = 3

	n &≡ x^2 \text{ (mod 3) }

	n^{{p - 1 \over 2}} &≡ 1 \text{ (mod 3) }

	(x^\cancel{2})^{{p - 1 \over \cancel{2}}} &≡ 1 \text{ (mod 3) }

	x^{p-1} &≡ 1 \text{ (mod 3) }

	x^2 &≡ 1 \text{ (mod 3) }

	\text{ x can be any number not a multiple of 3, e.g. } \boxed{x = 2}

	2^2 &≡ 1 \text{ (mod 3) }

	\end{aligned}

More generally, x can be any number not a multiple of 4k + 3, for any integer k.
:math:`\blacksquare`

Problem 4
---------

Prove that for any prime, p, and integer, :math:`k \ge 1,\ \phi(p^k) = p^k − p^{k−1}`, where :math:`\phi` is Euler’s function.
(Hint: Which numbers between 0 and :math:`p^{k − 1}` are divisible by p? How many are there?)

.. raw:: html

	<hr>

Since Euler's function is defined as the number of integers in :math:`[0..p)` that are relatively prime to p.
The maximum possible number of integers in :math:\phi(p)` is p, because we start from 0 so :math:`\mid [0..p) \mid = p`

In this question, p is a prime number so :math:`\phi(p) = p - 1`,
because every number in :math:`[0..p)` is relatively prime to p except 0.

The maximum number of possible integers in :math:`\phi(p^k)` then, is :math:`p^k`.
Every *pth* number will be divisible by p which gives us,

.. math::

	\phi(p^k) = p^k - {1 \over p} \cdot \big( p^k \big)

	= p^k - {p^k \over p}

	= p^k - p^{k-1}

This proves the original statement.
:math:`\blacksquare`

Problem 5
---------

Here is a very, very fun game. We start with two distinct, positive integers written on a blackboard.
Call them x and y. You and I now take turns. (I’ll let you decide who goes first.)
On each player’s turn, he or she must write a new positive integer on the board that is a common divisor of two numbers that are already there.
If a player can not play, then he or she loses.

For example, suppose that 12 and 15 are on the board initially.
Your first play can be 3 or 1. Then I play 3 or 1, whichever one you did not play.
Then you can not play, so you lose.

**(a) Show that every number on the board at the end of the game is either x, y, or a positive divisor of gcd(x, y).**

.. raw:: html

	<hr>

**Corollary 1**: For any step, n, the number added, z, is a factor of x and y.

**Base Case**: P(0) is trivially true, because in the start state x and y are the only numbers on the board,
so when we add a new number z, there exists quantifiers, q, such that,

.. math::

	z = q_1 x \land q_2 y

which makes it a factor of x and y.

**Inductive Step**: Assuming P(n) is true, we must show P(n + 1) is true.
Since every number on the board is a factor of x and y, any pair that we choose to make a new factor will also be a factor of x and y.
:math:`\whitesquare`

**Theorem**: If :math:`z \mid x,y` then :math:`z \mid gcd(x, y)`

**Proof**:

By Euclid's algorithm, we know the gcd(x, y) is a linear combination of x and y.

.. math::

	gcd(x, y) = sx + ty

We also know any number that divides x and y, also divides a linear combination of x and y,
by `common divisor divides integer combination <link https://proofwiki.org/wiki/Common_Divisor_Divides_Integer_Combination>`_

So any number on the board is either x and y (since they start on the board),
or is a common divisor of x and y, so therefore a divisor of gcd(x, y).
:math:`\blacksquare`

**(b) Show that every positive divisor of gcd(x, y) is on the board at the end of the game.**

.. raw:: html

	<hr>

In part (a) we showed that every common divisor of x and y also divides gcd(x, y).
We must show that there does not exist a positive integer that divides gcd(x, y) that does not also divide x and y.

Suppose we have integer c, that is a common divisor of x and y but doesn't divide gcd(x, y).
Since c divides x and y, it is a linear combination of x and y

.. math::

	c = sx + ty

But as we showed in part (a) the gcd is also a linear combination of x and y.
And since the gcd is by definition the greatest common divisor c < gcd(x, y), and so therefore :math:`c \mid gcd(x, y)`.
:math:`\blacksquare`

**(c) Describe a strategy that lets you win this game every time.**

.. raw:: html

	<hr>

If I start, there must be an odd number of total moves for me to win.
If you start, there must be an even number of total moves for me to win.

Games with odd numbers of moves exist, and so do games with even numbers of moves.
So a strategy to win every game is to check the parity of total moves and choose to go first or second accordingly.

This can be done starting with an empty set and adding to it;

1. The greatest common divisor of x and y (unless equal to x or y)

2. Each of the prime factors of the gcd(x, y)

3. Each of the unique combinations of prime factors of gcd(x, y)

4. Add 1, since it divides everything

5. If the parity of the resulting set is even, choose to go second, else choose to go first.

As an example, here are the steps for applying the strategy to (90, 45)

0. Initialise empty set

1. gcd(90, 45) = 45, but we already have 45 as a starting value, so skip this step.

2. Prime factors of 45 are :math:`3 \cdot 3 \cdot 5`, so add 3 and 5

3. Unique combinations of prime factors are :math:`3 \cdot 3 = 9` and :math:`3 \cdot 5 = 15`, so add 9 and 15

4. Add 1 to the set

5. Resulting set :math:`\mid \{ 1, 3, 5, 9, 15 \} \mid = 5` which is odd, so choose to go first.

Problem 6
---------

**In one of the previous problems, you calculated square roots of numbers modulo primes equivalent to 3 modulo 4.**
**In this problem you will prove that there are an infinite number of such primes!**

**(a) As a warm-up, prove that there are an infinite number of prime numbers.**
(Hint: Suppose that the set F of all prime numbers is finite, that is  and
define :math:`n = p_1, p_2 \dots p_{k + 1}`.)

.. raw:: html

	<hr>

Suppose there are a finite number of prime numbers, :math:`F = \{p_1, p_2, \dots , p_k\}`.
Then define the product of these numbers plus 1, :math:`n = p_1 \cdot p_2 \cdot \dots \cdot p_k + 1`
By definition of their being prime, n is not divisible by any prime in F because they would have to be able to divide 1, which is impossible.
Therefore it is either prime itself, or is divisible by another prime larger than :math:`p_k`, which is a contradiction.
:math:`\blacksquare`

**(b) Prove that if p is an odd prime, then p ≡ 1 (mod 4) or p ≡ 3 (mod 4).**

.. raw:: html

	<hr>

:math:`p mod 4 \ne 0` because then it is exactly divisible by 4, and so not prime.
Likewise, it cannot be equal to 2, because then,

.. math::

	p = 4b + 2

Since 4b is a multiple of 4 it is even. Adding two also gives us an even number,
so p must be divisible by 2. It is trivial to show the only even prime is 2,
so we can conclude it is the only prime mod 4 that gives 2.

2, itself, is not an odd prime so the hypothesis stands.

This then eliminates 2 of the 4 options for any odd prime mod 4, leaving only 1 and 3.
Thus the hypothesis stands.
:math:`\blacksquare`

**(c) Prove that if n ≡ 3 (mod 4), then n has a prime factor p ≡ 3 (mod 4).**

.. raw:: html

By modulus arithmetic, we know that :math:`ab ≡ (a \text{ mod c} \cdot b \text{ mod c}) \text{ mod c}`,
for any integer a,b and c.

Therefore if we take the prime factors of n we get :math:`n = p^{n_1}_1 \cdot p^{n_2}_2 \cdot \dots p^{n_k}_k`
Since we know n mod 4 is 3, we know n mod it's prime factors is also 3.

Therefore,

.. math::

	\begin{aligned}

	p^{n_1}_1 \cdot p^{n_2}_2 \cdot \dots p^{n_k}_k &≡ 3 \text{ (mod 4)}

	\Big( (p^{n_1}_1 \text{ mod 4}) \cdot (p^{n_2}_2 \text{ mod 4}) \cdot \dots (p^{n_k}_k \text{ mod 4}) \Big) \text{ mod 4} &≡

	\end{aligned}

As we showed in part (b) prime numbers mod 4 must be equal to 1, 2, or 3.
Suppose the prime factors mod 4 were all equal to 1, then the final mod 4 would be,

.. math::

	\begin{aligned}

	(1_1 \cdot 1_2 \cdot \dots 1_k) \text{ mod 4} \bcancel{&≡} 3

	1 \text{ mod 4} \bcancel{&≡} 3

	\end{aligned}

so :math:`p_1` to :math:`p_k` mod 4 cannot all be 1.

Similarly, if 2 was a prime factor, and the rest ones we would get,

.. math::

	\begin{aligned}

	(2 \cdot 1_1 \cdot \dots 1_k) \text{ mod 4} \bcancel{&≡} 3

	2 \text{ mod 4} \bcancel{&≡} 3

	\end{aligned}

And if we have more than two 2s in the prime factor then n becomes divisible by 4,
which would result in :math:`n ≡ 0 \text{ mod 4}`, so there can't be more than two 2s.

The only option left is for at least one of the prime factors mod 4 to be equal to 3.
:math:`\blacksquare`

**(d) Let F be the set of all primes p such that p ≡ 3 (mod 4).**
**Prove by contradiction that F has an infinite number of primes.**

.. raw:: html

	<hr>

Suppose F is finite, so we get :math:`F = \{p_1, p_2, \dots , p_k\}`.
Now define an integer n as a product of F such that :math:`n = 4 \cdot p_1 \cdot p_2 \cdot \dots \cdot p_k - 1`

We know by modulus arithmetic that n mod 4 = 3
But since we're assuming F is finite, n cannot be prime.
Every number is a product of primes, and as we showed in part (c),
if a number mod 4 equals 3, at least one of its prime factors mod 4 is equal to 3.

So, there must exist :math:`p_i \in F. p_i \mid n` where i in [0..k].

But :math:`p_i` cannot divide n, because it would have to divide -1, which is impossible.
So the only other option is that n itself is prime, which is a contradiction because then it is a prime larger than :math:`p_k`.
So that proves there are infinite primes in F.
:math:`\blacksquare`
