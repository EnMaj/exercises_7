'''dictionary[temp_array[0]] = temp_array[1:len(temp_array)]'''

n = int(input())
dictionary = {}

for i in range(n):
    temp_array = list(map(str, input().split(" ")))
    for i in range(1,len(temp_array)):
        dictionary[temp_array[i]] = temp_array[0]

subject = input()
print(dictionary.get(subject))
