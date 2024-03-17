t = int(input('정수를 입력하시오: '))
bt = bin(t)
n_bt = bin(~t)

print(t, "의 2진수 값: " , bt)
print(t, "의 2진수 값에 대한 비트단위 부정값: " , n_bt)
