firstNumber = 0
secondNumber = 1
sequence = 20
print(f"{firstNumber}, {secondNumber}", end = " ")
for i in range(2, sequence):
    result = firstNumber + secondNumber
    print(f"{result}", end = " ")
    firstNumber = secondNumber
    secondNumber = result