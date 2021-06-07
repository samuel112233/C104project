import csv
import counter
with open('SOCR-HeightWeight.csv')as f:
    reader=csv.reader(f)
    fileData=list(reader)

fileData.pop(0)
newData=[]
for i in range(len(fileData)):
    n=fileData[i][2]
    newData.append(float(n))

data=counter(newData)
modeData = {'75-85':0,
'85-95':0,
'95-105':0,
'105-115':0,
'115-125':0,
'125-135':0,
'135-145':0,
'145-155':0,
'155-165':0,
'165-175':0
}
for height,occurence in data.items():
    if 75<float(height)<85:
        modeData['75-85']+=occurence
    elif 85<float(height)<95:
        modeData['85-95']+=occurence
    elif 95<float(height)<105:
        modeData['95-105']+=occurence
    elif 105<float(height)<115:
        modeData['105-115']+=occurence
    elif 115<float(height)<125:
        modeData['115-125']+=occurence
    elif 125<float(height)<135:
        modeData['125-135']+=occurence
    elif 135<float(height)<145:
        modeData['135-145']+=occurence
    elif 145<float(height)<155:
        modeData['145-155']+=occurence
    elif 155<float(height)<165:
        modeData['155-165']+=occurence
    elif 165<float(height)<175:
        modeData['165-175']+=occurence

modeRange,modeOccurence=0,0
for range,occurence in modeData.items():
    if occurence>modeOccurence:
        modeRange,modeOccurence=[int(range.split('-')[0]),int(range.split('-')[2])],occurence

mode=float((modeRange[0]+modeRange[2])/2)
print(mode)