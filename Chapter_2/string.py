# string.py
# 문자열 관련 함수

# 문자 개수 세기 (count)
a = "hobby"
print(a.count('b'))

# 위치 알려주기1 (find) == 처음 나온 위치 찾기, 존재하지 않으면 -1 반환
a = "Python is the best choice"
print(a.find('b'))
print(a.find('k'))

# 위치 알려주기2 (index) == 처음 나온 위치 찾기, 존재하지 않으면 오류 발생
a = "Life is too short"
print(a.index('t'))
# print(a.index('k'))

# 문자열 삽입 (join) == 문자열 각각의 문자 사이에 삽입 (리스트나 튜플도 입력으로 사용가능)
print(",".join('abcd'))
print(",".join(['a', 'b', 'c', 'd']))

# 소문자를 대문자로 바꾸기 (upper)
a = "hi"
print(a.upper())

# 대문자를 소문자로 바꾸기 (lower)
a = "HI"
print(a.lower())

# 왼쪽 공백 지우기 (lstrip)
a = "  hi  "
print(a.lstrip())

# 오른쪽 공백 지우기 (rstrip)
a = "  hi  "
print(a.rstrip())

# 양쪽 공백 지우기 (strip)
a = "  hi  "
print(a.strip())

# 문자열 바꾸기 (replace)
a = "Life is too short"
print(a.replace("Life", "Your leg"))

# 문자열 나누기 (split)
a = "Life is too short"
print(a.split()) # 공백을 기준으로 문자열 나눔

b = "a:b:c:d"
print(b.split(':')) # :을 기준으로 문자열 나눔
