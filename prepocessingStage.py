import gate


class PreprocessingStage:
    @staticmethod
    def hashed_cells(a: list, b: list, k: list):
        g = [0] * len(a)
        p = [0] * len(a)
        h = [0] * len(a)
        a_prim = [0] * len(a)
        b_prim = [0] * len(a)

        for i in range(len(a) or len(b)):
            g[i] = gate.and_gate(a[i], b[i])
            p[i] = gate.or_gate(a[i], b[i])
            h[i] = gate.and_gate(not g[i], p[i])

            a_prim[i] = h[i] if k[i] == 0 else (0 if not h[i] else 1)
            if i != len(a) - 1:
                b_prim[i + 1] = p[i] if k[i] == 1 else g[i]

        return g, p, h, a_prim, b_prim

    @staticmethod
    def envelop_cells(a_prim: list, b_prim: list):
        g_prim = [0] * len(a_prim)
        p_prim = [0] * len(a_prim)
        h_prim = [0] * len(a_prim)

        for i in range(len(a_prim)):
            g_prim[i] = gate.and_gate(a_prim[i], b_prim[i])
            p_prim[i] = gate.or_gate(a_prim[i], b_prim[i])
            h_prim[i] = gate.and_gate(not g_prim[i], p_prim[i])

        return g_prim, p_prim, h_prim
