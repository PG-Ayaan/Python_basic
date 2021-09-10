count = 0
total = 0
limit_weight = int(input('제한 무게는 몇 인가요?: '))
n  = int(input('몇명이 탈 수 있나요?: '))
for i in range(n):
    total += int(input('몸무게를 입력해주세요: '))
    if total <= limit_weight:
        count += 1
print(count,"명이 탈 수 있습니다. ")

def number(x):
    for i in range(2, x):
        if x % i == 0:
            return "No"
    return "Yes"
print(number(4))

import datetime
m = int(input())
d = int(input())
def findDay(a,b):
    day = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
    return day[datetime.date(2020,a,b).weekday()]
print(findDay(m,d))

n = list(map(int, input()))
sum = 0
for i in n:
    sum+= i
print(sum)

import time
tm = time.gmtime()
print(tm.tm_year)

a = input()
b = []
for i in a:
    if i.islower():
        b.append(i.upper())
    else:
        b.append(i.lower())
for i in b:
    print(i, end = "")

people = [
         ('이호준', '01050442903'),
         ('이호상', '01051442904'),
         ('이준호', '01050342904'),
         ('이호준', '01050442903'),
         ('이준', '01050412904'),
         ('이호', '01050443904'),
         ('이호준', '01050442903'),
         ]
print(len(set(people)))

a = input()
b = []
for i in a:
    if i.islower():
        b.append(i.upper())
    else:
        b.append(i.lower())
for i in b:
    print(i, end= "")

num = list(map(int, input().split()))
print(max(num))

num = list(map(int, input().split()))
print(sorted(num)[-1])

def bubble(n, data):
	for i in range(n-1):
		for j in range(n-i-1):
			if data[j] > data[j+1]:
				data[j], data[j+1] = data[j+1], data[j]
	for i in range(n):
		print(data[i], end = " ")

n = int(input())
data = list(map(int, input().split()))

bubble(n, data)