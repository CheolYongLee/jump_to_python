# vartest_error.py

def vartest(a):
    a = a + 1

vartest(3)
print(a)

# 함수 안에서 선언한 매개변수는 함수 안에서만 사용 될 뿐 함수 밖에서는 사용되지 않는다.
# 그렇기에 함수 밖의 a에 대한 값이 없으므로 에러가 발생한다.
