# mod1.py

def add (a, b):
    return a + b

def sub (a, b):
    return a - b


# 이 파일을 직접 실행하였을 때만 사용되게 하기 위한 부분
# 대화형 인터프리터나 다른 파일에서 이 모듈을 불러서 사용 할 때에는 실행되지 않
if __name__ == "__main__":
    print(add(1, 4))
    print(sub(4, 2))
    
