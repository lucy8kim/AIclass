(a,b,c,d,e,f,g,h,i,j)=map(int,input("10개의 수를 입력하시오: ").split())
list_sd=list((a,b,c,d,e,f,g,h,i,j))
total=sum(list_sd)
mean=total/10
sd=((total-mean)**2/10)**0.5

print("합 :", total)
print("평균 :", mean)
print("표준편차: ", sd)
