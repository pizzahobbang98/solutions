import sys
input = sys.stdin.readline

n, c = map(int, input().split())
houses = [int(input()) for _ in range(n)] 

houses.sort()

start, end = 1, houses[-1] - houses[0]
max_len = 0

while start <= end:
    mid = (start + end) // 2
    now = houses[0]
    count = 1

    for i in range(n):
        if houses[i] >= now + mid: 
            count += 1
            now = houses[i]
    
    if count >= c:
        max_len = max(max_len, mid)
        start = mid + 1
    else:
        end = mid -1

print(max_len)