n = int(input('정수를 입력하세요: '))
is_even_number = ((n >= 0) and (n <= 100) and (n % 2 == 0))
#is_even_number:0에서 100의 범위 안의 짝수를 판별하는 논리연산
print(n , '은 0에서 100의 범위 안에 있는 짝수인가요?' , is_even_number)
