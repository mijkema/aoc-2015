from collections import defaultdict, Counter
from functools import lru_cache
from itertools import *
from random import randint

from numpy import array
import re
from timeit import default_timer as timer


def main(inp, is_real):
    inp = inp.strip()
    rules, inp = inp.split('\n\n')
    inp = str(inp)
    rules = list([x.split(' => ') for x in rules.split('\n')])
    molecules = set()
    for i in range(len(inp)):
        for r in rules:
            if r[0] == inp[i:i+len(r[0])]:
                molecules.add(inp[0:i] + r[1] + inp[i+len(r[0]):])

    result = 0
    formula = inp
    while formula != 'e':
        applicable = [r for r in rules if r[1] in formula]
        if len(applicable) == 0:
            formula = inp
            result = 0
            continue
        to_apply = applicable[randint(0, len(applicable) - 1)]
        formula = formula.replace(to_apply[1], to_apply[0], 1)
        result += 1
    print(result)
    print(f'Length: {len(re.findall(r"[A-Z][a-z]*", inp))}, Rn: {inp.count("Rn")}, Ar: {inp.count("Ar")}, Y: {inp.count("Y")}')


sample_input = r"""
H => HO
H => OH
O => HH
e => H
e => O

HOHOHO
"""

real_input = r"""
Al => ThF
Al => ThRnFAr
B => BCa
B => TiB
B => TiRnFAr
Ca => CaCa
Ca => PB
Ca => PRnFAr
Ca => SiRnFYFAr
Ca => SiRnMgAr
Ca => SiTh
F => CaF
F => PMg
F => SiAl
H => CRnAlAr
H => CRnFYFYFAr
H => CRnFYMgAr
H => CRnMgYFAr
H => HCa
H => NRnFYFAr
H => NRnMgAr
H => NTh
H => OB
H => ORnFAr
Mg => BF
Mg => TiMg
N => CRnFAr
N => HSi
O => CRnFYFAr
O => CRnMgAr
O => HP
O => NRnFAr
O => OTi
P => CaP
P => PTi
P => SiRnFAr
Si => CaSi
Th => ThCa
Ti => BP
Ti => TiTi
e => HF
e => NAl
e => OMg

ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF
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
