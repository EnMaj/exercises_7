n = int(input())
dictionary = {}

for i in range(n):
    temp_array = list(map(str, input().split(" ")))
    dictionary[temp_array[0]] = temp_array[1]

translate = list(map(str, input().split(" ")))
translation = ""

for i in range(len(translate)):
    translation += dictionary.get(translate[i],translate[i]) + " "


print(translation)