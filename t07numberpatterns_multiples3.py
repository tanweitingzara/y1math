# Generate multiples of 3 from 1 to 50

START = 1
END = 1000
num = 3
lis = []
for i in range(START, END+1):
  if i % num == 0:
    lis.append(i)
print(lis)
