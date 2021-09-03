
None = False
1 = True
"" = False
0 = False
bool(0) = False

# 변수명으로 사용할 수 없는 것
# as = as는 예약어이므로 사용할 수 없다
# 1age = 변수명은 숫자로 시작할 수 없다.

d = {'height':180,'weight':78,'weight':84,'temparture':36,'eyesight':1}
print(d['weight'])

#12
class Wizard:
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor
 
    def attack(self):
        print('파이어볼')

x = Wizard(health=545, mana=210, armor=10)
print(x.health, x.mana, x.armor)
x.attack()

a = int(input())
for i in range(a, a+1):
    if i == 1:
        print('수성')
    elif i == 2:
        print('금성')
    elif i == 3:
        print('지구')
    elif i == 4:
        print('화성')
    elif i == 5:
        print('목성')
    elif i == 6:
        print('토성')
    elif i == 7:
        print('천왕성')
    else:
        print('해왕성') 

num = int(input())
for i in range(num, num+1):
    if i % 3 == 0:
        print('짝')
    else:
        print(i)

n = input()
print('안녕하세요. 저는 %s입니다.' % n)

s = str(input())
reversed_str = s[::-1]
print(reversed_str)

key = int(input("키가 몇 cm 인가요?: "))
if key == 150:
    print('YES')
else:
    print('NO')

a, b, c  = map(int, input().split())
avg = (a+b+c)/3
print(round((avg)))

x, y = map(int, input().split())
pow = x ** y
print(pow)

n = list(map(int, input().split()))
print(n[0] // n[1],end=" ")
print(n[0] % n[1])

a = str(input())
x = a.upper()
print(x)

def solution(n):
    return n*n*3.14
print(solution(int(input())))

planets = {
	'수성' : 'Mercury',
	'금성' : 'Venus',
	'지구' : 'Earth',
	'화성' : 'Mars',
	'목성' : 'Jupiter',
	'토성' : 'Saturn',
	'천왕성' : 'Uranus',
	'해왕성' : 'Neptune',
}
name = input()
print(planets[name])

key = input().split()
values = map(int, input().split())
result = dict(zip(key, values))
print(result)

word = input()
word_text = zip(word, word[1:])
for i in word_text:
    print(i[0], i[1],sep="")

data = input()
for i in data:
    if  i == data.upper():
        print('YES')
    else:
        print('NO')

string = input()
word = input()
print(string.index(word))



