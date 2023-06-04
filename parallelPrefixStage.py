import math

import gate


def get_previous_node_index(previous_nodes: list, current_index: int):
    for index in reversed(range(current_index)):
        if previous_nodes[index] == 1:
            return index
    return current_index - 1


def parse_to_binary(number: int, number_of_bits: int):
    binary_number = [0] * number_of_bits
    index = 0
    while number > 0 and index < number_of_bits:
        binary_number[index] = number % 2
        number //= 2
        index += 1
    return binary_number


def get_parallel_prefix_nodes_positions(rows_number: int, length: int) -> list:
    result = [[0] * length for i in range(rows_number)]

    for row_num in range(rows_number):
        for position in range(length):
            bin_num = parse_to_binary(position, rows_number)
            if bin_num[row_num] == 1:
                result[row_num][position] = 1
    return result


def process(g: list, p: list, g_prim: list, p_prim: list) -> tuple[list, list, list, list]:
    rows = math.ceil(math.log2(len(g)))
    dots_positions = get_parallel_prefix_nodes_positions(rows, len(g))

    for row_num in range(rows):
        for i in reversed(range(len(g))):
            if row_num == 0:
                if dots_positions[row_num][i] == 1:
                    p[i], g[i], p_prim[i], g_prim[i] = gate.parallel_prefix_double_node(p[i], g[i], p[i - 1], g[i - 1],
                                                                                        p_prim[i], g_prim[i],
                                                                                        p_prim[i - 1],
                                                                                        g_prim[i - 1])
            else:
                if dots_positions[row_num][i] == 1:
                    previous_dot = get_previous_node_index(dots_positions[row_num - 1], i)
                    p[i], g[i], p_prim[i], g_prim[i] = gate.parallel_prefix_double_node(p[i], g[i], p[previous_dot],
                                                                                        g[previous_dot],
                                                                                        p_prim[i], g_prim[i],
                                                                                        p_prim[previous_dot],
                                                                                        g_prim[previous_dot])
    return g, p, g_prim, p_prim
