a = int(input("Enter the first number: "))
b = int(input("Enter the seccond number: "))
lcm = a * b
if a < b:
    temp = b
else:
    temp = a
for i in range(temp, a*b, temp):
    if ((i % a == 0) and (i % b == 0)):
        lcm = i
        break

print(f"LCM({a},{b}) is: {lcm}")
