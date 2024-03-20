
num=input("세 복권번호를 입력하시오: ")
num=num.split()
a, b, c=map(int,num)
if num==2 and 3 and 9:
    print("상금 1억원")

elif {(num==2 and 3) and (num!=9)}  or {(num==2 and 9) and (num!=3)}  or {(num==3 and 9) and (num!=2)}:
    print("상금 1천만 원")

elif {(num==2) and (num!=3 and 9)} or {(num!=2 and num!=3) and (num==9)} or{(num!=2 and num!=9) and (num==3)}:
    print("상금 1만 원")

elif num!=2 and 3 and 9:
    print("다음 기회에...")
