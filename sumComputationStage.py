from gate import xor_gate
from gate import buffer
from gate import or_gate


def compute_s(h: list, h_prim: list, carry: list, carry_prim: list) -> list:
    _sum = []
    c_out = or_gate(carry_prim[-1], carry[-1])

    for i in range(len(h)):
        if i == 0:
            _sum.append(buffer(h[i], h_prim[i], c_out))
        else:
            c_prev = buffer(carry[i - 1], carry_prim[i - 1], c_out)
            h_prev = buffer(h[i], h_prim[i], c_out)
            _sum.append(xor_gate(h_prev, c_prev))
    return _sum


a = 1
b = 0
c = 0

print(buffer(b, a, c))
