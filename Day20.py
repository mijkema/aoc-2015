from collections import defaultdict, Counter
from functools import lru_cache
from itertools import *
from numpy import product, array
from math import *
import re
from timeit import default_timer as timer


def get_divisors(n):
    divisors = set()
    i = 1
    while i <= sqrt(n):
        if n % i == 0:
            if n / i == i:
                divisors.add(i)
            else:
                divisors.add(i)
                divisors.add(int(n/i))
        i += 1
    return divisors


def main(inp, is_real):
    inp = inp.strip()
    inp = int(inp)

    for i in count(int(inp / 10 / 5)):
        divs = get_divisors(i)
        s = sum([d * 11 for d in divs if i / d <= 50])
        if s >= inp:
            print(f'{i}: {s / 10}')
            return


sample_input = r"""
300
"""

real_input = r"""
36000000
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
