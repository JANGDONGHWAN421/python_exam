import random
import time

num = random.randint(1,1000)
print("점수 맞춰봐 바보야!")
while True:
    t1 = time.time()
    input_range = input()
    i = int(input_range)

    if i == num:
        print("으악 내가 바보한테 지다니")
        t2 = time.time()
        print("game time %s" %(t2-t1))
        break
    elif i < num:
        print("더 큰 수를 입력해봐")
    elif i > num:
        print("더 작은 수를 입력해봐")

for i in range(1,15):
    print("지금부터 %s 이후 종료됩니다." %i)
    time.sleep(1)
