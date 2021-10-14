array = input("Enter the Array with space between each number and dont enter [ or ]: ").split(" ")
flag = True
for i in range(len(array)):
    if flag == False:
        break
    for j in range(i+1, len(array)):
        if array[i] > array[j]:
            flag = False
            break

if flag == True:
    print("The input array is sorted.")
else:
    print("The input array is not sorted.")
