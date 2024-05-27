def fibonacci(n):
    fib1 = [0,1]
    for i in range(2,n):
        fib2 = fib1[-1] + fib1[-2]
        fib1.append(fib2)
    return fib1[:n]
n=10
print(fibonacci(n))

factorial using function
# def factorial(x):
#     if x==0:
#         return 1
#     else:
#         return(x*factorial(x-1))
# x=int(input("enter a value"))
# print(factorial(x))