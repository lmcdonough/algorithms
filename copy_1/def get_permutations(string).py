def get_permutations(string):

    if len(string) <= 1:
        return [string]

    all_chars_except_last = string[:-1]
    last_char = string[-1]
    permutations_of_all_chars_except_last = get_permutations(all_chars_except_last)
    possible_positions_to_put_last_char = range(len(all_chars_except_last) + 1)
    permutations = set()

    for permutation_of_all_chars_except_last in permutations_of_all_chars_except_last:
        for position in possible_positions_to_put_last_char:
            permutation = permutation_of_all_chars_except_last[:position] + last_char + permutation_of_all_chars_except_last[position:]
            print(permutation)
            permutations.add(permutation)

    return permutations


def get_permutationsII(string):

    if len(string) <= 1:
        return [string]

    all_chars_except_last = string[:-1]
    last_char = string[-1]
    permutations_of_all_chars_except_last = get_permutations(all_chars_except_last)
    possible_positions_to_put_last_char = range(len(all_chars_except_last + 1))
    permutations = set()

    for permutation_of_all_chars_except_last in permutations_of_all_chars_except_last:
        for position in possible_positions_to_put_last_char:
            permutation = permutation_of_all_chars_except_last[:position] + last_char + permutation_of_all_chars_except_last[position:]
            print(permutation)
            permutations.add(permutation)

    return permutations
