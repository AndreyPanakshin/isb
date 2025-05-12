import math

from scipy.special import gammainc

from const import *


def freq_bit_test(sequence: str) -> float:
    """
    Performs a frequency bit test
    :param sequence: The bit sequence
    :return: P-value
    """

    n = len(sequence)

    if n == 0:
        raise ValueError("Sequence is empty")

    s = sum([1 if bit == "1" else -1 for bit in sequence])

    p_value = math.erfc((abs(s) / math.sqrt(n)) / math.sqrt(2))

    return p_value


def consecutive_bit_test(sequence: str) -> float:
    """
    Performs a test for identical consecutive bits.
    :param sequence: The sequence
    :return: P-value
    """

    p_value = 0

    n = len(sequence)

    p = sequence.count('1') / n

    if abs(p - 0.5) >= 2 / math.sqrt(n):
        return p_value

    v_n = 0

    for i in range(n - 1):

        if sequence[i] != sequence[i + 1]:
            v_n += 1

    numerator = abs(v_n - 2 * n * p * (1 - p))
    denominator = 2 * math.sqrt(2 * n) * p * (1 - p)

    return math.erfc(numerator / denominator)


def sequence_unit_test(sequence: str) -> float:
    """
    Performs a test for the longest sequence of ones in a block.
    :param sequence: The sequence
    :return: P-value
    """

    n = len(sequence)

    if n < 128:
        raise ValueError("Minimum 128 bits")

    N = n // 8

    v = [0, 0, 0, 0]

    for i in range(N):

        block = sequence[i * 8 : (i + 1) * 8]

        max_run = 0
        current_run = 0

        for bit in block:

            if bit == '1':
                current_run += 1

                if current_run > max_run:
                    max_run = current_run

            else:
                current_run = 0

        match max_run:

            case 0 | 1:
                v[0] += 1

            case 2:
                v[1] += 1

            case 3:
                v[2] += 1

            case _:
                v[3] += 1

    x_2 = 0.0

    for i in range(len(v)):
        x_2 += (v[i] - 16 * PI[i]) ** 2 / (16 * PI[i])

    p_value = gammainc(3 / 2, x_2 / 2)

    return p_value


def main():

    cpp_sequence = read_file(cpp_subs)
    java_sequence = read_file(java_subs)

    p_val_freq_bits_cpp = freq_bit_test(cpp_sequence)
    p_val_ident_bits_cpp = consecutive_bit_test(cpp_sequence)
    p_val_longest_bits_block_cpp = sequence_unit_test(cpp_sequence)

    result_cpp_test = (f"CPP sequence: {cpp_sequence}\n\n"
                      f"Frequency bit test: {p_val_freq_bits_cpp}\n"
                      f"Test for identical consecutive bits: {p_val_ident_bits_cpp}\n"
                      f"Test for the longest sequence of ones in a block: "
                      f"{p_val_longest_bits_block_cpp}")

    write_file(test_result_cpp, result_cpp_test)

    p_val_freq_bits_java = freq_bit_test(java_sequence)
    p_val_ident_bits_java = consecutive_bit_test(java_sequence)
    p_val_longest_bits_block_java = sequence_unit_test(java_sequence)

    result_java_test = (f"Java sequence: {java_sequence}\n\n"
                      f"Frequency bit test: {p_val_freq_bits_java}\n"
                      f"Test for identical consecutive bits: {p_val_ident_bits_java}\n"
                      f"Test for the longest sequence of ones in a block: "
                      f"{p_val_longest_bits_block_java}")

    write_file(test_result_java, result_java_test)


if __name__ == "__main__":
    main()