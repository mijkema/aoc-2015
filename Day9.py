from dataclasses import dataclass
from itertools import *
from numpy import product, array
import re
from timeit import default_timer as timer


@dataclass
class Node:
    name: str
    connections: {}

    def add_connection(self, dest: str, dist: int):
        self.connections[dest] = dist


def find_paths(seen, nodes, current):
    if len(nodes) == len(seen):
        return [seen]

    c = nodes[current].connections
    all_paths = []
    for n, dist in c.items():
        if n in seen:
            continue
        s = dict(seen)
        s[n] = max(s.values()) + dist
        for p in find_paths(s, nodes, n):
            all_paths.append(p)
    return all_paths


def find(nodes, shortest):
    all_paths = {}
    for n in nodes:
        seen = {n: 0}
        for p in find_paths(seen.copy(), nodes, n):
            all_paths[repr(p)] = max(p.values())

    return min(all_paths.values()) if shortest else max(all_paths.values())


def main(inp, is_real):
    inp = inp.strip()
    inp = inp.split('\n')
    nodes = {}
    for i in inp:
        orig, dest, dist = re.fullmatch(r'(.*) to (.*) = (.*)', i).groups()
        dist = int(dist)
        if orig in nodes:
            nodes[orig].add_connection(dest, dist)
        else:
            nodes[orig] = Node(orig, {dest: dist})
        if dest in nodes:
            nodes[dest].add_connection(orig, dist)
        else:
            nodes[dest] = Node(dest, {orig: dist})

    print(find(nodes, True))
    print(find(nodes, False))

sample_input = r"""
London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
"""

real_input = r"""
Faerun to Norrath = 129
Faerun to Tristram = 58
Faerun to AlphaCentauri = 13
Faerun to Arbre = 24
Faerun to Snowdin = 60
Faerun to Tambi = 71
Faerun to Straylight = 67
Norrath to Tristram = 142
Norrath to AlphaCentauri = 15
Norrath to Arbre = 135
Norrath to Snowdin = 75
Norrath to Tambi = 82
Norrath to Straylight = 54
Tristram to AlphaCentauri = 118
Tristram to Arbre = 122
Tristram to Snowdin = 103
Tristram to Tambi = 49
Tristram to Straylight = 97
AlphaCentauri to Arbre = 116
AlphaCentauri to Snowdin = 12
AlphaCentauri to Tambi = 18
AlphaCentauri to Straylight = 91
Arbre to Snowdin = 129
Arbre to Tambi = 53
Arbre to Straylight = 40
Snowdin to Tambi = 15
Snowdin to Straylight = 99
Tambi to Straylight = 70
"""


print("sample:")
start = timer()
main(sample_input, False)
end = timer()
print(f'sample: {(end-start)*1000_000:.0f}μs ({(end-start)*1000:.0f}ms)')


print("real:")
start = timer()
main(real_input, True)
end = timer()
print(f'sample: {(end-start)*1000_000:.0f}μs ({(end-start)*1000:.0f}ms)')
