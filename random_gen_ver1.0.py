import time
from random import choice

fileName = input("Enter Random List File Name:")
ranlist = open(fileName,"r")
ranlist = ranlist.read()
y = ranlist.split()
data = []

print('Welcome to Randomize Program')

while True:
    inp = input('please enter R to random :')
    if inp == 'R' or inp == 'r':
        inital = input('Enter inital Subject :')
        data.append(inital)
        item = choice(y)
        print('Randomzie Result:',item)
        data.append(item)
        index = y.index(item)
        del y[index]
        if len(y) == 0:
            break
    else:
        break

timestr = time.strftime("%Y%m%d-%H%M%S")
nameNew = 'listran' + timestr + ".txt"
newRanfile = open(nameNew, "a")
for itemRan in y:
    newRanfile.write("%s\n" % itemRan)
newRanfile.close()

RanReport = open('Randomize_Report.txt',"a")
txt = 'Randomize Reprot At ' + time.strftime("%d-%b-%Y-%H%M%S") + '\n'
RanReport.write(txt)
for dataRan in data:
    RanReport.write("%s\n" % dataRan)

print('Close Program !')
