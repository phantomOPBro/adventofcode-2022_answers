Bash 
pbpaste > input.txt

---
Python

with open('input.txt') as f:
    a = f.read().split('\n')
arr = []
arr2 = []
def do_it(that):
    for i in that:
        b = len(i)
        if b%2 == 0:
            string1 = i[0:b//2]
            string2 = i[b//2:]
        else:
            string1 = i[0:(b//2+1)]
            string2 = i[(b//2+1):]
        arr.append(''.join(sorted(set.intersection(set(string1), set(string2)))))
lookup = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26,'A':27,'B':28,'C':29,'D':30,'E':31,'F':32,'G':33,'H':34,'I':35,'J':36,'K':37,'L':38,'M':39,'N':40,'O':41,'P':42,'Q':43,'R':44,'S':45,'T':46,'U':47,'V':48,'W':49,'X':50,'Y':51,'Z':52}
for i in arr:
    arr2.append(lookup[i])
sum(arr2)
---
Part 2
---
split_lists = [a[x:x+3] for x in range(0, len(a), 3)]
for i in split_lists:
    arr.append(''.join(sorted(set.intersection(set(i[0]), set(i[1]), set(i[2])))))
for i in arr:
    arr2.append(lookup[i])
sum(arr2)
