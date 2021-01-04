from collections import defaultdict, Counter
from functools import lru_cache
from itertools import *
from numpy import product, array
import re
from timeit import default_timer as timer


def get_combinations(inp, target, acc=None):
    if acc is None:
        acc = []
    s = sum(acc)
    if target == 0:
        return [acc]

    res = []
    for i in range(len(inp)):
        val = inp[i]
        if val <= target:
            new_acc = acc.copy()
            new_acc.append(val)
            for x in get_combinations(inp[i+1:], target - val, new_acc):
                res.append(x)
    return res


def main(inp, is_real):
    inp = inp.strip()
    target = 150 if is_real else 25
    inp = sorted([int(x) for x in inp.split('\n')], reverse=True)
    res = get_combinations(inp, target, [])
    m = min([len(x) for x in res])
    print(len(res))
    print(len([x for x in res if len(x) == m]))

sample_input = r"""
20
15
10
5
5
"""

real_input = r"""
50
44
11
49
42
46
18
32
26
40
21
7
18
43
10
47
36
24
22
40
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
