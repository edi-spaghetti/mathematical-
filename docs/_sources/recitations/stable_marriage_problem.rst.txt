A Protocol For College Admission
================================

Next, we are going to talk about a generalization of the stable marriage problem.
The problem we’re going to talk about is a generalization of the one done in lecture.
In the new problem, there are N students :math:`s_1, s_2, \dots , s_N and M` universities :math:`u_1, u_2, \dots , u_M`.

University :math:`u_i` has :math:`n_i` slots for students, and we’re guaranteed that :math:`\sum_{i=1}^M n_i = N`.
Each student ranks all universities (no ties) and each university ranks all students (no ties).

Design an algorithm to assign students to universities with the following properties

1.  Every student is assigned to one university.

2.  :math:`\forall i, u_i` gets assigned :math:`n_i` students.

3.  There does not exist :math:`s_i, s_j , u_k, u_l` where :math:`s_i` is assigned to :math:`u_k`, :math:`s_j` is assigned to :math:`u_l`,
	:math:`s_j` prefers :math:`u_k` to :math:`u_l`, and :math:`u_k` prefers :math:`s_j` to :math:`s_i`.

4.  It is student-optimal. This means that of all possible assignments satisfying the first three properties,
	the students get their top choice of university amongst these assignments.
	The algorithm will be a slight modification of the mating algorithm given in lecture.

.. raw:: html

	<hr>

1. **Before we can say anything about our algorithm, we need to show that it terminates.**
   **Show that the algorithm terminates after NM + 1 days**

.. raw:: html

	<hr>

The algorithm terminates when each university has every slot filled with students.
Each iteration, students 'apply' to the university they rank highest that they haven't crossed off already.
If a university has more applicants than slots, they order the applicants by their own ranking.
They then reject any that exceed the number of slots they have available (so lowest ranked get rejected first).

This means at least one student is rejected by one university on each iteration.
If there are no rejections, it means every slot is filled, so the algorithm terminates.

Since there are N students and M universities, each student can try each university at most, once (which gives us :math:`N \cdot M`).
At this point every student will have found a match, so the algorithm terminates.
:math:`\blacksquare`

2. **Next, we will show that the four properties stated earlier are true of our algorithm.**
   **To start, let’s show the following:**
   **if during some day a university** :math:`\ u_j\ ` **has at least** :math:`\ n_j\ ` **applicants,**
   **then when the algorithm terminates it accepts exactly** :math:`\ n_j\ ` **students.**

.. raw:: html

	<hr>

When a university receives any application, the university is those applicants top choice so far.
This means, unless they are rejected by the university, they will still be applying to it on the next iteration.

Since :math:`n_j` refers to the capacity of the university, The university will only reject students :math:`n_j + 1` and beyond.
This means there are still :math:`n_j` applicants for whom :math:`u_j` is their top choice, and so they will apply on the next iteration.

By this, we can conclude that there will be at least :math:`n_j` applications for university :math:`u_j` when the algorithm terminates.
:math:`\blacksquare`

3. **Next, show that every student is assigned to one university.**

.. raw:: html

	<hr>

**Invariant**: If a university, :math:`u_i` rejects a student, :math:`s_j`,
it's because there are :math:`n_i` students ranked higher than :math:`s_j` also applying.

**Proof**: Suppose there are less than :math:`n_i` students also applying.
Then :math:`u_i` still has space for :math:`s_j`, so it doesn't reject :math:`s_j`.
Therefore the invariant is vacuously true.
:math:`\square`

**Theorem**: Every student is assigned to one university.

**Proof**: By contradiction. Assume, when the algorithm terminates there exists a student rejected by all universities.
That means every university has higher ranked students.
But since the algorithm has terminated, it means every university has every slot filled.
By since :math:`\sum_{i=1}^M n_i = N` that can't be possible, which is a contradiction.
So we can conclude that every student is assigned to one university.
:math:`\blacksquare`

4. **Next, show that for all i,** :math:`\ u_i\ ` **gets assigned** :math:`\ n_i\ ` **students.**

.. raw:: html

	<hr>

**Proof** By contradiction.
Assume, when the algorithm terminates there exists a university :math:`u_i`,
for some :math:`i \le M`, that has x applicants, for some x less than :math:`n_i`.
Since the algorithm has terminated we can assume no students have been rejected,
and no universities has more applicants than slots.
But since :math:`\sum_{i=1}^M n_i = N`, we know that there are :math:`N - n_i` slots available at other universities,
and :math:`N - x` students applying to other universities.
Since x is less than :math:`n_i`, then :math:`N - n_i < N - x`, which means there are less slots available than applicants.
So by the algorithm, some of them will be rejected. So the algorithm cannot have terminated.
This is a contradiction, so we can conclude that all universities get assigned a full roster of students.
:math:`\blacksquare`

5. **Before continuing, we need to establish the following property.**
   **Suppose that on some day a university** :math:`\ u_j\ ` **has at least** :math:`\ n_j\ ` **applicants.**
   **Define the rank of an applicant** :math:`\ s_i\ ` **with respect to a university** :math:`\ u_j\ ` **as** :math:`\ s_i` **’s location on** :math:`\ u_j` **’s preference list.**
   **So, for example,** :math:`\ u_j` **’s favorite student has rank 1.**
   **Show that the rank of** :math:`\ u_j` **’s least favorite applicant that it says “Maybe, . . .” to cannot decrease**
   **(e.g., going from 1000 to 1005 is decreasing) on any future day.**

   **Note that** :math:`\ u_j` **’s least favorite applicant might change from one day to the next.**

.. raw:: html

	<hr>

If :math:`s_i` was previously the least favourite accepted applicant,
and there were at least :math:`n_j` applicants, then all slots were filled.

If a student is not rejected, they continue to apply to the same university,
because that university is currently their top choice,
so the next iteration those :math:`n_j` students will continue to apply to :math:`u_j`.

Suppose another student, :math:`s_k` applies on the next iteration as well.
If :math:`s_k` is preferred by the university, then :math:`s_i` will by bumped off the list,
in favour of the next highest ranked student (which may or may not be :math:`s_k`).

Suppose :math:`s_k` was ranked lower than :math:`s_i`, then the university would prefer :math:`s_i` over :math:`s_k`,
so they would reject :math:`s_k` because there are no more slots left.

So the least favourite applicant's ranking can get no lower than :math:`s_i`'s ranking.
:math:`\blacksquare`

6. **Next, show there does not exist** :math:`\ s_i, s_j, u_k,\ and\ u_l\ ` **where** :math:`\ s_i\ ` **is assigned to** :math:`u_k`,
   :math:`s_j\ ` is assigned to :math:`u_l`, :math:`s_j\ ` **prefers** :math:`\ u_k\ ` **to** :math:`\ u_l\ `, **and** :math:`\ uk\ ` **prefers** :math:`\ s_j\ ` **to** :math:`\ s_i\ `.
   **Note that this is analogous to a “rogue couple” considered in lecture.**

.. raw:: html

	<hr>

**Proof**: By contradiction.

Suppose we have a student, :math:`s_r` and a university :math:`u_g` that are not matched up, and form a rogue couple.

**Case 1**: :math:`u_g` rejected :math:`s_r` for another student.
But then :math:`u_g` has a preferred match, so they are not a rogue couple.

**Case 2**: The algorithm terminated before :math:`s_r` applied to :math:`u_g`.
But then :math:`s_r` was accepted by a university they prefer over :math:`u_g`, so they are not a rogue couple.

This proves that for any pair, there are no rogue couples.
:math:`\blacksquare`

7. **Finally, we show in a very precise sense that this algorithm is student-optimal.**
   **As in lecture, define the realm of possibility of a student to be the set of all universities** *u*,
   **for which there exists some assignment satisfying the first three properties above,**
   **in which the student is assigned to u**.
   **Of all universities in the realm of possibility of a student we say that the student’s favorite is optimal for that student.**

   **Show that each student is assigned to its optimal university.**

.. raw:: html

	<hr>

Suppose we have student :math:`s_i` that is the first to not be assigned their optimal university, :math:`u_k`.
:math:`u_k` must have rejected :math:`s_i` in favour of :math:`n_k` other students :math:`s_a \dots s_j` where :math:`n_k` is the maximum capacity of :math:`u_k`.

Since :math:`s_i` was the first to be rejected by their optimal university,
All students in :math:`s_a \dots s_j` haven't been rejected by their optimal university,
and so must rank :math:`u_k` better than or equal to their optimal university.

Since :math:`u_k` is in :math:`s_i`'s realm of possibility,
there must be some stable matching, S, where :math:`s_i` could be assigned to :math:`u_k`.

We know :math:`u_k` ranks all of the students in :math:`s_a \dots s_j` better than :math:`s_i`.
However, in S, one of the students in :math:`s_a \dots s_j`, let's say :math:`s_j`,
would have to be matched with another university, :math:`u_l`, which it ranks worse than :math:`u_k`,
since by accepting :math:`s_i`, there would be no space for :math:`s_j`.

So :math:`s_j` prefers :math:`u_k` to :math:`u_l`, and :math:`u_k` prefers :math:`s_j` to :math:`s_i`.
This forms a rogue couple, which contradict the three properties above.

Therefore, there cannot exist a stable matching where :math:`s_i` is rejected by their optimal choice.
It follows then, that any given student's true optimal choice is the university they were not rejected from, which is the one they end up with.
:math:`\blacksquare`
