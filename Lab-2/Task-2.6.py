def bubble_sort(list):
    for i in range(0, len(list)):
        for j in range(1, len(list)-i):
            if list[j-1] > list[j]:
                temp = list[j-1]
                list[j-1] = list[j]
                list[j] = temp
    return list


def reverse_list(list):
    list_length = len(list)

    for i in range(list_length // 2):
        list[i], list[list_length - 1 - i] = list[list_length - 1 - i], list[i]

    return list


lista = [5, 6, 7]
listb = [1, 2, 3]
listc = []
listc = lista + listb

print("List A:", lista)
print("List B:", listb)
print("List C:", listc)

listd = bubble_sort(listc)
print("List D:", listd)

revers = reverse_list(listd)
print("Reverse List:", revers)

listc[3] = 42
print("Updated List C:", listc)
listd.append(10)
print("Append 10 in List D:", listd)

listc.append(7)
listc.append(8)
listc.append(9)
print("Append 7,8,9 in List C:", listc)
print("First Three Elements of List C:", listc[:3])
print("Last Elements of List D:", listd[-1])
print("Lenght List D:", len(listd))
