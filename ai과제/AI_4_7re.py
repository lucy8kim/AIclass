a,b,c=map(int,input("세 수를 입력하시오: ").split())

def mean3(a,b,c):
    mean = (a+b+c)/3
    return mean

def max3(a,b,c):
    mx = max(a,b,c)
    return mx

def min3(a,b,c):
    mi = min(a,b,c)
    return mi

print(a,b,c, "의 평균값은", mean3(a,b,c))
print(a,b,c, "의 최댓값은", max3(a,b,c))
print(a,b,c, "의 최솟값은", min3(a,b,c))


    
