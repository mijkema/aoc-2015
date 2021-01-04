from collections import defaultdict, Counter
from functools import lru_cache
from itertools import *
from numpy import product, array
import re
import sys
from timeit import default_timer as timer

best = sys.maxsize


def min_costs(boss_hp, boss_dmg, hp, mana, effects, mana_spent, turns=0):
    global best
    if mana_spent >= best:
        return sys.maxsize

    res = sys.maxsize
    for spell in range(5):
        _bh = boss_hp
        _bd = boss_dmg
        _hp = hp
        _mana = mana
        _effects = effects.copy()
        _ms = mana_spent

        # apply effects
        if _effects[1] > 0:
            _bh -= 3
        if _effects[2] > 0:
            _mana += 101
        _effects = [max(0, e - 1) for e in _effects]

        # 'hard' mode
        _hp -= 1
        if _hp <= 0:
            continue

        # perform spell
        if spell == 0 and _mana >= 53:  # missile
            _bh -= 4
            _mana -= 53
            _ms += 53
        elif spell == 1 and _mana >= 73:  # drain
            _bh -= 2
            _hp += 2
            _mana -= 73
            _ms += 73
        elif spell == 2 and _mana >= 113 and _effects[0] == 0:  # shield
            _effects[0] = 6
            _mana -= 113
            _ms += 113
        elif spell == 3 and _mana >= 173 and _effects[1] == 0:  # poison
            _effects[1] = 6
            _mana -= 173
            _ms += 173
        elif spell == 4 and _mana >= 229 and _effects[2] == 0:  # recharge
            _effects[2] = 5
            _mana -= 229
            _ms += 229
        else:
            # can not cast this spell now
            continue

        # apply effects
        if _effects[1] > 0:
            _bh -= 3
        if _effects[2] > 0:
            _mana += 101
        _effects = [max(0, e - 1) for e in _effects]

        if _bh <= 0:
            cost = _ms
            if cost < res:
                res = cost
            continue

        # boss to apply damage
        _hp -= _bd if _effects[0] == 0 else _bd - 7

        # check if we lost
        if _hp <= 0:
            continue

        cost = min_costs(_bh, _bd, _hp, _mana, _effects, _ms, turns + 1)
        if cost < res:
            res = cost
            if res < best:
                best = res

    return res


def main(inp, is_real):
    inp = inp.strip()
    boss_hp, boss_dmg = 55, 8

    hp = 50
    mana = 500
    effects = [0, 0, 0]

    print(min_costs(boss_hp, boss_dmg, hp, mana, effects, 0))


sample_input = r"""

"""

real_input = r"""
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
