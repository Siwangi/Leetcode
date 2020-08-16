userInput = int(input("How many integers do you want to enter in an array: "))
count = 1
array = []
try:
    while count <= userInput:
        Input = int(input("Enter the number: "))
        array.append(Input)
        count = count + 1
    target = int(input("Select your target Integer: "))
    num = 0
    for x in range(0, len(array)-1):
        for y in range(x+1, len(array)):
            if array[x] + array[y] == target:
                print("value:", array[x], array[y])
                print("indices: ", x, y)
                num = 1
            break
    if num == 0:
        print("Target not achieved")

except ValueError:
    print("Please enter the number in integer value")
