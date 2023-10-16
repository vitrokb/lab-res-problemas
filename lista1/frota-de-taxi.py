values = list(map(float, input().split(" ")))

per_alcohol = round(values[2], 2) / round(values[0], 2)
per_gasoline = round(values[3], 2) / round(values[1], 2)

if per_alcohol > per_gasoline:
    print("A")
else:
    print("G")
