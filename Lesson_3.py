# 1-5
s = input()
print(s[2], s[-2], s[0:5], s[:-2:], s[::2])
# 6
n = int(input("Введите первое число:"))
c = int(input("Введите второе число:"))
print(n, "плюс", c, "равно", n + c)
# 7
q = "привет друг"
print("!", q[7:11], q[0:6], "!")
# 8
n = input()
if len(n) % 3 == 0:
    print(n, "!")
# 9
firstname = input()
lastname = input()
age = input()
print("Привет,меня зовут", lastname, firstname, ",мне", age)
