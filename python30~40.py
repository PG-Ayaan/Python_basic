#30
word = input().split(" ")
print(len(word))

n = input()
le = list(n.strip().split())
l = len(le) - 1
for i in range(l,-1,-1):
    print(le[i], end = " ")

user_input = input()
l = list(user_input.strip().split())
l = [int (i) for i in l]
if l != sorted(l):
    print('NO')
else:
    print('yes')

def one(n):
    def two(value):
        sq = value ** n
        return sq
    return two

a = one(2)
b = one(3)
c = one(4)
print(a(10))
print(b(10))
print(c(10))

n = int(input())
for i in range(1,10):
    print(i*n,end=" ")

l = input().split()
count  = 0
for i in range(len(l)-1):
    if l.count(l[i-1]) < l.count(l[i]):
        count = i
print(count)

user  = list(map(int, input().split()))
if user != sorted(user):
    print("NO")
else:
    print("YES")

a = int(input())
for i in range(1,10):
    print(i*a,end = " ")

data = list(map(str, input().split()))
count = 0
for i in range(len (data)):
    if data.count(data[i-1]) < data.count(data[i]):
        count = i
print(f"{data[count]}(이)가 총 {data.count(data[count])}표로 반장이 되었습니다")

score_list =[97,86,75,66,55,97,85,97,97,95]
count = 0
for i in range(3):
    max_value = max(score_list)
    for j in range(len(score_list)):
        if max_value in score_list:
            count+= 1
            score_list.remove(max_value)
print(count)

a = str(input())
x = a.replace("q","e")
print(x)

#40
count = 0
total = 0
limit_weight = int(input('제한 무게는 몇 인가요?: '))
n = int(input('몇 명에서 탈건가요?: '))
for i in range(n):
    total += int(input('몸무게를 입력해주세요: '))
    if total <= limit_weight:
        count+= 1
print(count)