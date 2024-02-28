def generate_primes_grid(width, height, start):
    primes = []
    num = max(start, 2)

    while len(primes) < width * height:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 1

    result = ""
    for i in range(height):
        for j in range(width):
            result += str(primes[i * width + j]) + " "
        result = result.rstrip() + "\n"

    return result
if __name__ == "__main__":
    print(generate_primes_grid(2, 3, 13))
    """
    17 19
    23 29
    31 37
    """
    print(generate_primes_grid(5, 2, 1))
    """
    2  3  5  7 11
    13 17 19 23 29
    """