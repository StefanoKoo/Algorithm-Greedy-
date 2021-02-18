## Link : https://www.acmicpc.net/problem/1956

num_city, num_road = map(int,input().split())

cost_city = [[100001 for _ in range(num_city+1)] for _ in range(num_city+1)]

for _ in range(num_road):
  start, end, cost = map(int,input().split())
  cost_city[start][end] = cost

for j in range(len(cost_city)):
  for i in range(len(cost_city)):
    for k in range(len(cost_city)):
      cost_city[i][k] = min(cost_city[i][k],cost_city[i][j] + cost_city[j][k])

min_value = 100001
for i in range(1,num_city+1):
  min_value = min(min_value,cost_city[i][i])
    
if min_value == 100001:
  print(-1)
else:
  print(min_value)
