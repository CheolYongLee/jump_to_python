# multiple_union.py

# 3의 배수와 5의 배수의 합

def multiple_union(a, b):
    print("1부터 999까지의 정수 중에 두 숫자의 배수의 합을 구하는 함수입니다.\n 두 숫자를 각각 입력하여주세요.")
    a = int(input("첫번째 숫자: "))
    b = int(input("두번째 숫자: "))
    s = 0
    union = []

    for i in range(1, 1000):
        if i % a == 0 or i % b == 0:
            union.append(i)
    print("%d의 배수와 %d의 배수\n"%(a, b), union)

    for s in union:
        s += s
    print("두 수의 배수의 합\n", s)

multiple_union(3, 5)
