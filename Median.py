import csv
with open('SOCR-HeightWeight.csv')as f:
    reader=csv.reader(f)
    fileData=list(reader)

fileData.pop(0)
newData=[]
for i in range(len(fileData)):
    n=fileData[i][2]
    newData.append(float(n))

num=len(newData)
newData.sort()
if num%2==0:
    median1=float(newData[num//2])
    median2=float(newData[num//2-1])
    median=(median1+median2)/2

else:
    median=newData[num//2]

print(median)