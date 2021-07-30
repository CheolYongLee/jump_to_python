# vartest_return.py

a = 1
def vartest(a):
    a = a + 1
    return a

a = vartest(a) # vartest 함수에 a(=1)의 값을 입력하여 함수를 실행 후 return을 통하여 함수 안에서 입력 된 매개변수 a의 값을 결괏값으로 반환하여 함수 밖의 a 값으로 입력한다.
print(a) # 함수에서 계산된 a의 값을 return으로 결괏값을 반환하여 함수 밖의 a에 입력함.
