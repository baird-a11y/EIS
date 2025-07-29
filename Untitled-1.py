def sieve_of_eratosthenes(limit):
    # Generate a list of prime numbers up to the given limit using the Sieve of Eratosthenes algorithm.
    primes = []
    is_prime = [True] * (limit + 1)
    for p in range(2, limit + 1):
        if is_prime[p]:
            primes.append(p)
            for multiple in range(p * p, limit + 1, p):
                is_prime[multiple] = False
    return primes

def main():
    limit = 100  # Example limit
    primes = sieve_of_eratosthenes(limit)
    print(f"Prime numbers up to {limit}: {primes}")

if __name__ == "__main__":
    main()
