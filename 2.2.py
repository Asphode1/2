f = open("2.2.txt", "r")
num = f.readline().split()
a = int(num[0])
b = int(num[1])

mt = [None] * a
for i in range(a):
  mt[i] = [None] * b

for i in range(a):
  row = f.readline().split()
  for j in range(b):
    mt[i][j] = row[j]

def determinant(mt: list[list[float]]) -> float | None:
  if(len(mt) != len(mt[0])):
    print("ko co")
  else:
    # tinh dinh thuc
    return

def plus(mt1, mt2) -> list:
  return

def mul(mt1, mt2) -> list:
  return

def writeFile(path: str, s: str) -> None:
  return
