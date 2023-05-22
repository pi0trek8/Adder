import math

import gate


def hamming_weight(number: int) -> int:
    bits = [bit for bit in bin(number) if bit == '1']
    return int(len(bits))


def process(g: list, p: list, g_prim: list, p_prim: list):
    # liczba kropek + trzeba wiedziuec na jakim poziomie beda + moze poslużyc liczba zapisana bitowo i sprawdzenie gdzie jest 1 na którym bicie
    # liczba pieter to sufit(log2 len(liczba))
    double_dot_num = []
    for i in range(len(g)):
        double_dot_num.append(hamming_weight(i))
    print(double_dot_num)
    for row_num in range(math.ceil(math.log2(len(g)))):
        for i in range(len(g)):
            if double_dot_num[i] <= 0:
                continue
            bin_num = [*bin(i).lstrip('0b')]
            bin_num.reverse()

            if bin_num[row_num] == '1':
                p[i], g[i], p_prim[i], g_prim[i] = gate.parallel_prefix_double_node(p[i], g[i], p[i - 1], g[i - 1],
                                                                                    p_prim[i - 1], g_prim[i - 1],
                                                                                    p_prim[i],
                                                                                    g_prim[i])
                double_dot_num[i] -= 1

    return g, p, g_prim, p_prim
