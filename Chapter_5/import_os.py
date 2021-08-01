# import_os.py

import os

# 내 시스템의 환경 변수 값을 알고 싶을 때
print(os.environ)

print(os.environ['PATH'])


# 디렉토리 위치 변경하기

os.chdir("C:/WINDOWS")


# 디렉토리 위치 돌려받기

print(os.getcwd())


# 시스템 명령어 호출하기

# print(os.system("시스템 명령어"))
print(os.system("dir"))


# 실행한 시스템 명령어의 결괏괎 돌려받기

f = os.popen("dir")
print(f.read())


# ==========================================================

# 파일을 복사하는 모듈
'''
import shutil
shutil.copy("src.py", "dst.txt.")
'''

# ==========================================================

# 디렉토리에 있는 파일들을 리스트로 만들기

import glob
print(glob.glob("c:/Users/*"))


# ==========================================================

# 파일을 임시로 만들어서 사용할 때 유용한 모듈

import tempfile
filename = tempfile.mkstemp()
print(filename)
f.close() # 생성한 임시 파일이 자동으로 삭제됨


# ==========================================================

# 시간과 관련된 모듈

import time

# (1970년 1월 1일 0시 0분 0초)를 기준으로 지난 시간을 초 단위로 돌려준다.
print(time.time())

# time.time()이 돌려준 실수 값을 사용하여 연도, 월, 일, 시, 분, 초, .... 의 형태로 바꾸어준다.
print(time.localtime(time.time()))

# time.localtime()에 의해 반환 된 (튜플형태의 값)을 인수로 받아서 날짜와 시간을 알아보기 쉬운 형태로 돌려주는 함수
print(time.asctime(time.localtime(time.time())))

# 간편하게 현재 시간만을 돌려주는 함수
print(time.ctime())

# 세밀하게 표현하는 여러가지 포맷코드를 활용
print(time.strftime('%X', time.localtime(time.time())))
