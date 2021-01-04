from itertools import *
from numpy import product, array
import re
from timeit import default_timer as timer


def main(inp, is_real):
    inp = inp.strip()
    v = inp
    for i in range(50):
        new_v = ''
        current = v[0]
        count = 0
        for c in v:
            if c == current:
                count += 1
            else:
                new_v += str(count) + str(current)
                current = c
                count = 1
        new_v += str(count) + str(current)
        v = new_v
    print(len(v))

sample_input = r"""
1
"""

real_input = r"""
1113122113
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
