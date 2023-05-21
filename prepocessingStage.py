class PreprocessingStage:
    @staticmethod
    def hashed_cells(a: list, b: list, k: list):
        g = [0 for i in range(len(a) or len(b))]
        p = [0 for i in range(len(a) or len(b))]
        h = [0 for i in range(len(a) or len(b))]
        a_prim = [0 for i in range(len(a) or len(b))]
        b_prim = [0 for i in range(len(a) or len(b))]

        for i in range(len(a) or len(b)):
            g[i] = 1 if a[i] and b[i] else 0
            p[i] = 1 if a[i] or b[i] else 0
            h[i] = 1 if not g[i] and p[i] else 0

            a_prim[i] = h[i] if k[i] == 0 else (0 if not h[i] else 1)

            if i != len(a) - 1:
                b_prim[i + 1] = p[i] if k[i] == 1 else g[i]

        return g, p, h, a_prim, b_prim

    @staticmethod
    def envelop_cells(a_prim: list, b_prim: list):
        g_prim = [0 for i in range(len(a_prim) or len(b_prim))]
        p_prim = [0 for i in range(len(a_prim) or len(b_prim))]
        h_prim = [0 for i in range(len(a_prim) or len(b_prim))]

        for i in range(len(a_prim)):
            g_prim[i] = 1 if a_prim[i] and b_prim[i] else 0
            p_prim[i] = 1 if a_prim[i] or b_prim[i] else 0
            h_prim[i] = 1 if not g_prim[i] and p_prim[i] else 0

        return g_prim, p_prim, h_prim
