initial_values = list(map(int, input().split(" ")))
play_list = []

players = {
    "D": initial_values[0],
    "E": initial_values[0],
    "F": initial_values[0],
}

for i in range(0, initial_values[1]):
    play = list(input().split(" "))
    play_list.append(play)

for j in play_list:
    if j[0] == "C":
        players[j[1]] = players[j[1]] - int(j[2])
    elif j[0] == "V":
        players[j[1]] = players[j[1]] + int(j[2])
    else:
        players[j[1]] = players[j[1]] + int(j[3])
        players[j[2]] = players[j[2]] - int(j[3])

print(f"{players['D']} {players['E']} {players['F']}")
