# while.py

# 나무 찍기

treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." %treeHit)
    if treeHit == 10:
        print("나무 넘어집니다")
        
# ------------------------------------------------
# 항목 입력받기

prompt = """
1. Add
2. Del
3.List
4. Quit

Enternumber: """

number = 0

while number != 4:
    print(prompt)
    number = int(input())

# ------------------------------------------------
# 커피 판매하기

coffee = 10
money = 300

while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee - 1
    print("남은 커피의 양은 %d개입니다.\n" %coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

# ------------------------------------------------
# 홀수 출력하기

a = 0

while a < 10:
    a = a + 1

    if a % 2 == 0: continue
    print(a)

# ------------------------------------------------
# 무한 루프

while True:
    print("Ctrl + C를 눌러야 while문을 빠져나갈 수 있습니다
