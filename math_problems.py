# yeah screw that old one
import random
import time
print("\n")

OPERATORS = ["+", "-", "*"]
MIN_RAND_NUM = 2
MAX_RANDOM_NUM = 12
TOTAL_OPERATIONS = int(input("How many questions do you want to do? "))

def generateMathProblem():
    leftNum = random.randint(MIN_RAND_NUM, MAX_RANDOM_NUM)
    rightNum = random.randint(MIN_RAND_NUM, MAX_RANDOM_NUM)
    if leftNum < rightNum:
        generateMathProblem()
    operator = random.choice(OPERATORS)
    expression = (str(leftNum)+ operator + str(rightNum))
    answer = eval(expression)
    return expression, answer

input("Press enter to start." )
print("---------------------------------")
startTime = time.time()

for i in range(TOTAL_OPERATIONS):
    expression, answer = generateMathProblem()
    while True:
        userInput = input(f'Question {str(i + 1)}: {expression} = ')
        if userInput == str(answer):
            break

endTime = time.time()
totalTime = round(endTime - startTime, 1)
print("---------------------------------")
print(f'Total time taken: {totalTime} seconds')