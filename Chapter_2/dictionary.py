# dictionary.py

# 딕셔너리 쌍 추가
a = {1: 'a'}
a[2] = 'b'
print(a)

a['name'] = 'pey'
print(a)

a[3] = [1, 2, 3]
print(a)

# 딕셔너리 요소 삭제
del a[1]
print(a)

# Key를 사용해 Value 얻기
grade = {'pey': 10, 'juliet': 99}
print(grade['pey'])
print(grade['juliet'])

# -----------------------------------------------

# Key 리스트 만들기 (keys)
a = {'name': 'pey', 'phone': '0119993323', 'birth':'1118'}
print(a.keys())

for k in a.keys():
    print(k)
print(list(a.keys()))

# Value 리스트 만들기 (values)
print(a.values())

# Key, Value 쌍 얻기 (items)
print(a.items())

# Key:Value 쌍 모두 지우기 (clear)
print(a.clear())

# Key로 Value 얻기 (get)
a = {'name':'pey', 'phone': '0119993323', 'birth':'1118'}
print(a.get('name'))
print(a.get('phone'))

# get(x, '디폴트 값') == 딕셔너리 안에 찾으려는 Key 값이 없을 경우 미리 정해둔 디폴트 값을 대신 가져오게 함
print(a.get('foo', 'bar'))

# 해당 Key가 딕셔너리 안에 있는지 조사하기 (in)
a = {'name':'pey', 'phone': '0119993323', 'birth':'1118'}
print('name' in a)
print('mail' in a)
