num = int(input("Enter a pstive number: "))
if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    # Check for factors
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")