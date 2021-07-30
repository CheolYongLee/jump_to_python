# vartest_global.py

a = 1
def vartest():
    global a
    a = a + 1

vartest()
print(a)

# 함수 밖의 a 변수를 global을 이용하여 직접 사용하는것은 별로 좋지 않다. 외부 변수에 종속적인 함수는 별로 좋은 함수가 아니다.
# global은 되도록 사용하지 말고 return을 통하여 사용 하는 방법을 권고한다.
