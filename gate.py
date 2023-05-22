def or_gate(first_signal: int, second_signal: int):
    return 1 if first_signal or second_signal else 0


def and_gate(first_signal: int, second_signal: int):
    return 1 if first_signal and second_signal else 0


def xor_gate(first_signal: int, second_signal: int):
    return first_signal ^ second_signal


def buffer(first_signal: int, second_signal: int, enable_signal: int):
    return first_signal if not enable_signal else second_signal


def parallel_prefix_double_node(pi, gi, pi_prev, gi_prev, pi_prim_prev, gi_prim_prev, pi_prim, gi_prim):
    pi_new = and_gate(pi, pi_prev)
    gi_new = or_gate(and_gate(pi, gi_prev), gi)
    pi_prim_new = and_gate(pi_prim_prev, pi_prim)
    gi_prim_new = or_gate(and_gate(pi_prim, gi_prim_prev), gi_prim)
    return pi_new, gi_new, pi_prim_new, gi_prim_new
