# writedata.py

f = open("C:/Users/ypopp/OneDrive/바탕 화면/Git_Hub/jump_to_python/Chapter_4/New.txt", "w")
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" %i
    print(data)
    f.write(data) # data를 파일 객체 f에 써라
f.close()
