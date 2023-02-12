
# a + b*x <= c*x
# a <= (c-b)*x
# a/(c-b) <= x
# ( x>0 )  -> c>b  // c != b
# 기본금 + 1개 생산당 추가금 * 생산갯수 ==> a + b*x (a: 기본금, b: 추가금, x: 생산갯수(구하고자하는값))
a, b, c = map(int, input().split())

if b >= c:
    print(-1)
else:
    cnt = a//(c-b)  # 10
    print(cnt+1)
