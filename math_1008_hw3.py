
import math
while True:
    wage = input("想知道工作幾年有100萬，請輸入預期月薪: ")
    if "不" in wage:
        print("好吧那不吵你了，我要去賺錢了，掰掰")
        break
    else:
        wage = float(wage)
    cost = float(input("請輸入預期月支出: "))

    year = math.ceil(1000000/(wage-cost))
    print("需要 %d 年喔\n" % (year, ))