from collections import defaultdict, Counter
from functools import lru_cache
from itertools import *
from numpy import product, array
import re
from timeit import default_timer as timer


def main(inp, is_real):
    inp = inp.strip()
    inp = inp.split('\n')
    time = 2503 if is_real else 1000
    furthest = 0
    dists = defaultdict(dict)
    for i in inp:
        deer, speed, dur, rest = re.findall(
            r'(.*) can fly (.*) km/s for (.*) seconds, but then must rest for (.*) seconds', i)[0]
        speed = int(speed)
        dur = int(dur)
        rest = int(rest)
        dist = 0
        for j in range(time):
            if j % (dur + rest) < dur:
                dist += speed
            dists[j][deer] = dist
        if dist > furthest:
            furthest = dist
    print(furthest)

    points = defaultdict(lambda: 0)
    for i, d in dists.items():
        m = max(d.values())
        for name, dist in d.items():
            if dist == m:
                points[name] += 1
    print(points)

sample_input = r"""
Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
"""

real_input = r"""
Rudolph can fly 22 km/s for 8 seconds, but then must rest for 165 seconds.
Cupid can fly 8 km/s for 17 seconds, but then must rest for 114 seconds.
Prancer can fly 18 km/s for 6 seconds, but then must rest for 103 seconds.
Donner can fly 25 km/s for 6 seconds, but then must rest for 145 seconds.
Dasher can fly 11 km/s for 12 seconds, but then must rest for 125 seconds.
Comet can fly 21 km/s for 6 seconds, but then must rest for 121 seconds.
Blitzen can fly 18 km/s for 3 seconds, but then must rest for 50 seconds.
Vixen can fly 20 km/s for 4 seconds, but then must rest for 75 seconds.
Dancer can fly 7 km/s for 20 seconds, but then must rest for 119 seconds.
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
