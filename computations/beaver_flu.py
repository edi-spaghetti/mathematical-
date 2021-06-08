import sys


class BeaverFluInfectionModel(object):

    def __init__(self, state):

        # make sure we're dealing with a list of lists
        assert isinstance(state, list)

        self.n = len(state)

        # make sure inner list is same length as outer
        for i, _ in enumerate(state):
            assert isinstance(state[i], list)
            assert len(state[i]) == self.n

        self.state = state
        self.time_step = 0  # time step
        self.border = list()  # edges not occupied
        self.edges = list()  # all edges
        self.valid_edges = set()  # valid edges (i.e. unique edges in bounds
                                  # and unoccupied)
        self.unique_edges = set()  # unique unoccupied edges
        self.overlaps = set()  # overlapping valid edges
        self.spaces = set()  # remaining spaces
        self._infected = set()  # number infected

    def run(self):

        while self.process_state():
            self.log_state(show_matrix=True)
            self.update_state()
            self.time_step += 1

        self.log_state(show_matrix=True)

    def update_state(self):
        for r, c, value in self.iterate_state():
            if (r, c) in self.overlaps:
                # add 2 because we use 1 for True state on start
                # if we just added 1, then initial state and first round of
                # infection are both represented with 1
                self.state[r][c] = self.time_step + 2

    def iterate_state(self):
        for r, row in enumerate(self.state):
            for c, value in enumerate(row):
                yield r, c, value

    def process_state(self):

        self.invalidate_caches()

        for r, c, value in self.iterate_state():
            if value:
                self.check_edge(r-1, c)  # top
                self.check_edge(r+1, c)  # bottom
                self.check_edge(r, c-1)  # left
                self.check_edge(r, c+1)  # right

        return len(self.overlaps) > 0

    def log_state(self, show_matrix=False):
        sys.stdout.write(
            f't={self.time_step}, '
            f'o={len(self.overlaps)}, '
            f'i={len(self.infected())}, '
            f'p={len(self.border)}'
            f'\n'
        )

        if show_matrix:
            for row in self.state:
                sys.stdout.write(f'{row}\n')

        sys.stdout.flush()

    def check_edge(self, r, c):
        edge = (r, c)
        if not self.is_occupied(r, c):
            self.border.append(edge)

            if self.is_in_bounds(*edge):

                # check if we already added, in which case 2 or more
                # infected are adjacent
                if edge in self.valid_edges:
                    self.overlaps.add(edge)

                self.valid_edges.add(edge)

    def invalidate_caches(self):
        self.border = list()  # edges not occupied
        self.valid_edges = set()  # valid edges (i.e. unique edges in bounds
                                  # and unoccupied)
        self.overlaps = set()  # overlapping valid edges
        self._infected = set()  # number infected

    def infected(self):

        # return cached value
        if self._infected:
            return self._infected

        # recalculate
        infected = set()
        for r, c, value in self.iterate_state():
            if value:
                infected.add((r, c))

        # cache and return
        self._infected = infected
        return infected

    def is_in_bounds(self, r, c):
        if not (0 <= r < self.n):
            return False
        if not (0 <= c < self.n):
            return False

        return True

    def is_occupied(self, r, c):
        try:
            assert r >= 0
            assert c >= 0
            occupied = bool(self.state[r][c])
        except (IndexError, AssertionError):
            occupied = False

        return occupied


def main():
    m = BeaverFluInfectionModel([
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
    ])

    m.run()


if __name__ == '__main__':
    main()
