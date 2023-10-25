coordinates_first_side = list(input().split())
coordinates_second_side = list(input().split())

if "" in coordinates_first_side:
    coordinates_first_side.remove("")

if "" in coordinates_second_side:
    coordinates_second_side.remove("")

first_side_x0 = int(coordinates_first_side[0])
first_side_x1 = int(coordinates_first_side[2])
first_side_y0 = int(coordinates_first_side[1])
first_side_y1 = int(coordinates_first_side[3])

first_side_vector_1 = []
first_side_vector_2 = []

result = 0

for a in range(0, (first_side_x1 - first_side_x0) + 1):
    first_side_vector_1.append(first_side_x0 + a)

for b in range(0, (first_side_y1 - first_side_y0) + 1):
    first_side_vector_2.append(first_side_y0 + b)


second_side_x0 = int(coordinates_second_side[0])
second_side_x1 = int(coordinates_second_side[2])
second_side_y0 = int(coordinates_second_side[1])
second_side_y1 = int(coordinates_second_side[3])

second_side_vector_1 = []
second_side_vector_2 = []

result = 0

for c in range(0, (second_side_x1 - second_side_x0) + 1):
    second_side_vector_1.append(second_side_x0 + c)

for d in range(0, (second_side_y1 - second_side_y0) + 1):
    second_side_vector_2.append(second_side_y0 + d)

for e in first_side_vector_1:
    if e in second_side_vector_1:
        result = 1

for f in first_side_vector_2:
    if f in second_side_vector_2:
        result = 1

print(result)
