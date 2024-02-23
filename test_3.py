n = int(input())
dictionary = {}

for i in range(n):
    temp_array = list(map(str, input().split(" ")))
    dictionary[temp_array[0]] = temp_array[1]

antonym_search = input()
print(dictionary.get(antonym_search,antonym_search))
