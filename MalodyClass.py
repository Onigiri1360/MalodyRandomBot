# -*- coding: utf-8 -*-
"""MalosdyClss.py
"""

""" CLASS I では30,31,32
    CLASS II では31,32,33
    CLASS III では32,33,34
    CLASS IV では33,34,35
    CLASS V では 34,35,36
    CLASS ∞ では 35,36,WE 
    からそれぞれランダム
"""

import random
splitRecord1 = []
splitRecord2 = []
splitSongDetail = []
noTemp = []
sortedSongs1 = []
sortedSongs2 = []
sortedSongs3 = []
count = 0
with open("./MalodySongs.csv") as n:
    recordNormalLine = n.readlines()
    recordNormal = n.read()
  
with open("./MalodyRandom6_WE.csv") as w:
    recordWELine = w.readlines()
    recordWE = w.read()

 
for i in range(len(recordNormalLine)):
    lineNum = i + 1
    record1 = recordNormalLine[i] #record1 = Normalの行単位のレコード
    splitRecord1.append(record1.split(","))

for j in range(len(recordWELine)):
    lineNum = j + 1
    record2 = recordWELine[j] #record2 = WE・隔離枠の行単位のレコード
    splitRecord2.append(record2.split(","))

#定数ではなくレベルで指定する場合は.0~.9で絞り込み


for r in range(1,7):
    lowerLevel1 = 29 + r
    higherLevel1 = lowerLevel1 + 0.9
    lowerLevel2 = 30 + r
    higherLevel2 = lowerLevel2 + 0.9
    lowerLevel3 = 31 + r
    higherLevel3 = lowerLevel3 + 0.9
    

    for a in range(len(splitRecord1)):
        temp = splitRecord1[a]
        if lowerLevel1-0.1 < float(temp[2]) and higherLevel1+0.1 > float(temp[2]):
            sortedSongs1.append(temp)
        if lowerLevel2-0.1 < float(temp[2]) and higherLevel2+0.1 > float(temp[2]):
            sortedSongs2.append(temp)
        if r == 6:
            for b in range(len(splitRecord2)):
                WETemp = splitRecord2[b]
                sortedSongs3.append(WETemp)
        else:
            if lowerLevel3-0.1 < float(temp[2]) and higherLevel3+0.1 > float(temp[2]):
                sortedSongs3.append(temp)


    setSong1 = sortedSongs1[random.randint(0,len(sortedSongs1)-1)]
    title1 = setSong1[0].replace('"', '')
    if setSong1[0] == "Destruction3.2.1":
        title1 = "DESTRUCTION3,2,1"
    difficulty1 = setSong1[1]
    const1 = setSong1[2]


    setSong2 = sortedSongs2[random.randint(0,len(sortedSongs2)-1)]
    title2 = setSong2[0].replace('"', '')
    if setSong1[0] == "Destruction3.2.1":
        title2 = "DESTRUCTION3,2,1"
    difficulty2 = setSong2[1]
    const2 = setSong2[2]


    setSong3 = sortedSongs3[random.randint(0,len(sortedSongs3)-1)]
    title3 = setSong3[0].replace('"', '')
    if setSong1[0] == "Destruction3.2.1":
        title3 = "DESTRUCTION3,2,1"
    difficulty3 = setSong3[1]
    const3 = setSong3[2]


    print("")
    if r == 1:
        print("Random Set I 選曲結果")
    elif r == 2:
        print("Random Set II 選曲結果")
    elif r == 3:
        print("Random Set III 選曲結果")
    elif r == 4:
        print("Random Set IV 選曲結果")
    elif r == 5:
        print("Random Set V 選曲結果")
    elif r == 6:
        print("Random Set -Infinity- 選曲結果")
    print(f"1曲目：{title1} ({difficulty1})")
    print(f"2曲目：{title2} ({difficulty2})")
    print(f"3曲目：{title3} ({difficulty3})")
    print("")
    print("")
    sortedSongs1 = []
    sortedSongs2 = []
    sortedSongs3 = []
