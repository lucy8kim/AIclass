n = int(input("숫자를 입력하세요: "))

s = 0

for i in range(0, n):
    s = s + ((i+1)**2)
print("결과는" , s,"입니다.")
