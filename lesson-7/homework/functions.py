# 1
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
print(is_prime(11))

# 2
def digit_sum(k):
    k = int(input("Please enter the number: "))
    h = list(str(k))
    total = 0
    for i in h:
        total += int(i)
    return total

# 3
def two_power(n):
    k = 1
    while k <= n:
        print(k, end=' ')
        k *= 2





