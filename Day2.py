#         ---PART-ONE---
#
def verify(line):
   liste = [int(x) for x in line.split(' ')]
   if liste != sorted(liste) and liste != sorted(liste, reverse=True):
       return 0
   for x in range(len(liste) - 1):
       if abs(int(liste[x]) - int(liste[x + 1])) not in [1, 2, 3]:
           return 0
   return 1

with open("input.txt") as file:
   rst = sum(verify(line) for line in file.read().splitlines())
   print(rst)


#         ---PART-TWO---
#
def verify(liste):
   if liste != sorted(liste) and liste != sorted(liste, reverse=True):
       return 0
   for x in range(len(liste) - 1):
       if abs(int(liste[x]) - int(liste[x + 1])) not in [1, 2, 3]:
           return 0
   return 1

def modify(line):
   liste = [int(x) for x in line.split(' ')]
   if verify(liste) == 1:
       return 1
   for x in range(len(liste)):
       tmp = liste.copy()
       tmp.pop(x)
       if verify(tmp) == 1:
           return 1
   return 0

with open("input.txt") as file:
   rst = sum(modify(line) for line in file.read().splitlines())
   print(rst)