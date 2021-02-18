## Link : https://www.acmicpc.net/problem/11758
## 벡터 외적 개념을 알면 구현은 어렵지 않음

def ccw(position_list):
  x1, y1 = position_list[0]
  x2, y2 = position_list[1]
  x3, y3 = position_list[2]
  return (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)

position_list = []
for i in range(3):
    position_list.append(list(map(int, input().split())))

result = ccw(position_list)
if result > 0:
    print(1)
elif result < 0:
    print(-1)
else:
    print(0)
