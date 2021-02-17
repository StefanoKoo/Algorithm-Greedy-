## Link : https://www.acmicpc.net/problem/1655

import heapq

trial = int(sys.stdin.readline())
##trial = int(input()) : 시간 초과
min_heap, max_heap = [], []

for _ in range(trial):
  num = int(sys.stdin.readline())
  ##num = int(input()) : 시간 초과
    
  if len(min_heap) == len(max_heap):
    heapq.heappush(max_heap,(-num,num))
  else:
    heapq.heappush(min_heap,(num,num))

  if len(min_heap) >= 1 and len(max_heap) >= 1 and max_heap[0][1] > min_heap[0][1]:
    max_value = heapq.heappop(max_heap)[1]
    min_value = heapq.heappop(min_heap)[1]
    heapq.heappush(min_heap,(max_value,max_value))
    heapq.heappush(max_heap,(-min_value,min_value))

  print(max_heap[0][1])
