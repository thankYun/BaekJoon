
import sys

n = int(sys.stdin.readline())
nums = []
for i in range(n):
    nums += [int(sys.stdin.readline())]

nums.sort()
for i in nums:
    print(i)