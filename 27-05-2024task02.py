def squaresum(n):
    sm = 0
    for i in range(1, n + 1):
        sm += i * i
    return sm

n = 10
print(f"Sum of squares of first {n} natural numbers is {squaresum(n)}")