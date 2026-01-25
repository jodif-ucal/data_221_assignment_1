def exponential_calculator(x, y):
    return x**y

pairs = [[5, 2], [3, -1], [4, 3], [2, 0]]
exponential_results = []

for number1, number2 in pairs:
    #Skipping over any pair if either number is a negative number
    if number1 < 0 or number2 < 0:
        continue

    #Adding each result of the exponential calculation to the exponential_results list
    exponential_results.append(exponential_calculator(number1, number2))

print(exponential_results)