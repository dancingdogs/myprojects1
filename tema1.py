myfile=open('C:/Users/User/Desktop/tema1st.txt','r')

mylist=myfile.read()

mylist=mylist.split('\n')
n=300
x=[]
y=[]


for i in range(len(mylist)):

    mylist[i]=mylist[i].split(':')
    x.append(mylist[i][0])              #1st split
    mylist[i][1]=mylist[i][1].split('(')
    y.append(mylist[i][1])              #2nd split
    y[i]=y[i][0]

z=x
for i in range(len(x)):
    z[i]=x[i]+y[i]            #lista de interes

#print(mylist)
#print(x)
#print(y)
#print(z)

list1=[]
listout=[]

for i in range(n):
    num_str=str(i)
    list1.append(num_str.zfill(3))

for i in list1:
    for j in z:
        if i in j:
            listout.append(j)
        
#print(list1)
#print(listout)
l=list1
for i in range(len(l)):
    for j in range(len(listout)):
        if l[i] in listout[j]:
            l[i]=listout[j]


#print(l)


def insert_comma(string,index):
    return string[:index] + ',' + string[index:]

for i in range(len(l)):
    l[i] = insert_comma(l[i],3)

for i in range(len(l)):
    l[i]=(" ".join(l[i].split()))

#print(l)


finalString=('\n'.join(l[1:]))
print(finalString)     

output_file= open('C:/Users/User/Desktop/tema1stout.txt','w')
output_file.write(finalString)
output_file.close()


#print(list1)
#print(listout1)
#print(l)
#print(lst)
#print(listout1)
#print(l)


myfile.close()


