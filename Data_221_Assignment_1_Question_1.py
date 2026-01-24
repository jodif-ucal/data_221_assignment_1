threshold = 100
product = 1
current_number = 1

while product < threshold:
    current_number += 1
    product *= current_number

print(f"Product at the end of the while loop: {product}")
print(f"Integer that caused product to exceed the threshold {threshold}: {current_number}")