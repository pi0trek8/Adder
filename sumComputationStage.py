from gate import xor_gate
from gate import buffer


class SumComputationStage:
    @staticmethod
    def compute_s(h: list, h_prim: list, c: list, c_prim: list) -> list:
        s = []
        C_out = c[-1]

        for i in range(len(h)):
            if i == 0:
                s.append(buffer(h[i], h_prim[i], C_out))
            else:
                c_prev = buffer(c[i - 1], c_prim[i - 1], C_out)
                h_prev = buffer(h[i], h_prim[i], C_out)
                s.append(xor_gate(h_prev, c_prev))
        return s
