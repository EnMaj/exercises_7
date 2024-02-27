'''
dictionary.items() возвращает пары (ключ, значение)
key=lambda item: item[1] указывает, что сортировка происходит по значению (второму элементу пары), а не по ключу.
Результатом выполнения этого кода будет список кортежей

key принимает то каким образом функцию нужно сортировать


'''
import operator

word_array = list(map(str, input().split(" ")))
dictionary = {}
for i in range(len(word_array)):
    dictionary[word_array[i]] = word_array.count(word_array[i])

'''
for i in sorted(dictionary.items(), key=lambda item: item[1], reverse=True):
    print(i[0])'''

'''for i in sorted(dictionary.items(),key=operator.itemgetter(1), reverse=True):
    print(i[0])'''








