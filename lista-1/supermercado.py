amount_of_markets = int(input())
list_of_values = []

lower_value = 999999999

for i in range(0, amount_of_markets):
    value_from_input = input().split(" ")
    value = [float(value_from_input[0]), int(value_from_input[1])]
    list_of_values.append(value)

for j in list_of_values:
    value_of_gram = j[0] / j[1]
    value_of_kilo = value_of_gram * 1000

    if value_of_kilo < lower_value:
        lower_value = value_of_kilo

print(format(lower_value, ".2f"))
