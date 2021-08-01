# chapter4_exercise.py

# 문제 1
print("Q1. 주어진 자연수가 홀수인지 짝수인지 판별해주는 함수(is_odd)를 작성해보자")
print("A1.")

def is_odd(number):
    if number % 2 == 1: # 홀수면 True
        return True
    else:
        False

print()
# ----------------------------------------------------------
# 문제 2
print("Q2. 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수 작성.")
print("A2.")
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return print(result/len(args))

avg_numbers(1, 2)
avg_numbers(1, 2, 3, 4, 5)

print()
# ----------------------------------------------------------
# 문제 3
print("Q3. 입력받은 두개의 숫자를 더하여 돌려주는 프로그램 작성")
print("A3.")

input1 = int(input("첫번째 숫자를 입력하세요: "))
input2 = int(input("두번째 숫자를 입력하세요: "))
# int(input())으로 숫자를 입력받지 않으면 문자 형식으로 받아서 제대로 된 연산이 불가능 하다. (단순히 숫자를 연결해서 출력함)

total = input1 + input2
print("두 수의 합은 %s입니다." %total)

print()
# ----------------------------------------------------------
# 문제 4
print("Q4. 다음 중 출력 결과가 다른 한 개를 골라보자")
print("""------------------------------------------------------------
1) print("you" "need" "python")
2) print("you"+"need"+"python")
3) print("you", "need", "python")
4) print("".join(["you", "need", "python"]))
------------------------------------------------------------""")
print("A4.")
print("3번, 콤마는 띄어쓰기로 사용된다.")

print()
# ----------------------------------------------------------
# 문제 5
print("Q5. test.txt에서 ""Life is too short"" 문자열을 저장한 후 다시 읽어서 출력하는 프로그램을 작성해보자")
print("A5.")
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()
# open() 함수를 이용하여 파일을 열었다면 close()를 잊지말고 해야한다.

print()
# ----------------------------------------------------------
# 문제 6
print("Q6. 사용자의 입력을 파일(test1.txt)에 저장하는 프로그램을 작성해보자. (단, 다시 실행해도 기존 내용을 유지하고 내용을 추가할 것)")
print("A6.")

user_input = input("저장할 내용을 입력하세요: ")
f = open("test1.txt", "a")
f.write(user_input)
f.write("\n")
f.close()

print()
# ----------------------------------------------------------
# 문제 7
print("Q7. test2.txt의 기존 내용 중 'java'라는 문자열을 'python'으로 바꾸어서 저장해보자.")
print("""--------기존 내용--------
Life is too short
you need java
-------------------------""")
print("A7.")

f = open("test2.txt", 'r')
body = f.read()
# readline() = 첫 줄만 읽기, readlines() = 모든 줄 단위를 리스트로 읽기, read() = 모든 내용을 문자열로 읽기
f.close()

print(body)

body = body.replace("java", "python")

print(body)

f = open("test2.txt", 'w')
f.write(body)
f.close()
