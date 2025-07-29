import time
from typing import Dict

def fibonacci_recursive(n: int) -> int:
	if n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
	
def fibonacci_iterative(n: int) -> int:
	if n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		result_1: int = 0
		result_2: int = 1
		puffer: int = 0
		for i in range(n - 1):
			result_1 = result_1 + result_2
			puffer = result_2
			result_2 = result_1
			result_1 = puffer
		return result_1

def fibonacci_memoized(n: int, memo: Dict[int, int] = None) -> int:
    # Implementieren Sie mit Memoization
	if memo is None:
		memo = {}
	if n in memo:
		return memo[n]
	if n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
	return memo[n]

n = 10
print(f"Fibonacci of {n} is {fibonacci_recursive(n)}")
print(f"Fibonacci of {n} is {fibonacci_iterative(n)}")
print(f"Fibonacci of {n} is {fibonacci_memoized(n)}")


