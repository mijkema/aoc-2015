from itertools import *
from numpy import product, array
import re
from timeit import default_timer as timer

base = ord('a')
char_o = ord('o') - base
char_i = ord('i') - base
char_l = ord('l') - base


def to_digit(inp, pows):
    return sum(pows[i] * (ord(inp[i]) - base) for i in range(len(pows)))


def to_chrs(inp, pows):
    res = []
    val = inp
    for i in range(len(pows)):
        q, r = divmod(val, pows[i])
        res.append(q)
        val = r
    return res


def to_str(inp, pows):
    return [chr(i + base) for i in to_chrs(inp, pows)]


def is_valid(inp, pows):
    pw = to_chrs(inp, pows)
    v1 = False
    v2 = False
    pair = -1
    for i in range(len(pw)):
        if i >= 2 and pw[i] - 1 == pw[i-1] and pw[i-1] - 1 == pw[i-2]:
            v1 = True
        if pw[i] == char_i or pw[i] == char_l or pw[i] == char_o:
            return False
        if i >= 1 and pw[i] == pw[i-1]:
            if pair == -1:
                pair = pw[i]
            elif pair != pw[i]:
                v2 = True
    return v1 and v2


def main(inp, is_real):
    inp = inp.strip()
    pows = [pow(26, len(inp)-1-i) for i in range(len(inp))]
    inp = to_digit(inp, pows)
    while not is_valid(inp, pows):
        inp += 1
    print(''.join(to_str(inp, pows)))

    inp += 1
    while not is_valid(inp, pows):
        inp += 1
    print(''.join(to_str(inp, pows)))

sample_input = r"""
abcdefgh
"""

real_input = r"""
cqjxjnds
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
