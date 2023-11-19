numbers = []
n = int(input("Enter the numbers of element:"))
for i in range(n):
    ele = int(input())
    numbers.append(ele)


def sum(arr):
    s = 0
    for i in range(n):
        s += arr[i]
    return s


def mean_of_list(arr):
    s = sum(arr)
    mean = s/n
    return mean


def meadian_of_list(arr):
    m = {(n+1)/2}
    return m


print("List: " + str(numbers))
NumberSum = sum(numbers)
print("Sum of list is: " + str(NumberSum))

m = mean_of_list(numbers)
print("Mean of list: " + str(m))

median = meadian_of_list(numbers)
print("Median of list: " + str(median))
