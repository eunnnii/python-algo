dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
num = list(input())
cnt = 0
for n in num:
    for e in dial:
        if n in e:
            cnt += 3 + dial.index(e)
print(cnt)

#
