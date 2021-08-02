# tabto4.py

# a 파일의 탭을 4개의 공백으로 바꾸어 b에 저장
# 명령 프롬프트 기준
# 이 파일이 있는 경로>python tabto4.py a.txt b.txt
import sys

src = sys.argv[1]
dst = sys.argv[2]

f = oprn(src)
tab_content = f.read()
f.close()
space_content = tab_content.replace("\t", " "*4)

f.open(dst, 'w')
f.write(space_content)
f.close()
