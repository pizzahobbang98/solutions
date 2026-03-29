import sys
input = sys.stdin.readline

n, m = map(int, input().split())
times = list(map(int, input().split()))

start = max(times)
end = sum(times)

while start <= end:
    mid = (start + end) // 2

    tmp = 0
    cnt = 0
    for t in times:
        if tmp + t > mid:
            cnt += 1
            tmp = 0
        tmp += t

    if tmp != 0:
        cnt += 1

    if cnt > m:
        start = mid + 1
    else:
        end = mid - 1

print(start)