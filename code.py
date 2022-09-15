import random
import os
import time

data = {}
time = 0
left = []
randResult = []

while True:
  add = input("Enter User: ")
  data.update({time: add})
  if time == 0 or (time % 2) == 0:
    time = time + 1
    continue
  else:
    quit = int(input("1 - Quit, 0 - Continue: "))
    if quit == 1:
      time = time + 1
      if (time % 2) == 0:
        break
      else:
        print("Error")
        time = time + 1
        continue
    elif quit == 0:
      time = time + 1
      continue

for x in range(len(data)):
  left.append(x)

for i in range(int(str(time/2).replace(".0",""))):
  while True:
    randNum_1 = random.choice(left)
    randNum_2 = random.choice(left)
    if randNum_1 != randNum_2:
      randResult.append([randNum_1,randNum_2])
      break
    elif randNum_1 == random.randint(0,time-1):
      continue

  for y in range(2):
    left.remove(randResult[i][y])

os.system("clear")

for z in range(int(str(time/2).replace(".0",""))):
  print(z+1, ")", data[randResult[z][0]], " - ", data[randResult[z][1]])
