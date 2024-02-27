word_array = list(map(str, input().split(" ")))
dictionary = {}
for i in range(len(word_array)):
    dictionary[word_array[i]] = word_array.count(word_array[i])

'''
for i in sorted(dictionary.items(), key=lambda item: item[1], reverse=True):
    print(i[0])'''

sort_dict = sorted((value, key) for (key, value) in dictionary.items())
sort_dict.reverse()
for i in sort_dict:
    print(i[1])





