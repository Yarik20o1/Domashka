import random
import json

matrix = [[random.randint(1, 10), random.randint(10, 20), random.randint(20, 30)] for i in range(3)]
with open('matrix.json', 'w') as f:
    json.dump(matrix, f)
with open('matrix.json', 'r') as f1:
    data = json.load(f1)
count = 0
for i in data:
    for j in i:
        if count % 2 == 0:
            i[i.index(j)] = 0
        count += 1
print(data)
with open('matrix1.txt', 'w') as f:
    json.dump(data, f)
