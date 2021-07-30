# for.py

test_list = ['one', 'two', 'three']

for i in test_list:
    print(i)

# ------------------------------------------------

a = [(1, 2), (3, 4), (5, 6)]

for (first, last) in a:
    print(first + last)

# ------------------------------------------------

a = range(0, 10)
print(a)

# ------------------------------------------------
# 1부터 101까지 더하기

number = 0

for i in range(1, 101):
    number = number + i
print(number)

# ------------------------------------------------
# 구구단 2단부터 9단까지

for i in range(2, 10):
    for j in range(1, 10):
        print("%d * %d = %d \n" %(i,j,(i*j)))

# ------------------------------------------------
# 리스트 내포하기

a = [1, 2, 3, 4]
result = []

for num in a:
    result.append(num*3)
print(result)

# ------------------------------------------------

a = [1, 2, 3, 4]
result = [num * 3 for num in a]
print(result)

# ------------------------------------------------
# 짝수만 계산하기

a = [1, 2, 3, 4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)

# ------------------------------------------------

result = [x*y for x in range(2, 10) for y in range(1, 10)]
print(result)
