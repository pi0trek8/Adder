from prepocessingStage import PreprocessingStage
from sumComputationStage import SumComputationStage
import parrarelPrefixStage


if __name__ == '__main__':
    a = [0, 0, 1, 1, 0, 0, 1]
    b = [0, 1, 0, 0, 0, 0, 1]
    k = [1, 0, 0, 1, 0, 0, 0]

    preprocessingStage = PreprocessingStage()
    g, p, h, a_prim, b_prim = preprocessingStage.hashed_cells(a, b, k)

    g_prim, p_prim, h_prim = preprocessingStage.envelop_cells(a_prim, b_prim)

    # print(a)
    # print(b)
    # print(k)
    # print()
    # print(g)
    # print(p)
    # print(h)
    # print()
    # print(g_prim)
    # print(p_prim)
    # print(h_prim)
    g, p, g_prim, p_prim = parrarelPrefixStage.process(g, p, g_prim, p_prim)

    # h = [1, 0, 0, 1, 0, 1, 0]
    # h_prim = [0, 0, 0, 0, 1, 1, 0]
    # c = [0, 0, 0, 0, 0, 0, 1]
    # c_prim = [0, 1, 0, 0, 0, 0, 0]

    sumComputationStage = SumComputationStage()
    s = sumComputationStage.compute_s(h, h_prim, g, g_prim)
    print()
    print(s)
