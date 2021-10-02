from functools import reduce
from typing import Dict


def topological_sort(graph: Dict[str, Dict[str, set]]):
    """
    Applies topological sort using Kahn's algorithm.
    :param graph: directed graph of nodes with both upstream and downstream
    :return: nodes of the graph
    """

    # init container for our finished topological sort
    top_sort = list()

    # initialise 'source nodes' as nodes with no upstream dependency
    source = [n for n in graph if not graph[n]['up']]

    while source:
        node = source.pop(0)
        top_sort.append(node)
        downstream = [n for n in graph[node]['down']]
        for child in downstream:
            try:
                graph[child]['up'].remove(node)
            except KeyError:
                print(f'upstream {node} is already removed from {child}')
            try:
                graph[node]['down'].remove(child)
            except KeyError:
                print(f'downstream {child} is already removed from {node}')
            if not graph[child]['up']:
                source.insert(0, child)

    # check if any edges remain, which indicates there are cycles
    edges = set(reduce(
        lambda a, b: a.union(b),
        [graph[n]['up'] for n in graph]))
    if edges:
        raise TypeError(f'Graphs with cycles cannot be topologically sorted: '
                        f'{edges}')

    return top_sort


def main():
    graph = {
        '6.01':  {'up': set(),             'down': {'6.004', '6.034', '6.003'}},
        '8.01':  {'up': set(),             'down': {'8.02'}},
        '18.01': {'up': set(),             'down': {'18.03', '18.02', '6.042'}},
        '6.034': {'up': {'6.01'},          'down': set()},
        '8.02':  {'up': {'8.01'},          'down': {'6.02'}},
        '18.03': {'up': {'18.01'},         'down': {'6.02'}},
        '18.02': {'up': {'18.01'},         'down': set()},
        '6.042': {'up': {'18.01'},         'down': {'6.046'}},
        '6.046': {'up': {'6.042'},         'down': {'6.840'}},
        '6.840': {'up': {'6.046'},         'down': set()},
        '6.02':  {'up': {'8.02', '18.03'}, 'down': {'6.004', '6.003'}},
        '6.004': {'up': {'6.01', '6.02'},  'down': {'6.033'}},
        '6.003': {'up': {'6.01', '6.02'},  'down': set()},
        '6.033': {'up': {'6.004'},         'down': {'6.857'}},
        '6.857': {'up': {'6.033'},         'down': set()},
    }
    top_sort = topological_sort(graph)
    print(', '.join(top_sort))


if __name__ == '__main__':
    main()
