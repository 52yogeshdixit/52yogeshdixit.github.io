f2 = open("demo.txt","r")
sm = 0
for line in f2:
    l = line.split()
    c = len(l)
    sm = sm + c
print("The no. of words in file are :",sm)
f2.close()
