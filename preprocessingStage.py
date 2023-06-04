import gate


def hashed_cells(a: list, b: list, k: list) -> tuple[list[int], list[int], list[int], list[int], list[int]]:
    length = len(a) if len(a) >= len(b) else len(b)

    g = [0] * len(a)
    p = [0] * len(a)
    h = [0] * len(a)
    a_prim = [0] * len(a)
    b_prim = [0] * len(a)

    for i in range(length):
        g[i] = gate.and_gate(a[i], b[i])
        p[i] = gate.or_gate(a[i], b[i])
        h[i] = gate.and_gate(not g[i], p[i])

        if k[i] == 0:
            a_prim[i] = h[i]
        else:
            a_prim[i] = int(not h[i])

        if i != len(a) - 1:
            b_prim[i + 1] = p[i] if k[i] == 1 else g[i]

    return g, p, h, a_prim, b_prim


def envelop_cells(a_prim: list, b_prim: list) -> tuple[list[int], list[int], list[int]]:
    length = len(a_prim) if len(a_prim) >= len(b_prim) else len(b_prim)

    g_prim = [0] * length
    p_prim = [0] * length
    h_prim = [0] * length

    for i in range(length):
        g_prim[i] = gate.and_gate(a_prim[i], b_prim[i])
        p_prim[i] = gate.or_gate(a_prim[i], b_prim[i])
        h_prim[i] = gate.and_gate(not g_prim[i], p_prim[i])

    return g_prim, p_prim, h_prim
