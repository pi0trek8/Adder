from prepocessingStage import PreprocessingStage

if __name__ == '__main__':
    a = [0, 0, 1, 1, 0, 0, 1]
    b = [1, 1, 0, 0, 0, 0, 0]
    k = [1, 0, 0, 1, 0, 0, 0]

    preprocessingStage = PreprocessingStage()
    g, p, h, a_prim, b_prim = preprocessingStage.hashed_cells(a, b, k)

    g_prim, p_prim, h_prim = preprocessingStage.envelop_cells(a_prim, b_prim)

    print(a)
    print(b)
    print(k)

    print(g)
    print(p)
    print(h)

    print(g_prim)
    print(p_prim)
    print(h_prim)
