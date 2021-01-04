from collections import defaultdict, Counter
from functools import lru_cache
from itertools import *
from numpy import product, array
import re
import sys
from timeit import default_timer as timer


def main(inp, is_real):
    inp = inp.strip()
    inp = set([int(x) for x in inp.split('\n')])
    inp = set(sorted(inp, reverse=True))

    lowest = sys.maxsize
    for i in range(1, len(inp)):
        for g1 in combinations(inp, i):
            size1 = sum(g1)
            remaining = inp.difference(g1)
            if sum(remaining) == 3 * size1:
                for j in range(1, len(remaining)):
                    for g2 in combinations(remaining, j):
                        size2 = sum(g2)
                        if size2 != size1:
                            continue
                        remaining2 = remaining.difference(g2)
                        if sum(remaining2) == 2 * size2:
                            for k in range(1, len(remaining2)):
                                for g3 in combinations(remaining2, k):
                                    g4 = remaining2.difference(g3)
                                    if sum(g3) == sum(g4):
                                        print(f'found possibility: {product(g1)}')
                                        return


sample_input = r"""
1
2
3
4
5
7
8
9
10
11
"""

real_input = r"""
1
2
3
5
7
13
17
19
23
29
31
37
41
43
53
59
61
67
71
73
79
83
89
97
101
103
107
109
113
"""


if len(sample_input.strip()) > 0:
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
