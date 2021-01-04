from collections import defaultdict, Counter
from functools import lru_cache
from itertools import *
from numpy import product, array
import re
from timeit import default_timer as timer


def get_combinations(ingredients, r):
    if len(ingredients) == 1:
        return [[r]]
    result = []
    for i in range(1, r):
        for j in get_combinations(ingredients[1:], r-i):
            result.append([i] + j)
    return result


def main(inp, is_real):
    inp = inp.strip()
    inp = inp.split('\n')
    ing = {}
    props = 5
    for i in inp:
        name, cap, dur, fla, tex, cal = re.findall(
            r'(.*): capacity (.*), durability (.*), flavor (.*), texture (.*), calories (.*)', i)[0]
        ing[name] = [int(cap), int(dur), int(fla), int(tex), int(cal)]
    keys = list(ing.keys())
    score = 0
    for weights in get_combinations(keys, 100):
        vals = []
        for prop in range(props - 1):
            v = 0
            for k in range(len(keys)):
                v += ing[keys[k]][prop] * weights[k]
            vals.append(max(v, 0))
        s = product(vals)
        calories = 0
        for k in range(len(keys)):
            calories += ing[keys[k]][-1] * weights[k]
        if s > score and calories == 500:
            score = s
    print(score)

sample_input = r"""
Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
"""

real_input = r"""
Sprinkles: capacity 5, durability -1, flavor 0, texture 0, calories 5
PeanutButter: capacity -1, durability 3, flavor 0, texture 0, calories 1
Frosting: capacity 0, durability -1, flavor 4, texture 0, calories 6
Sugar: capacity -1, durability 0, flavor 0, texture 2, calories 8
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
