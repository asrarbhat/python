def is_prime(positive_integer):

    if not isinstance(positive_integer, int) or positive_integer < 2:
        return False
    if positive_integer == 2:
        return True
    elif positive_integer % 2 == 0:
        return False

    largest_potential_factor = int(positive_integer**0.5)
    potential_factors = (int(x)
                         for x in range(3, largest_potential_factor+1, 2))

    for factor in potential_factors:
        if positive_integer % factor == 0:
            return False

    return True


print(is_prime(9973))
