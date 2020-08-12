이것이 취업을 위한 코딩 테스트다 with 파이썬
===================================
# 1. 큰 수의 법칙
## 1-1. 내 코드
``` python
# N, M, K 입력 받기
N,M,K = map(int, input().split())

# 제일 큰 수, 2번째로 큰 수를 찾기 위해 배열을 선언
data = list(map(int, input().split()))

# 해당 배열을 정렬
data.sort()

# 제일 큰 수 = 배열 제일 뒤에 있는 수
num_first = data[N-1]
# 2번째로 큰 수 = 배열 제일 뒤에서 바로 앞에 있는 수
num_second = data[N-2]

# 총합
result = 0

# 제일 큰 수는 최대 'K' 만큼만 더할 수 있다
while True:
  for i in range(K):
    if M == 0:
      break
    result += num_first
    M -= 1
  if M == 0:
    break
  result += num_second
  M -= 1

print(result)
```
# 2. 숫자 카드 게임
## 2-1. 내 코드
```python
N, M = map(int, input().split())

result = 0

for _ in range(N):
  arr = list(map(int, input().split()))
  min_val = min(arr)
  result = max(result, min_val)

print(result)
```
# 3. 1이 될 때까지
## 3-1. 내 코드
```python
N, K = map(int,input().split())

result = 0

while N != 1:
  if N%K == 0:
    # int 로 캐스팅 하는 습관이 필요
    N = (int)N/K
    result += 1
  else:
    N -= 1
    result += 1

print(result)
```

# 4. 구현
## 4-1. 왕실의 나이트
```python
input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [
  (-2, -1), (-2, 1), (-1, -2), (-1, 2),
  (1, -2), (1, 2), (2, -1), (2, 1)
]

result = 0

for step in steps:
  next_row = row + step[0]
  next_col = col + step[1]

  if next_row >=1 and next_col <= 8 and next_row <= 8 and next_col >= 1:
    result += 1

print(result)
```
## 4-2. 게임 개발
```python
n, m = map(int, input().split())

# list comprehension(page 425)
visit_map = [[0] * m for _ in range(n)]

x, y, d = map(int, input().split())
visit_map[x][y] = 1

input_map = []
for i in range(n):
  input_map.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
  global d
  d -= 1
  if d == -1:
    d = 3

count = 1
turn_count = 0

while True:
  turn_left()
  nx = x + dx[d]
  ny = y + dy[d]

  if visit_map[nx][ny] == 0 and input_map[nx][ny] == 0:
    visit_map[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    turn_count = 0
    continue
  else:
    turn_count += 1
  
  if turn_count == 4:
    nx = x - dx[d]
    ny = y - dy[d]
    if input_map[nx][ny] == 0:
      x = nx
      y = ny
    else:
      break
    turn_count = 0

print(count)
```
# 7. 이진탐색
## 7-1. 부품 찾기
```python
def binary_search(array, start, end, target):
  if start > end:
    return None
  
  mid = (start + end) // 2

  if array[mid] == target:
    return mid
  elif array[mid] > target:
    return binary_search(array, start, mid-1, target)
  else:
    return binary_search(array, mid+1, end, target)


product_num = int(input())
product_arr = list(map(int, input().split()))

search_num = int(input())
search_list = list(map(int, input().split()))

product_arr.sort()

for i in search_list:
  result = binary_search(product_arr,0,product_num-1,i)
  if result != None:
    print('yes',end = ' ')
  else:
    print('no', end = ' ')
```

## 8. 다이나믹 프로그래밍
## 8-1. '1'로 만들기
```pyhton
x = int(input())

d = [0]*30001

for i in range(2,x+1):
  d[i] = d[i-1] + 1

  if i % 2 == 0:
    d[i] = min(d[i], d[i //2] + 1)
  
  if i % 3 == 0:
    d[i] = min(d[i], d[i // 3] +1)

  if i % 5 == 0:
    d[i] = min(d[i], d[i // 5] + 1)

print(d[x])
```
## 8-2. 개미전사
```python
n = int(input())
arr = list(map(int, input().split()))

d = [0]*100

d[0] = arr[0]
d[1] = max(arr[0],arr[1])

for i in range(2,n):
  d[i] = max(d[i-1],d[i-2] + arr[i])

print(d[n-1])
```
## 8-3. 바닥공사
```pyhton
n = int(input())

d = [0]*1000

d[1] = 1
d[2] = 3

for i in range(3,n+1):
  d[i] = (d[i-1] + 2 * d[i-2]) % 796796
  
print(d[n])
```
