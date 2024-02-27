word_array = list(map(str, input().split(" ")))
dictionary = {}
for i in range(len(word_array)):
    dictionary[word_array[i]] = word_array.count(word_array[i])

'''
for i in sorted(dictionary.items(), key=lambda item: item[1], reverse=True):
    print(i[0])'''

now_array = sorted((value, key) for (key, value) in dictionary.items())
now_array.reverse()
for i in now_array:
    print(i[1])





