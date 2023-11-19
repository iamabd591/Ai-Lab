def duplicate(arr):
    array = []
    array2 = set()
    for i in arr:
        if i in array2:
            array.append(i)
        else:
            array2.add(i)
    return array


numbers = []
n = int(input("Enter the numbers of element:"))
for i in range(n):
    ele = int(input())
    numbers.append(ele)

print("Numbers: ", numbers)
newarr = duplicate(numbers)
print("Duplicate Numbers: ", newarr)
