Number Theory
=============

Problem 1
---------

Define a *3-chain* to be a (not necessarily contiguous) subsequence of three integers,
which is either monotonically increasing or monotonically decreasing.
We will show here that any sequence of five distinct integers will contain a *3-chain*.
Write the sequence as :math:`a_1, a_2, a_3, a_4, a_5`.
Note that a monotonically increasing sequences is one in which each term is greater than or equal to the previous term.
Similarly, a monotonically decreasing sequence is one in which each term is less than or equal to the previous term.
Lastly, a subsequence is a sequence derived from the original sequence by deleting some elements without changing the location of the remaining elements.

a) Assume that :math:`a_1 < a_2`. Show that if there is no *3-chain* in our sequence,
   then :math:`a_3` must be less than :math:`a_1`. (Hint: consider :math:`a_4`!)

Since the integers are distinct, we know :math:`a_x \ne a_y` for any item x and y in the sequence.

If :math:`a_3` is greater than :math:`a_2` then we have a monotonically increasing *3-chain* of :math:`(a_1,a_2,a_3)` already,
so :math:`a_3` cannot be greater than :math:`a_2`.

If :math:`a_3` is between :math:`a_1` and :math:`a_2` then :math:`a_4` has two options.

1. if :math:`a_3 < a_4` then :math:`a_1 < a_3 < a_4` which is a monotonically increasing *3-chain*,
    so :math:`a_4` cannot be greater than :math:`a_3`.
2. if :math:`a_3 > a_4` then :math:`a_2 > a_3 > a_4` which is a monotonically decreasing *3-chain*,
    so :math:`a_4` cannot be less than :math:`a_3`

Therefore, :math:`a_3` cannot be greater than :math:`a_1`.

b) Using the previous part, show that if :math:`a_1 < a_2` and there is no *3-chain* in our sequence,
   then :math:`a_3 < a_4 < a_2`.

If :math:`a_4` is greater than :math:`a_2`, then we have a monotonically increasing *3-chain* of :math:`(a_1,a_2,a_4)` already,
so :math:`a_4` cannot be greater than :math:`a_2`.

From part (a) we already established :math:`a_3 < a_2`, so if :math:`a_4` is less than :math:`a_3`,
then we have a monotonically decreasing *3-chain* of :math:`(a_2,a_3,a_4)`, so :math:`a_4` cannot be less than :math:`a_3`.

Therefore, :math:`a_4` must be between :math:`a_2` and :math:`a_3`.

c) Assuming that :math:`a_1 < a_2 \text{ and } a_3 < a_4 < a_2`,
   show that any value of :math:`a_5` must result in a *3-chain*.

From part (a) and part (b) we established :math:`a_2` and :math:`a_3` are the highest and lowest numbers respectively.

If :math:`a_4` is greater than :math:`a_1` then :math:`a_5` has two options;

1. If :math:`a_5 > a_4` then :math:`(a_3,a_4,a_5)` is a monotonically increasing *3-chain*
2. If :math:`a_5 < a_4` then :math:`(a_2,a_4,a_5)` is a monotonically decreasing *3-chain*

If :math:`a_4` is less than :math:`a_1` then :math:`a_5`, again, has two options;

1. If :math:`a_5 > a_4` then :math:`(a_3,a_4,a_5)` is a monotonically increasing *3-chain*
2. If :math:`a_5 < a_4` then :math:`(a_2,a_4,a_5)` is a monotonically decreasing *3-chain*

In every case we have a *3-chain*, therefore any value of :math:`a_5` results in a *3-chain*

d) Using the previous parts, prove by contradiction that any sequence of five distinct integers must contain a *3-chain*.

**Theorem**: Any sequence of five distinct integers must contain a *3-chain*

**Proof**: By contradiction.
We shall try to prove the proposition that there exists a sequence of five distinct integers that does not contain a *3-chain*.

The question establishes the integers in the sequence are distinct, so we don't need to consider :math:`a_x = a_y`.
This is a necessity, because if :math:`a_x = a_y` then there is always a *3-chain*.
This is because no matter if :math:`a_z` is higher, lower or equal, it will create the third item in the chain.

As we saw in (a) (b) and (c) there is always a *3-chain* if :math:`a_1 < a_2`.
So if our proposition holds then :math:`a_1 > a_2`.

If :math:`a_1 > a_2` then no subsequent number can be less than :math:`a_2`
because it would complete a monotonically decreasing *3-chain* of :math:`(a_1, a_2, a_n)`

If :math:`a_3 < a_1` then :math:`a_4` has 2 options:

1. :math:`a_4 > a_3`, but then we get :math:`(a_2, a_3, a_4)` increasing
2. :math:`a_4 < a_3`, but then we get :math:`(a_1, a_3, a_4)` decreasing

So :math:`a_3 > a_1`.
This means :math:`a_4 < a_3` because otherwise we'd get :math:`(a_1, a_3, a_4)` increasing.

So :math:`a_4 < a_3` and :math:`a_2 < a_4 < a_3`.

This leaves 2 options for :math:`a_5`;

1. :math:`a_5 > a_4`, but then we get :math:`(a_2, a_4, a_5)` increasing.
2. :math:`a_5 < a_4`, but then  we get :math:`(a_3, a_4, a_5)` decreasing.

This gives us a *3-chain* in all cases, which contradicts our proposition.
So the theory must be true - any sequence of five distinct integers must contain a *3-chain*.
:math:`\blacksquare`
