A = input()
ls = []
li = str(A)
for j in li:
    ls.append(int(j))
count_z = 0
count_o = 0
for k in ls:
    if(k==1):
        count_o += 1
    if(k==0):
        count_z += 1

if((count_o == 1) or (count_z == 1)):
    print("YES")

else:
    if((count_o == 0) or (count_z == 0)):
        print("NO")
    else:
        print("NO")