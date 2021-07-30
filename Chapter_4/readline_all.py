# readline_all.py

f = open("C:/Users/ypopp/OneDrive/바탕 화면/Git_Hub/jump_to_python/Chapter_4/New.txt", "r")
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

# ----------------------------------------------------------
# 위의 코드와 다른 점은 입력을 받는 방식의 차이가 있다는 것이다.
# 위의 코드는 파일을 사용한 입력 방식이고,
# 아래의 코드는 키보드를 이용하여 사용자의 입력을 방는 형식이다.

while 1:
    data = input()
    if not data: break
    print(data)

# ----------------------------------------------------------

# readlines 함수 사용하기
f = open("C:/Users/ypopp/OneDrive/바탕 화면/Git_Hub/jump_to_python/Chapter_4/New.txt", "r")
lines = f.readlines()
for line in lines:
    print(line)
f.close()

# read 함수 사용하기
f = open("C:/Users/ypopp/OneDrive/바탕 화면/Git_Hub/jump_to_python/Chapter_4/New.txt", "r")
data = f.read()
print(data)
f.close()
