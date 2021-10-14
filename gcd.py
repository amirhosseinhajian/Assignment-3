a = int(input("Enter the first number: "))
b = int(input("Enter the seccond number: "))
gcd = 1
if a > b:
    temp = b
else:
    temp = a
for i in range(temp, 1, -1):
    if ((a % i == 0) and (b % i == 0)):
        gcd = i
        break

print(f"GCD({a},{b}) is: {gcd}")
