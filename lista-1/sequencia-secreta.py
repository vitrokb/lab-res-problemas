amount_of_numbers_in_col = int(input())
list_of_values = []

for i in range(0, amount_of_numbers_in_col):
    value = int(input())
    if value == 1 or value == 2:
        list_of_values.append(value)

counter = 0
last_number = 2

for j in list_of_values:
    if j != last_number:
        counter += 1
        last_number = j

print(counter)
