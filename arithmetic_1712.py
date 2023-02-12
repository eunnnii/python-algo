

a, b, c = map(int, input().split())
# a + b*x <= c*x
# a <= (c-b)*x
# a//(c-b) <= x

if b >= c:
    print(-1)
else:
    cnt = a//(c-b)
    print(cnt+1)
