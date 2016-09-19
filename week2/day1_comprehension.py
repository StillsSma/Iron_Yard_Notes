
list_of_numbers = [9, 10, 5, 100, 23, 2]

half_values = []

for x in list_of_numbers:
    half_of_x = x / 2
    half_values.append(half_of_x)

print (half_values)

###################

list_of_numbers = [5, 2, 8, 2, 10, 5]

half_values = [number / 2 for number in list_of_numbers]
print (half_values)

# The slow way to create a dictionary from a list

list_of_numbers = [9, 67, 23, 45, 11]

square_numbers = {}

for number in list_of_numbers:
    square_numbers[number] = number ** 2
print (square_numbers)

# Dict comprehension method

list_of_numbers = [9, 67, 23, 45, 11]

square_numbers = {numberxlol: numberxlol ** 2 for numberxlol in list_of_numbers}

print (square_numbers)

######################

# nested comprehensions

matrix = [["_", "X", "_"],
          ["_", "O", "_"],
          ["_", "_", "X"]]

target_column = [row[1] for row in matrix]


print (target_column)
