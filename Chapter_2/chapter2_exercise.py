# chapter2_exercise.py

# 문제 1
print("Q1. 평균 점수 구하기")
print("A1.")
kor = 80
eng = 75
math = 55

print("평균: ", (kor + eng + math)/3)

print()
# 문제 2
print("Q2. 자연수 13이 홀수인지 짝수인지 판별할 수 있는 방법은?")
print("A2.")
print("2로 나눈 후 나머지가 0이면 짝수, 나머지가 1이면 홀수로 구분할 수 있다.")
print("나머지: ", 13%2)
if 13%2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")

print()
# 문제 3
print("Q3. 홍길동씨의 주민등록번호를 연월일(YYYYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어보자.")
print("A3.")
pin = "881120-1068234"
yymmdd = pin[:6]
num = pin[7:]
print("연월일: ", yymmdd)
print("뒷자리: ", num)

print()
# 문제 4
print("Q4. 주민등록번호에서 성별을 나타내는 숫자를 출력해보자.")
print("A4.")
pin = "881120-1068234"
print(pin[7])

print()
# 문제 5
print("Q5. replace 함수를 사용하여 a#b#c#d로 바꿔서 출력해보자.")
print("A5.")
a = "a:b:c:d"
b = a.replace(":", "#")
print(b)

print()
# 문제 6
print("Q6. [1, 3, 5, 4, 2] 리스트를 [5, 4, 3, 2, 1]로 만들어보자.")
print("A6.")
a = [1, 3, 5, 4, 2]
a.sort() # 리스트 정렬(오름차순)
a.reverse()
print(a)

print()
# 문제 7
print("Q7. ['Life', 'is', 'too', 'short'] 리스트를 Life is too short 문자열로 만들어 출력해보자.")
print("A7.")
a = ['Life', 'is', 'too', 'short']
result = " ".join(a) # 구분자.join(리스트)
print(result)

print()
# 문제 8
print("Q8. (1, 2, 3) 튜플에 값 4를 추가하여 (1, 2, 3, 4)를 만들어 출력해 보자.")
print("A8.")
a = (1, 2, 3)
a = a + (4,)
print(a)

print()
# 문제 9
print("""Q9.다음과 같은 딕셔너리 a가 있다.
    다음 중 오류가 발생하는 경우를 고르고, 그 이유는?""")
print("A9.")
a = dict()
print(a, "\n")
print("""1) a['name'] = 'python'
2) a[('a',)] = 'python'
3) a[[1]] = 'python'
4) a[250] = 'python'""", "\n")
print("3번) 리스트는 딕셔너리의 Key 값으로 입력될 수 없디.")

print()
# 문제 10
print("Q10. 딕셔너리 a에서 'B'에 해당하는 값을 추출해 보자.")
print("A10.")
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)
print(result)

print()
# 문제 11
print("Q11. a 리스트에서 중복 숫자를 제거해보자.")
print("A11.")
a = [1,1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b)

print()
# 문제 12
print("Q12. 다음과 같이 a, b 변수를 선언한 후 a의 두 번째 요솟 값을 변경하면 b 값은 어떻게 될까? 그리고 이런 이유가 나오는 이유는?")
print("A12.")
a = b = [1, 2, 3]
a[1] = 4
print("b의 두 번째 요솟 값도 a의 두 번째 요솟 값과 같이 변경될 것이다. 왜냐하면 두개의 변수를 동시에 하나의 값으로 지정할 시 같은 메모리 주소에서 값을 가져오기 때문이다.")
print(b)
