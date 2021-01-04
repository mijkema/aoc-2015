from itertools import *
from numpy import product
import re
from timeit import default_timer as timer
from hashlib import md5

def main(input, is_real):
    input = input.strip()
    for i in count():
        hash = md5((input + str(i)).encode()).hexdigest()
        if hash.startswith('000000'):
            print(f"hash {hash} at {i}")
            return
        i += 1

sample_input = """
abcdef
"""

real_input = """
iwrupvqb
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

