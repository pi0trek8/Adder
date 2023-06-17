import preprocessingStage
import sumComputationStage
import parallelPrefixStage
import sys

Bin = list[int]


def decToBin(decimal_num: int, num_bits: int = 0) -> Bin:
    binary_list = []
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_list.insert(0, int(remainder))
        decimal_num //= 2

    while len(binary_list) < num_bits:
        binary_list.insert(0, 0)

    return binary_list


def binToDec(binary_list: Bin) -> int:
    decimal_num = 0
    for i in range(len(binary_list)):
        if binary_list[i]:
            decimal_num += 2 ** (len(binary_list) - 1 - i)
    return decimal_num


def main():
    bit_numer = 7
    first_number_a = decToBin(int(sys.argv[1]), bit_numer)
    second_number_b = decToBin(int(sys.argv[2]), bit_numer)
    modulo_controller = decToBin(int(sys.argv[3]), bit_numer)

    carry_generate_vector, carry_propagate_vector, half_sum_vector, a_prim, b_prim = preprocessingStage.hashed_cells(
        first_number_a, second_number_b, modulo_controller)

    g_prim, p_prim, h_prim = preprocessingStage.envelop_cells(a_prim, b_prim)
    carry_generate_vector, carry_propagate_vector, g_prim, p_prim = parallelPrefixStage.process(carry_generate_vector,
                                                                                                carry_propagate_vector,
                                                                                                g_prim, p_prim)

    print('a=', first_number_a)
    print('b=', second_number_b)
    print('k=', modulo_controller)
    print()
    print('half sum vector (h) = ', half_sum_vector)
    print('carry propagate vector (p) = ', carry_propagate_vector)
    print('carry generate vector (g) = ', carry_generate_vector)
    print()
    print('half sum from enveloped cells (h`) = ', h_prim)
    print('carry propagate vector from enveloped cells (p`) = ', p_prim)
    print('carry generate vector from enveloped cells (g`) = ', g_prim)

    sum_vector = sumComputationStage.compute_s(half_sum_vector, h_prim, carry_generate_vector, g_prim)
    sum_vector.reverse()
    print()
    print('sum vector = ', sum_vector)
    print('Result:', binToDec(sum_vector))


def test():
    bit_number = 7
    k = 4
    for a in range(0, 2 ** bit_number - k):
        for b in range(0, 2 ** bit_number - k):
            first_number_a = decToBin(a, bit_number)
            second_number_b = decToBin(b, bit_number)
            modulo_controller = decToBin(k, bit_number)
            first_number_a.reverse()
            second_number_b.reverse()
            modulo_controller.reverse()
            carry_generate_vector, carry_propagate_vector, half_sum_vector, a_prim, b_prim = preprocessingStage.hashed_cells(
                first_number_a, second_number_b, modulo_controller)

            g_prim, p_prim, h_prim = preprocessingStage.envelop_cells(a_prim, b_prim)
            carry_generate_vector, carry_propagate_vector, g_prim, p_prim = parallelPrefixStage.process(
                carry_generate_vector,
                carry_propagate_vector,
                g_prim, p_prim)

            print('a=', first_number_a)
            print('b=', second_number_b)
            print('k=', modulo_controller)
            print('a=', a)
            print('b=', b)
            print('k=', k)
            print()
            print('half sum vector (h) = ', half_sum_vector)
            print('carry propagate vector (p) = ', carry_propagate_vector)
            print('carry generate vector (g) = ', carry_generate_vector)
            print()
            print('half sum from enveloped cells (h`) = ', h_prim)
            print('carry propagate vector from enveloped cells (p`) = ', p_prim)
            print('carry generate vector from enveloped cells (g`) = ', g_prim)

            sum_vector = sumComputationStage.compute_s(half_sum_vector, h_prim, carry_generate_vector, g_prim)
            print()
            print("Wynik:")
            print('sum vector = ', sum_vector)
            # sum_vector.reverse()
            print(binToDec(sum_vector))
            s = (a + b) % (2 ** bit_number - k)

            print("Oczekiwane:")
            print(s)
            print()
            print()


if __name__ == '__main__':
    main()
