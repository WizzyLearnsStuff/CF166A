import sys

l = sys.stdin

n, k = list(map(int, l.readline().strip().split()))

class Pair(tuple):
    def __lt__(s, o):
        return o[0] > s[0] or (o[0] == s[0] and o[1] < s[1])

place = [Pair(map(int, l.readline().strip().split())) for _ in range(n)]

place.sort(reverse=True)

rank = 1
obj = 0
count = 0
for idx, i in enumerate(place):
    if obj == i:
        count += 1
    else:
        if k >= rank and k < (rank + count):
            print(count)
            raise SystemExit
        rank = idx + 1
        count = 1
        obj = i

print(count)
