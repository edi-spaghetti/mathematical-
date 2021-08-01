Networks
========

Analysis of Two Networks
------------------------

Two communication networks are shown below.
Complete the table of properties and be prepared to justify your answers.

.. list-table::

	* - .. image:: ../images/networks-5-path.png
	  - .. image:: ../images/networks-4-cycle.png

.. raw:: html

	<hr>

.. list-table::
	:widths: 20 20 20 20 20
	:header-rows: 1

	* - Network
	  - # Switches
	  - Switch Size
	  - Diameter
	  - Max Congestion
	* - 5-path
	  - 5
	  - :math:`3 \times 3`
	  - 6
	  - 5
	* - 4-cycle
	  - 4
	  - :math:`3 \times 3`
	  - 4
	  - 3

5-path
''''''

The diameter of the 5-path is 6, with the longer paths from :math:`I_0—O_4` as shown below;

.. image:: ../images/networks-5-path-diameter.png
	:align: center

The max congestion of the 5-path is 5, where we have the following permutation;

.. math::

	\begin{aligned}

	\pi(0) &= 4

	\pi(1) &= 3

	\pi(2) &= 2

	\pi(3) &= 1

	\pi(4) &= 0

	\text{this can also be} & \text{ expressed as,}

	\pi(i) &= 4 - i

	\end{aligned}

Every path will then have to pass through the central switch, as shown below;

.. image:: ../images/networks-5-path-max-congestion.png
	:align: center

There can't be congestion higher than 5, however, because there are only 5 paths.

4-cycle
'''''''

The diameter of the 4-cycle is 4 when taking the path from diagonally opposite inputs and outputs.
For example :math:`I_0—O_2`, as shown below,

.. image:: ../images/networks-4-cycle-diameter.png
	:align: center

The max congestion of the 4-cycle is 3, with the following permutation;

.. math::

	\begin{aligned}

	\pi(0) &= 2

	\pi(1) &= 3

	\pi(2) &= 0

	\pi(3) &= 1

	\end{aligned}

.. image:: ../images/networks-4-cycle-max-congestion.png
	:align: center

Each switch has at 3 inputs (2 from switches, 1 from terminal) and 1 output.
Suppose :math:`I_0`'s terminal input crosses through, as well as :math:`I_1` and :math:`I_2`'s.
:math:`I_3` is the last remaining terminal, but notice if we attempt to route through the switch adjacent to :math:`I_0`,
there is an unused route (coloured black below).

.. image:: ../images/networks-4-cycle-invalid-congestion-4.png
	:align: center

Since we always calculate congestion as the 'maximum minimum' congestion, this route wouldn't be chosen.
By symmetry, the same is true for any other terminal-adjacent switch.
Meaning a congestion greater than 3 is not possible on this network.


Routing in a Benes Network
--------------------------

1.  Within the Benes network of size :math:`N = 8`, there are two subnetworks of size :math:`N = 4`.
	Put boxes around these. Hereafter, we’ll refer to these as the upper and lower subnetworks.

	.. raw:: html

		<hr>

	.. image:: ../images/networks-benes-upper-lower.png
		:align: center

2.  Now consider the following permutation routing problem:

	.. math::

		\begin{aligned}

		\pi(0) = 3 &\qquad \pi(4) = 2

		\pi(1) = 1 &\qquad \pi(5) = 0

		\pi(2) = 6 &\qquad \pi(6) = 7

		\pi(3) = 5 &\qquad \pi(7) = 4

		\end{aligned}

	Each packet must be routed through either the upper subnetwork or the lower subnetwork.
	Construct a graph with vertices :math:`0, 1, \dots , 7` and draw a dashed edge between each pair of packets that can not go through the same subnetwork
	because a collision would occur in the second column of switches.

	.. raw:: html

		<hr>

	.. graph:: collision
		:align: center

		edge [style=dotted]

		0 -- 4
		1 -- 5
		2 -- 6
		3 -- 7

3.  Add a solid edge in your graph between each pair of packets that can not go through the same subnetwork
	because a collision would occur in the next-to-last column of switches

	.. raw:: html

		<hr>

	.. graph:: collision
		:align: center

		0 -- 4 [style=dotted]
		1 -- 5 [style=dotted]
		2 -- 6 [style=dotted]
		3 -- 7 [style=dotted]

		5 -- 7
		1 -- 3
		2 -- 4
		0 -- 6

4.  Color (i.e., label) the vertices of your graph red and blue so that adjacent vertices get different colors.
	Why must this be possible, regardless of the permutation :math:`\pi`?

	.. raw:: html

		<hr>

	A 2-coloring must be possible, because the input constraints (dotted lines) are a matching,
	and the output constraints (solid lines) are also a matching. As we showed in :ref:`graph-theory`, problem 1.

	.. graph:: collision
		:align: center

		0, 1, 2, 7 [color=indianred, style=filled]
		3, 4, 5, 6 [color=lightblue, style=filled]

		0 -- 4 [style=dotted]
		1 -- 5 [style=dotted]
		2 -- 6 [style=dotted]
		3 -- 7 [style=dotted]

		5 -- 7
		1 -- 3
		2 -- 4
		0 -- 6

5.  Suppose that red vertices correspond to packets routed through the upper subnetwork
	and blue vertices correspond to packets routed through the lower subnetwork.
	On the attached copy of the Bene˘s network, highlight the first and last edge traversed by each packet.

	.. raw:: html

		<hr>

	.. image:: ../images/networks-benes-first-last-traversed.png
		:align: center

6.  All that remains is to route packets through the upper and lower subnetworks.
	One way to do this is by applying the procedure described above recursively on each subnetwork.
	However, since the remaining problems are small, see if you can complete all the paths on your own.

	.. raw:: html

		<hr>

	.. image:: ../images/networks-benes-complete-traversal.png
		:align: center
