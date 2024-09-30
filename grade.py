marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number + 1
    if mark < 60:
      continue
    print("%d번 학생의 합격을 진심으로 축하드립니다." % number)
