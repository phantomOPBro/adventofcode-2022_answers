b = []
c = []
d = []
with open('this.txt') as f:
  elf_cals = f.read().split("\n\n")
for i in elf_cals:
  cals = sum(map(int, i.splitlines()))
  b.append(cals)
max(b)
# Answer to number 1 is 71506
'''
---Part 2---
'''
b.sort(reverse=True)
d = b[0:3]
sum(d)
