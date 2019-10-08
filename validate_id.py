
areaDict = {"A":"台北市", "B": "台中市", "C": "基隆市", 
    "D": "台南市", "E": "高雄市", "F": "新北市", "G": "宜蘭縣", 
    "H": "桃園縣", "I": "嘉義市", "J": "新竹縣", "K": "苗栗縣", 
    "L": "臺中縣", "M": "南投縣", "N":"彰化縣", "O": "新竹市", "P": "雲林縣",
    "Q": "嘉義縣", "R": "臺南縣", "S": "高雄縣", "T": "屏東縣", "U": "花蓮縣",
    "V": "臺東縣", "W": "金門縣", "X": "澎湖縣", "Y": "陽明山", "Z":"連江縣",}

numDic = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 
    'H': 17, 'I': 34, 'J': 18, 'K': 19, 'L': 20, 'M': 21, 'N': 22, 'O': 35, 
    'P': 23, 'Q': 24, 'R': 25, 'S': 26, 'T': 27, 'U': 28, 'V': 29, 'W': 30, 
    'X': 31, 'Y': 32, 'Z': 33}
while True:

    idNumber = input("請輸入你的身分字號: ")
    if idNumber == "byebye":
        print("bye!")
        break

    if len(idNumber) == 10:
        pass
    else:
        print(("身分證應該是 10 碼，你只輸入 %d 碼"%(len(idNumber))))
        continue

    if (idNumber[0].upper() in numDic):
        pass
    else:
        print("第一碼應該是 A - Z 的英文字母")
        continue

    if idNumber[1:].isnumeric():
        pass
    else:
        print("後九碼應該是數字")
        continue

    idNumber = idNumber[0].upper() + idNumber[1:]


    area = areaDict[idNumber[0]]
    print("你的出身地為:", area)
    if idNumber[1] == "1":
        print("你的性別為: 男")
    else:
        print("你的性別為: 女")

    check = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    numId = str(numDic[idNumber[0]]) + idNumber[1:]
    checksum = 0
    for i, v in enumerate(numId[:-1]):
        v = int(v)
        checksum = checksum +v*check[i]
    last = 10 - checksum%10

    if last == int(idNumber[-1]):
        print("你的身分證是有效的\n")
    else:
        print("你的身分是無效的\n")


    