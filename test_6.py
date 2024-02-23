import sys
sys.setrecursionlimit(3000)

n = int(input())
m = int(input())
dictionary = {}
weight = {}

def dijkstra(now_peak,last_peak,dictionary, weight):
    for i in dictionary[now_peak]:
        if i[0]!=now_peak and i[0] in weight:
            weight[i[0]] = min(weight[i[0]],weight[now_peak]+int(i[1]))
    min_peak = ""
    min_peak_weight = float("inf")
    for i in weight:
        if weight[i]<min_peak_weight and i!=now_peak:
            min_peak = i
            min_peak_weight = weight[i]
    if min_peak == last_peak:
        return weight[min_peak]
    else:
        del weight[now_peak]
        now_peak = min_peak
        return dijkstra(now_peak,last_peak,dictionary,weight)

for i in range(m):
    temp_array = list(map(str, input().split(" ")))
    if temp_array[0] in dictionary:
        dictionary[temp_array[0]] = dictionary[temp_array[0]] + [[temp_array[1]] + [temp_array[2]]]
        if temp_array[1] in dictionary:
            dictionary[temp_array[1]] = dictionary[temp_array[1]] + [[temp_array[0]] + [temp_array[2]]]
        else:
            dictionary[temp_array[1]] = [[temp_array[0]] + [temp_array[2]]]
            weight[temp_array[1]] = float('inf')
    else:
        dictionary[temp_array[0]] = [[temp_array[1]] + [temp_array[2]]]
        dictionary[temp_array[1]] = [[temp_array[0]] + [temp_array[2]]]
        weight[temp_array[0]] = float('inf')
        weight[temp_array[1]] = float('inf')

first_peak, last_peak = map(str, input().split(" "))
weight[first_peak] = 0
print(dijkstra(first_peak,last_peak,dictionary,weight))



