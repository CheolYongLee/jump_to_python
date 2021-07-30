# vartest.py

a = 1
def vartest(a):
    a = a + 1

vartest(a)
print(a)

# 함수 안에서 새로 만든 매개변수는 "함수 안에서만"의 변수이기 때문에 매개변수 a는 함수 안에서만의 a이고 함수 밖의 a는 별개의 변수이다.
