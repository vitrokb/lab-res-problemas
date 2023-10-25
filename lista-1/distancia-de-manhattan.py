coordinates = list(map(int, input().split(" ")))

total1 = 0
total2 = 0

if coordinates[2] > coordinates[0]:
    total1 = coordinates[2] - coordinates[0]
else:
    total1 = coordinates[0] - coordinates[2]

if coordinates[3] > coordinates[1]:
    total2 = coordinates[3] - coordinates[1]
else:
    total2 = coordinates[1] - coordinates[3]

total = total1 + total2

print(total)
