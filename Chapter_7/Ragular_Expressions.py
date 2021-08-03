# Ragular_Expressions

data = """
park 800905-1049118
kim 700905-1059119
"""

result = []
for line in data.split("\n"): # 줄 단위 문자마다 나누기
# data.split("\n") == ['', 'park 800905-1049118', 'kim 700905-1059119', '']


    word_result = []

    for word in line.split(" "): # 공백 문자마다 나누기
        # line.split(" ") == [' '] ['park' '800905-1049118] ['kim' '700905-1059119'] [' ']
    
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
        #  요소의 길이가 14이고, [처음부터 5까지] 6글자가 자연수(양의 정수)이고, [7부터 끝까지]가 자연수(양의 정수)일 때

            word = word[:6] + "-" + "*******"
        word_result.append(word)
    result.append(" ".join(word_result)) # 나눈 단어 조립하기
    
print("\n".join(result))    


# ==========================================================
# 정규 표현식을 사용하여 작성

print("정규 표현식을 사용한 작성법")
import re # 정규 표현식을 사용하기 위한 모듈

data = """
park 800905-1049118
kim 700905-1059119
"""

pat = (re.compile("(\d{6})[-]\d{7}"))

print(pat.sub("\g<1>-*******", data))
