
while True:
    name = input("同學您好，請輸入您的姓名:")
    department = input("請輸入您的系級")
    number = input("請輸入您的學號：")

    reminder = ("{} {} 同學您好，這是一份有關網路使用行為的調查量表，主要的內容是想瞭解"
        "您上網的情形。請您花幾分鐘的時間填寫，在此謝謝您的參與和協助!請問您準備好要開始"
        "了嗎？請輸入Y (代表Yes)or N (代表No)：").format(department, name)
    a = input(reminder)
    if len(a) != 1:
        print("無效回應，請重新執行程式><")
        break
    elif a == "Y":
        print("耶耶感謝你！題目準備開始")
        print("="*50)
        b = input("這半年以來，您是否有使用電腦網路?是請填1，否請填2")
        if len(b) == 1:
            if b == "1":
                print("請繼續作答")
                print("下面是一些有關個人使用網路情況的描述請評估您目前的實際情形是否與句中的描述一致並輸入數字到該頁面中。由1至4，數字越大，表示句中所描述的情形與目前您實際的情形愈符合")

            elif b == "2":
                print("您不符合本問卷需求，請停止作答")
                a = "@"
                break
            else:
                
                a = "N"
                print("無效回應，請重新執行程式><")
                break

    elif a == "N":
        print("嗚嗚我們下次見")
        break
    elif a == "@":
        print("謝謝您的參與！祝您平安喜樂！")
    else:
        print("無效回應，請重新執行程式")
        break


