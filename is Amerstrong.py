number = input("Enter the number: ")
sum = 0
for num in number:
    sum += int(num) ** len(number)
if sum == int(number):
    print("yes")
else:
    print("no")