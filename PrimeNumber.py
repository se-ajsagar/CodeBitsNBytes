isPrime = True
input = 7
isPrime = True if input > 1 else False
for i in range(2, input - 1):
    if input % i == 0:
        isPrime = False
        break
        
print(f"{input} is Prime: {isPrime}")