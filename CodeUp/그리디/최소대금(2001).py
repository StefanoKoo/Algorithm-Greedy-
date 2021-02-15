## Link : https://codeup.kr/problem.php?id=2001

pasta_list = []
juice_list = []

for _ in range(3):
  pasta_list.append(int(input()))

for _ in range(2):
  juice_list.append(int(input()))

pasta_list.sort()
juice_list.sort()

## 소수점 1자리 수 출력 시 format 사용이 항상 합리적인가?
print(format((pasta_list[0]+juice_list[0])*1.1,".1f"))
