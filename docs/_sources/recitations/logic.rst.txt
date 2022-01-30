Logic
=====

`problems <link https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/recitations/MIT6_042JF10_rec01.pdf>`_
`solution <link https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/recitations/MIT6_042JF10_rec01_sol.pdf>`_

Team Problem: A Mystery
-----------------------

A certain cabal within the 6.042 course staff is plotting to make the final exam ridiculously hard.
(“Problem 1. Prove that the axioms of mathematics are complete and consistent. Express your answer in Mayan hieroglyphics.”).
The only way to stop their evil plan is to determine exactly who is in the cabal.
The course staff consists of nine people:

	{Oscar, Stav, Darren, Patrice, David, Nick, Martyna, Marten, Tom}

The cabal is a subset of these nine.
A membership roster has been found and appears below, but it is deviously encrypted in logic notation.
The predicate `incabal` indicates who is in the cabal; that is, `incabal(x)` is true if and only if x is a member.

Definitions
"""""""""""

For an extra challenge (because I'm a nerd) I've defined these here;

.. math:: Staff ::= \{ Oscar, Stav, Darren, Patrice, David, Nick, Martyna, Marten, Tom \}

.. math:: incabal(x) ::= \text{x is in the cabal}

.. math:: Cabal ::= \{ x \in Staff \mid incabal(x) \}

Translation
"""""""""""

Translate each statement below into English and deduce who is in the cabal.

.. math:: i)\ \exists x \exists y \exists z \ (x \ne y \land x \ne z \land y \ne z \land incabal(x) \land incabal(y) \land incabal(z))

.. centered:: There are at least 3 people in the cabal, i.e. :math:`|Cabal| \ge 3`

.. math:: ii)\ \lnot (incabal(Stav) \land incabal(David))

.. centered:: Stav and David can't both be in the cabal.

.. math:: iii)\ (incabal(Martyna) \lor incabal(Patrice)) \Rightarrow \forall x\ incabal(x)

.. centered:: If either Martyna or Patrice are in the cabal, then so is everyone else.

.. math:: iv)\ incabal(Stav) \Rightarrow incabal(David)

.. centered:: If Stav is in the cabal then so is David.

.. math:: v)\ incabal(Darren) \Rightarrow incabal(Martyna)

.. centered:: If Darren is in the cabal, then so is Martyna.

.. math:: vi)\ (incabal(Oscar) \lor incabal(Nick)) \Rightarrow \lnot incabal(Tom)

.. centered:: If either Oscar or Nick (or both) are in the cabal, then Tom is not.

.. math:: vii)\ (incabal(Oscar) \lor incabal(David)) \Rightarrow \lnot incabal(Marten)

.. centered:: If either Oscar or David (or both) are in the cabal, then Marten is not.

Conclusions
"""""""""""

From statement (ii) we know Stav and David can't both be in the cabal at the same time.
If we then consider statement (iv), the only way for the implication to be true is if both left and right sides are true.
This contradicts statement (ii) so the left side must be false, the right side can be true or false.
This eliminates Stav from the cabal, so we know the cabal has 8 or less members.

.. math:: \{ Oscar, Darren, Patrice, David, Nick, Martyna, Marten, Tom \}

Statement (iii) can now be used to determine both Martyna and Patrice are not in the cabal.
If we were to assume either of them were, to balance the implication everyone would be in the cabal.
This contradicts what we established with statements (ii) and (iv).
With this we can conclude the left side of statement (iii) must be false.
That means neither Martyna nor Patrice are in the cabal.

.. math:: \{ Oscar, Darren, David, Nick, Marten, Tom \}

Statement (v) can be used by considering the contrapositive,

.. math:: \lnot incabal(Martyna) \Rightarrow \lnot(Darren)

We've already established Martyna is not in the cabal from statement (iii),
so this allows us to safely assume the left side of the contrapositive implication is true.
This means Darren is also not in the cabal.

.. math::  \{ Oscar, David, Nick, Marten, Tom \}

If we look at the contrapositive of statement (vi),

.. math:: incabal(Tom) \Rightarrow \lnot (incabal(Oscar) \lor incabal(Nick))

we can see that if Tom is in the cabal, then both Oscar and Nick are not.
This would leave us with a cabal of:

.. math:: \{Marten, David, Tom\}

But then statement (vii) says if either Oscar or David are in the cabal then Marten is not.
This would leave us with a cabal of

.. math:: \{David, Tom\}

This contradicts statement (i) because now we only have 2 members.
So we can conclude that Tom is not in the cabal, leaving us with;

.. math::  \{ Oscar, David, Nick, Marten \}

Now we can apply statement (vii) again to eliminate Marten, leaving us with the final cabal;

.. math:: Cabal = \{ Oscar, David, Nick \}
