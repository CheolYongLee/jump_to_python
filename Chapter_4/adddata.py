# adddata.py

f = open("C:/Users/ypopp/OneDrive/바탕 화면/Git_Hub/jump_to_python/Chapter_4/New.txt", "a")
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()

# ----------------------------------------------------------

# with문과 함께 사용하기

f = open("foo.txt", "w")
f.write("Life is too short, you need python")
f.close()

# 위의 코드와 동일
with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")
