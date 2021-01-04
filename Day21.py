import sys
from collections import defaultdict, Counter
from functools import lru_cache
from itertools import *
from numpy import product, array
import re
from timeit import default_timer as timer


def main(inp, is_real):
    pattern = re.compile(r'(.*) + ([0-9]+) +([0-9]+) +([0-9]*)')
    inp = inp.strip()
    inp = inp.split('\n\n')
    weapons = [re.findall(pattern, i)[0] for i in inp[0].split('\n')[1:]]
    weapons = [[x[0]] + [int(y) for y in x[1:]] for x in weapons]
    armor = [re.findall(pattern, i)[0] for i in inp[1].split('\n')[1:]]
    armor = [[x[0]] + [int(y) for y in x[1:]] for x in armor]
    armor.append(['None', 0, 0, 0])
    rings = [re.findall(pattern, i)[0] for i in inp[2].split('\n')[1:]]
    rings = [[x[0]] + [int(y) for y in x[1:]] for x in rings]
    rings.append(['None', 0, 0, 0])
    rings.append(['None', 0, 0, 0])

    boss_hp, boss_dmg, boss_arm = [int(s.split(': ')[1]) for s in inp[3].split('\n')]

    min_cost = sys.maxsize
    max_cost = 0
    item_list = []
    item_list_loss = []
    for w in weapons:
        for a in armor:
            for r in combinations(rings, 2):
                items = [w, a] + list(r)
                cost = sum([x[1] for x in items])
                dmg = sum([x[2] for x in items])
                arm = sum([x[3] for x in items])
                dmg_dealt = max(1, dmg - boss_arm)
                dmg_taken = max(1, boss_dmg - arm)
                if dmg_dealt >= dmg_taken and cost < min_cost:
                    min_cost = cost
                    item_list = items
                if dmg_dealt < dmg_taken and cost > max_cost:
                    max_cost = cost
                    item_list_loss = items
    print(f'{min_cost} with {item_list}')
    print(f'{max_cost} with {item_list_loss}')



sample_input = r"""

"""

real_input = r"""
Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3

Hit Points: 100
Damage: 8
Armor: 2
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
