import sys
input = lambda: sys.stdin.buffer.readline().decode().rstrip()






def code(TC):
	n, k = list(map(int, input().split()))
	a = list(map(int, input().split()))
	for i in a:
		if i % k == 0: print(i / k, end = " ")







TT = 1
TT = int(input())
for i in range(1, TT + 1, 1):
	code(i)