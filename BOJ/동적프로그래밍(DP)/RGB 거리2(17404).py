# Link : https://www.acmicpc.net/problem/17404

n = int(input())
m = []
for _ in range(n):
  m.append([int(i) for i in input().split()])
 
ret = 100001
 
for x in range(3): 
  dp = [[0 for _ in range(3)] for _ in range(n)]
 
  for i in range(3): 
    if i == x:
      dp[0][i] = m[0][i]
      continue
    dp[0][i] = 100001
 
  for i in range(1,n): 
    dp[i][0] = m[i][0]+min(dp[i-1][1],dp[i-1][2])
    dp[i][1] = m[i][1]+min(dp[i-1][0],dp[i-1][2])
    dp[i][2] = m[i][2]+min(dp[i-1][0],dp[i-1][1])

  print(dp)  
  for i in range(3): 
    if i == x:
        continue
    ret = min(ret, dp[-1][i])
print(ret)
