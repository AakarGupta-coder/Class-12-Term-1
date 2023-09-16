#(a)
def generate_factors(n):
    factors = []
    for i in range(1, n):
        if n % i == 0:
            factors.append(i)
    return factors
#(b)
def is_prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
#(c)
def is_perfect_number(n):
    factors = generate_factors(n)
    factor_sum = sum(factors)
    return factor_sum == n
# Main program
try:
    num = int(input("Enter a number: "))
    factors = generate_factors(num)
    if is_prime_number(num):
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")
        if is_perfect_number(num):
            print(num, "is a perfect number.")
        else:
            print(num, "is not a perfect number.")
    print("Factors:", factors)
except ValueError:
    print("Invalid input. Please enter a valid number.")
