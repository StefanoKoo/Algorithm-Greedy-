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

