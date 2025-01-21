import random

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

random_numbers = [random.randint(100, 900) for _ in range(100)]

odd_numbers = [num for num in random_numbers if num % 2 != 0]
print(f"Odd numbers ({len(odd_numbers)}): {odd_numbers}")

even_numbers = [num for num in random_numbers if num % 2 == 0]
print(f"Even numbers ({len(even_numbers)}): {even_numbers}")

prime_numbers = [num for num in random_numbers if is_prime(num)]
print(f"Prime numbers ({len(prime_numbers)}): {prime_numbers}")