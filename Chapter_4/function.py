# function.py

def add(a, b):
    return a + b

a = 3
b = 4
c = add(a, b)
print(c)
print(add(3, 4))

# ------------------------------------------------
# 입력값이 없는 함수

def say():
    return 'Hi'

a = say()
print(a)

# ------------------------------------------------
# 결과값이 없는 함수

def add1(a, b):
    print("%d, %d의 합은 %d입니다." %(a, b, a+b))

add1(3, 4)

a = add1(3, 4)
print(a)

# ------------------------------------------------
# 입력값도 결과값도 없는 함수

def say1():
    print('Hi')

a = say1()
print(a)

# ------------------------------------------------
# 매개변수 지정하여 호출하기

def add2(a, b):
    return a+b

result = add2(a = 3, b = 7)
print(result)

result = add2(b = 5, a = 3)
print(result)

# ------------------------------------------------
# 입력값이 몇 개인지 모를 때

def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(result)

# ------------------------------------------------
# 여러개의 입력을 처리할 때

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

result = add_mul('add', 1, 2, 3, 4, 5)
print(result)

result = add_mul('mul', 1, 2, 3, 4, 5)
print(result)

# ------------------------------------------------
# 키워드 파라미터

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a = 1)
print_kwargs(name = 'foo', age = 3)

# ------------------------------------------------
# return으로 함수 빠져나가기

def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s입니다." %nick)

say_nick("야호")
say_nick("바보")
say_nick("야호")

# ------------------------------------------------
# 매개변수에 초깃값 미리 설정하기

def say_myself(name, old, man=True):
    print("나의 이름은 %s입니다." %name)
    print("나의 나이는 %d살입니다." %old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("박응용", 27)
say_myself("박응용", 27, True)
say_myself("qkrdmdtjs", 27, False)
