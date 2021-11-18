C_1 = (35, 78,21,37, 2,98, 6, 100, 231)
C_2 = (45, 21,124,76,5,23,91,234)
if sum(C_1) > sum(C_2):
    print(f'Сумма больше в кортеже - C_1')
else:
    print(f'Сумма больше в кортеже - C_2')
print(C_1.index(max(C_1)),C_1.index(min(C_1)))
print(C_2.index(max(C_2)),C_2.index(min(C_2)))