initial_values = list(map(int, input().split(" ")))
initial_vector = list(map(int, input().split(" ")))

counter = 0

for i in range(0, len(initial_vector)):
    for j in initial_vector:
        if initial_vector[0] == j:
            continue
        summation = initial_vector[0] + j
        if summation >= initial_values[1] and summation <= initial_values[2]:
            counter += 1
    del initial_vector[0]

print(counter)
