import time

number = 1000000
startTime = time.time()
series = [True] * (number + 1)
series[0] = False
series[1] = False
for i in range(2, number):
    current = i + i
    while (current <= number):
        series[current] = False
        current = current + i

endTime = time.time()
executionTime = endTime - startTime        
print(*[i for i, v in enumerate(series) if v], sep=' ')
print(f"\nTotal execution time is {executionTime: .2f} seconds")