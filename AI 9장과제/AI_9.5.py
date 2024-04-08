a = 1
b = 1
c = 2
d = 3
e = 3
if a is b:
    print('a와 b는 같은 객체인가?', a is b)

if b is not c:
    print('b와 c는 같은 객체인가?', b is c)

if c is not d:
    print('c와 d는 같은 객체인가?', c is d)

if d is e:
    print('d와 e는 같은 객체인가?', d is e)
