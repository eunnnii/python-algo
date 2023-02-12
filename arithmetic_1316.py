# a a a // b b b b a 값이 변경되는순간(//로 표시된곳) 뒤에 이전값이 또 등장하는지 확인한다. 또 등장한다면 전체 갯수 - 1하는 식으로 그룹단어갯수를 계산한다.
# a , b , --> pass .... stack

n = int(input())
cnt = n
for i in range(n):
    word = (input())
    for j in range(len(word)-1):  # 0,1////len-1
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            cnt -= 1
            break
print(cnt)
