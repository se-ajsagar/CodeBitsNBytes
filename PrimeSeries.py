import time

def checkPrimeNumber(input):
    isPrime = True
    isPrime = True if input > 1 else False
    for i in range(2, input - 1):
        if input % i == 0:
            isPrime = False
            break
    return isPrime
    
number = 1000000
startTime = time.time()
for i in range(2, number):
    if checkPrimeNumber(i):
        print(f"{i}", end=" ")
endTime = time.time()
executionTime = endTime - startTime
print(f"\nTotal execution time is {executionTime: .2f} seconds")