from collections import defaultdict, Counter
from functools import lru_cache
from itertools import *
from numpy import product, array
import re
import sys
from timeit import default_timer as timer


def main(inp, is_real):
    inp = inp.strip()
    inp = inp.split('\n')
    ins = []
    for i in inp:
        cmd, rest = i[0:3], i[4:]
        ins.append([cmd] + rest.split(', '))
    ptr = 0
    reg = {'a': 1, 'b': 0}
    while ptr < len(ins):
        cur = ins[ptr]
        if cur[0] == 'inc':
            reg[cur[1]] += 1
        elif cur[0] == 'hlf':
            reg[cur[1]] = int(reg[cur[1]] / 2)
        elif cur[0] == 'tpl':
            reg[cur[1]] *= 3
        elif cur[0] == 'jmp':
            ptr += int(cur[1])
            continue
        elif cur[0] == 'jie':
            if reg[cur[1]] % 2 == 0:
                ptr += int(cur[2])
                continue
        elif cur[0] == 'jio':
            if reg[cur[1]] == 1:
                ptr += int(cur[2])
                continue
        else:
            assert False
        ptr += 1
    print(reg['b'])


sample_input = r"""
inc a
jio a, +2
tpl a
inc a
"""

real_input = r"""
jio a, +18
inc a
tpl a
inc a
tpl a
tpl a
tpl a
inc a
tpl a
inc a
tpl a
inc a
inc a
tpl a
tpl a
tpl a
inc a
jmp +22
tpl a
inc a
tpl a
inc a
inc a
tpl a
inc a
tpl a
inc a
inc a
tpl a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
jio a, +8
inc b
jie a, +4
tpl a
inc a
jmp +2
hlf a
jmp -7
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
