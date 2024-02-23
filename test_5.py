def number_of_descendants(name,dictionary):
    if name in dictionary:
        summ = len(dictionary[name])
        for i in dictionary[name]:
            summ += number_of_descendants(i,dictionary)
        return summ
    else:
        return 0


n = int(input())
dictionary = {}

for i in range(n):
    temp_array = list(map(str, input().split(" ")))
    if temp_array[0] in dictionary:
        dictionary[temp_array[0]] = dictionary[temp_array[0]] + [temp_array[1]]
    else:
        dictionary[temp_array[0]] = [temp_array[1]]

name = input()

print(number_of_descendants(name,dictionary))
