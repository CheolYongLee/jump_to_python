# variable.py

# 변수 a가 가리키는 메모리의 주소
a = [1, 2, 3]
print(id(a))

# 리스트를 복사할 때
a = [1, 2, 3]
b = a

print(id(a))
print(id(b))

# a와 b가 가리키는 객체는 동일한가?
print(a is b)


a[1] = 4
print(a)
print(b)

# [:] 사용
a = [1, 2, 3]
b = a[:]
a[1] = 4
print(a)
print(b)

# copy 모듈 사용
from copy import copy
a = [1, 2, 3]
b = copy(a)
print(a)
print(b)

# 같은 값을 가지는 두 변수의 메모리 주소 비교
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)

print(id(a))
print(id(b))

# 변수를 만드는 여러 가지 방법
## 튜플 형식
a, b = ('python', 'life')
print(a)
print(b)
print("*" * 20)

(a, b) = 'python', 'life'
print(a)
print(b)

print("*" * 20)

## 리스트 형식
[a, b] = ['python', 'life']
print(a)
print(b)

print("*" * 20)

# 여러개의 변수에 같은 값을 대입 == 같은 메모리 주소를 할당
a = b = 'python'
print(a)
print(b)
print(id(a))
print(id(b))
print("*" * 20)

# 두 변수의 값을 바꾸기
a = 3
b = 5
print(a)
print(b)

a, b = b, a
print(a)
print(b)
