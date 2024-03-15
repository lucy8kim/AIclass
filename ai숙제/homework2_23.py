tr = int(input('세 자리 정수를 입력하시오: '))
#tr:세 자리 정수

hun = tr//100
#hun:백의 자리

de = (tr%100)//10
#de:십의 자리

o = tr%10
#o:일의 자리
print("백의 자리: " , hun , "\n십의 자리: " , de , "\n일의 자리: " , o)
