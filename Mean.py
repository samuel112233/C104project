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
total=0
for x in newData:
    total+=x

mean=total/num
print(mean)