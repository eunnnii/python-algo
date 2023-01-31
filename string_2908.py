num1, num2 = input().split(' ')

#num1[::-1] --> 문자열 거꾸로 출력
num1 = int(num1[::-1])
num2 = int(num2[::-1])

print(max([num1,num2]))