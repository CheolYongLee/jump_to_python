# marks3.py

marks = [90, 25, 67, 45, 80]

for number in range(len(marks)):
    if marks[number] < 60: continue
    print("%d번째 학생 합격입니다. 축하드립니다." %(number + 1))
