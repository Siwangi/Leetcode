"""Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice."""


userInput = int(input("How many integers do you want to enter in an array: "))
count = 1
array = []
try:
    while count <= userInput:
        Input = int(input("Enter the number: "))
        array.append(Input)
        print(array)
        count = count + 1

    for x in range(len(array)):
        for y in range(len(array)-1):
            if array[y] < array[y+1]:
                continue
            elif array[y] > array[y+1]:
                array[y], array[y+1] = array[y+1], array[y]
    print("sorted array: ", array)

    target = int(input("Select your target Integer: "))
    count = 0
    start = 0
    end = len(array)-1
    while start <= end:
        mid = int((start + end)/2)
        print("mid point:", mid)
        print("mid point value: ", array[mid])
        if target == array[mid]:
            count = 1
            print("target found: ", array[mid])
            break

        elif target < array[mid]:
            end = mid-1
            print("left new array mid point: ", mid)
            print("left array mid value: ", array[mid])

        elif target > array[mid]:
            start = mid + 1
            print("Right new array mid point: ", mid)
            print("Right array mid value: ", array[mid])

    if count == 0:
        print("target not found")


    num = 0
    for x in range(0, len(array)-1):
        for y in range(1, len(array)-1):
            if array[x] + array[y] == target:
                print("value:", array[x], array[y])
                print("indices: ", x, y)
                num = 1
        break
    if num == 0:
        print("Target not achieved")

except ValueError:
    print("Please enter the number in integer value")











