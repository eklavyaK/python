import sys




def code(TC):
	n = int(input())
	a = list(map(int, input().split()))
	dic = {}
	for i in range(n):
		if a[i] not in dic:
			dic[a[i]] = 1;
	print(len(dic))




TT = 1
for TC in range(1, TT + 1, 1):
	code(TC)