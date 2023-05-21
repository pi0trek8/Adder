def or_gate(first_signal: int, second_signal: int):
    return 1 if first_signal or second_signal else 0


def and_gate(first_signal: int, second_signal: int):
    return 1 if first_signal and second_signal else 0

def xor_gate(first_signal: int, second_signal: int):
    return first_signal ^ second_signal