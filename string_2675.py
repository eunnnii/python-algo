# 1<=N<=1000
N = int(input())
    
for i in range(N):
    repeat, my_str = input().split(' ')
    # repat -- 2, my_str -- "ABC"
    # my_str -- 요소 하나를 repeat만큼 찍어
    result = [a*int(repeat) for a in my_str]
    print(''.join(result))