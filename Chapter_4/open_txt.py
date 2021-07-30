# open_txt.py

f = open("새파일.txt", 'w')
f.close()

# 파일 객체 = open(파일 이름, 파일 열기 모드)
# 파일 열기 모드/ r = 읽기 모드 - 파일 읽기만 할 때, w = 쓰기 모드 - 내용 쓰기만 할 때, a = 추가 모드 - 파일의 마지막에 새로운 내용을 추가 할 때


# 특정 디렉토리에 파일을 생성 할 때
f = open("C:/Users/ypopp/OneDrive/바탕 화면/Git_Hub/jump_to_python/Chapter_4/New.txt", "w")
f.close()
