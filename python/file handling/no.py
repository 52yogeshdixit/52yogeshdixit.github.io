f8 = open("demo.txt","r")
n = [str(x) for x in range(10000)]
for i in f8:
    for j in i.split():
        if(j in n):
            print(j)
f8.close()
