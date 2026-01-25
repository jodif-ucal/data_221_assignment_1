from random import random

values = [random() for i in range(20)] #Create 20 random numbers and put them in the list
x = random()

sorted_values = sorted(values)

list_of_indices_from_values_list = []
for index in range(len(sorted_values)):
    if values[index] >= x:
        list_of_indices_from_values_list.append(index)

print(f"Sorted list: {sorted_values}")
print(f"Value of x: {x}")
if len(list_of_indices_from_values_list) > 0:
    print(f"First matching index from values: {list_of_indices_from_values_list[0]}")
else:
    print("No matching index exists")