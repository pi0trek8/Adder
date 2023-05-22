from prepocessingStage import PreprocessingStage
from sumComputationStage import SumComputationStage
import parrarelPrefixStage
import sys


def main():
    # a = [0, 1, 1, 1, 0, 0, 0]
    # b = [0, 1, 1, 1, 0, 1, 1]
    # k = [1, 1, 0, 1, 0, 0, 0]
    a = [int(char) for char in sys.argv[1]]
    b = [int(char) for char in sys.argv[2]]
    k = [int(char) for char in sys.argv[3]]

    preprocessingStage = PreprocessingStage()
    g, p, h, a_prim, b_prim = preprocessingStage.hashed_cells(a, b, k)
    g_prim, p_prim, h_prim = preprocessingStage.envelop_cells(a_prim, b_prim)
    g, p, g_prim, p_prim = parrarelPrefixStage.process(g, p, g_prim, p_prim)

    print('p=', p)
    print('g=', g)

    print('p`=', p_prim)
    print('g`=', g_prim)

    sumComputationStage = SumComputationStage()
    s = sumComputationStage.compute_s(h, h_prim, g, g_prim)
    s.reverse()
    print()
    print(s)


if __name__ == '__main__':
    main()
