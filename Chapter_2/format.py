# format.py

# 숫자 바로 대입하기
A = "I eat {0} apples".format(3)
print(A)

# 문자열 바로 대입하기
B = "I eat {0} apples".format("five")
print(B)

# 숫자 값을 가진 변수로 대입하기
number = 3
C = "I eat {0} apples".format(number)
print(C)

# 2개 이상의 값 넣기
number = 10
day = "three"
D = "I ate {0} apples. so I was sick for {1} days.".format(number, day)
print(D)

# 이름으로 넣기
E = "I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)
print(E)

# 인덱스와 이름은 혼용해서 넣기
F = "I ate {0} apples. so I was sick for {day} days.".format(10, day=3)
print(F)


# 왼쪽 정렬
G = "{0:<10}".format("hi")
print(G)

# 오른쪽 정렬
H = "{0:>10}".format("hi")
print(H)

# 가운데 정렬
I = "{0:^10}".format("hi")
print(I)

# 공백 채우기
J = "{0:=^10}".format("hi")
print(J)

K = "{0:!^10}".format("hi")
print(K)

# 소수점 표현하기
y = 3.42134234
L = "{0:0.4f}".format(y)
print(L)

M = "{0:10.4f}".format(y)
print(M)

# { 또는 } 문자 표현하기
N = "{{ and }}".format()
print(N)

# ---------------------------------------------------------------------------------------

# f문자열 포매팅
name = '홍길동'
age = 30
O = f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
print(O)

age = 30
P = f'나는 내년이면 {age+1}살이 된다.'
print(P)

d = {'name':'홍길동', 'age':30}
Q = f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'
print(Q)

# 정렬
R = f'{"hi":<10}'
print(R)

S = f'{"hi":>10}'
print(S)


T = f'{"hi":^10}'
print(T)

# 공백 채우기
U = f'{"hi":=^10}'
print(U)

V = f'{"hi":!<10}'
print(V)

# 소수점 표현

y = 3.42134234
W = f'{y:0.4f}'
print(W)

X = f'{y:10.4f}'
print(X)

# {} 문자 표시
Y = f'{{ and }}'
print(Y)
