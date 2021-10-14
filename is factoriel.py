number = int(input("Enter the number: "))
i = 2
buff = 1
while True:
    if buff < number:
        buff = buff * i
        i += 1
    elif buff > number:
        print("no")
        break
    elif buff == number:
        print("yes")
        break