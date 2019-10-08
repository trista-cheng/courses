
height = float(input("請輸入您的身高: "))
weight = float(input("請輸入您的體重: "))
bmi = weight/(height/100)**2
if bmi >25:
    print("您過重了")
    ideal = weight*30
    print("您每天需攝取",ideal ,"大卡")
    
    

elif bmi <18.5:
    print("您過輕了")
    ideal = weight*40
    print("您每天需攝取",ideal ,"大卡")


else:
    print("您剛剛好")
    ideal = weight*35
    print("您每天需攝取",ideal ,"大卡")

ca = float(input("請輸入您已經攝取多少大卡: "))
if ca > ideal:
    print("您今天已超過 ", ca-ideal," 大卡")
else:
    print("您今天尚能攝取的卡路里是 ", ideal-ca," 大卡")

