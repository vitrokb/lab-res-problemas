amount_of_trays = int(input())
trays = []

amount_of_broken_glasses = 0

for i in range(0, amount_of_trays):
    tray = list(map(int, input().split(" ")))
    trays.append(tray)

for j in trays:
    if j[0] > j[1]:
        amount_of_broken_glasses += j[1]

print(amount_of_broken_glasses)
