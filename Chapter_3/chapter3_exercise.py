# chapter3_exercise.py

# 문제 1
print("Q1. 다음 코드읭 결괏값은?")
print("""------------------------------------------------------------
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")
------------------------------------------------------------""")
print("A1.")
print("shirt가 출력될 것이다.")

print()
# ----------------------------------------------------------
# 문제 2
print("Q2. 1부터 1000까지의 자연수 중 3의 배수의 합 구하기")

print("A2.")

result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1
print(result)

print()
# ----------------------------------------------------------
# 문제 3.
print("Q3. 다음과 같은 화면이 출력 되도록 작성해보자.")
print("""------------------------------------------------------------
*
**
***
****
*****
------------------------------------------------------------""")
print("A3.")
i = 0
while True:
    i += 1
    if i > 5: break
    print("*" * i)

print()
# ----------------------------------------------------------
# 문제 4.
print("Q4. 1부터 100까지 출력해보자.")
print("A4.")
for i in range(1, 101):
    print(i)

print()
# ----------------------------------------------------------
# 문제 5
print("Q5. for문을 사용하여 A학급의 평균 점수를 구해 보자.")
print("A5.")
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A:
    total += score
average = total/(len(A))
print(average)

print()
# ----------------------------------------------------------
# 문제 6
print("Q6. 리스트 중 홀수에만 2를 곱하여 저장하는 다음 코드를 리스트 내포를 사용하여 표현해보자.")
print("""------------------------------------------------------------
number = [1, 2, 3, 4, 5]

result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)
------------------------------------------------------------""")
print("A6.")
numbers = [1, 2, 3, 4, 5]

# 리스트 내포를 사용 할 때에는 append는 사용되지 않는다.
result = [i * 2 for i in numbers if i % 2 == 1]
print(result)
