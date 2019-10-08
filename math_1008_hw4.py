

print("幫你算出你的成績，轉換成 GPA 喔!祝你推甄超順利!")


total = 0
amount = 0
while True:
    grade = input("請輸入成績: ")
    credit = input("請輸入此科的學分數:")
    total = total + float(grade)*int(credit)
    amount = amount + int(credit)
    go = input("是否繼續輸入")
    print()
    if go == "是":
        pass
    else:
        break

avg = total/amount
if avg >= 90:
    print("你的成績: %f 等第: %s GP: %f" % (avg, "A+", 4.3))
elif avg >= 85:
    print("你的成績: %f 等第: %s GP: %f" % (avg, "A", 4.0))
elif avg >= 80:
    print("你的成績: %f 等第: %s GP: %f" % (avg, "A-", 3.7))
elif avg >= 77:
    print("你的成績: %f 等第: %s GP: %f" % (avg, "B+", 3.3))
elif avg >= 73:
    print("你的成績: %f 等第: %s GP: %f" % (avg, "B", 3.0))

elif avg >= 70:
    print("你的成績: %f 等第: %s GP: %f" % (avg, "B-", 2.7))

elif avg >= 67:
    print("你的成績: %f 等第: %s GP: %f" % (avg, "C+", 2.3))
elif avg >= 63:
    print("你的成績: %f 等第: %s GP: %f" % (avg, "C", 2.0))

elif avg >= 60:
    print("你的成績: %f 等第: %s GP: %f" % (avg, "C-", 1.7))
elif avg >= 50:
    print("你的成績: %f 等第: %s GP: %f" % (avg, "D", 1.0))
elif avg >= 1:
    print("你的成績: %f 等第: %s GP: %f" % (avg, "E", 0.0))
else:
    print("你的成績: %f 等第: %s GP: %f" % (avg, "X", 0.0))






