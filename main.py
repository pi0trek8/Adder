import preprocessingStage
import sumComputationStage
import parrarelPrefixStage
import sys


def resolve_difference_in_length(first_nuber: list, second_number: list):
    if len(first_nuber) > len(second_number):
        difference = len(first_nuber) - len(second_number)
        for i in range(difference):
            second_number.append(0)
        return first_nuber, second_number
    difference = len(second_number) - len(first_nuber)
    for i in range(difference):
        first_nuber.append(0)
    return first_nuber, second_number


def main():
    first_number_a = [1, 1, 1, 1, 1, 1, 1]
    second_number_b = [0, 0, 0, 0, 0, 0, 0]
    modulo_controller = [0, 0, 1, 0, 1, 0, 0]
    # if sys.argv[1] == 'dec':
    #     first_number_a = [int(char) for char in bin(int(sys.argv[2]))[2:]]
    #     second_number_b = [int(char) for char in bin(int(sys.argv[3]))[2:]]
    #     modulo_controller = [int(char) for char in bin(int(sys.argv[4]))[2:]]
    # else:
    #     first_number_a = [int(char) for char in sys.argv[1]]
    #     second_number_b = [int(char) for char in sys.argv[2]]
    #     modulo_controller = [int(char) for char in sys.argv[3]]
    #
    # first_number_a.reverse()
    # second_number_b.reverse()
    # modulo_controller.reverse()
    # if len(first_number_a) != len(second_number_b):
    #     first_number_a, second_number_b = resolve_difference_in_length(first_number_a, second_number_b)

    carry_generate_vector, carry_propagate_vector, half_sum_vector, a_prim, b_prim = preprocessingStage.hashed_cells(
        first_number_a, second_number_b, modulo_controller)

    g_prim, p_prim, h_prim = preprocessingStage.envelop_cells(a_prim, b_prim)
    carry_generate_vector, carry_propagate_vector, g_prim, p_prim = parrarelPrefixStage.process(carry_generate_vector,
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


if __name__ == '__main__':
    main()
