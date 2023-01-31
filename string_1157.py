# 문자열 한개가 input, input 1<=input <=1,000,000
# 출력 대문자 한개
# 조건 : 대문자와 소문자는 구별하지 않는다.
# 조건2 : 만약에 가장 많이 등장하는 단어가 2개 이상이라면 '?'를 출력한다.

word = input()
word = word.upper() # word.upper()
my_dict = list(set(list(word))) 
cnt = [] 
for e in my_dict:
    cnt.append(word.count(e)) # str.count(string) --> 문자열에서 입력받은 string의 개수 정수값을 반환
if cnt.count(max(cnt)) >= 2: # [1,1,2,3,3] --> 3을 count-- 2
    print('?')
else:
    # cnt = [1,2,3,4], max(cnt) -- 4
    # cnt.index(4) --> cnt안에 존재하는 4라는 요소의 index값을 반환
    print(my_dict[cnt.index(max(cnt))])