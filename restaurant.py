# 餐廳推薦
# 提供不同校區 的各類別 餐廳
# 先以 dictionary 存好各校區 各類別 的餐廳
# 使用者先輸入 校區
# 再選擇餐廳類別
#
# 有防呆機制
# 且如果在選擇餐廳類別 錯誤後不需重新選擇校區 可繼續選擇正確的餐廳類別

import random

print("歡迎使用 '要吃什麼' 系統~~\n讓吃東西小天使幫你找找")

categoryDict = {
    'A': '中式',
    'B': '西式',
    'C': '日韓',
    'D': '其他異國(東南亞)',
    'E': '點心',
}
queryString = ''

restaurantDict = {
    '政大': {
        'A': ['四川飯館','敏忠餐廳','八方雲集','喜記燒臘','四五大街','左撇子','MY麵屋','大汗麻辣鴨血臭豆腐','重慶酸辣粉','健康滷味','呷麵騎士','江記水盆羊肉'],
        'B': ['麥當勞','JUICY BOND','世界大同(太難吃不推薦)','舒曼','米塔','SUBWAY','提洛斯','摩斯','享窩'],
        'C': ['金鰭日式料理','加賀日式料理','松町和風小舖','樂山食堂','小丼作食堂','八角和食','韓大佬韓式精緻料理','高句麗','阿里郎韓國小吃','韓國朴媽媽美食','韓國首爾小吃','韓半島'],
        'D': ["多果異國風味料理","小曼谷滇泰料理","華越美食","滇味廚房","越南大食館","明泰傳統小吃","私房麵","波波恰恰","世界大同","越南赤肉羹"],
        'E': ['水煎包','小木屋鬆餅','可麗餅','明池豆花','77巷燒仙草','紅豆餅','小公寓','Louisa','元老蔥抓餅','麵包大亨'],
    },
    '台大':{
        'A': ['鳳城燒臘粵菜','小飯館兒','小飯館兒','台大牛莊','祥記號美食小吃','金雞園','香港泉記小吃館','藍家割包','佳興魚丸店','無名魷魚羹','龍哥無骨雞腿排','蕭家傳統小吃','阿英滷肉飯','指有雞飯','胡饕米粉湯'],
        'B': ['Living One','好處 Have A Nice Day','新卡莎素食西餐廳','台大牛莊','土司吐司 ToasToasT','SEMINAR西餐廳','吃吐吧','義饗食堂','龐德羅莎(台大店)','Cafe Bastille','Bravo Burger發福廚房公館台大店','貳樓餐廳 Second Floor Cafe 公館店','Curry Kitchen咖哩廚房(台大辛亥店)'],
        'C': ['靜壽司','京都日式拉麵','赤神日式豬排','蔥丼','平山家日式料理','狂愛咖哩','韓庭州韓國料理','韓天閣','韓江館銅盤烤肉','首爾之星','梅江韓國銅盤烤肉',],
        'D': ["池先生 Kopitiam","idiots toast & curry三個傻瓜蔬食印度餐廳","Sababa沙巴巴中東美食","俄羅斯城堡","滇味小館","Masala House 香料館","希臘左巴","Lacuz 新泰食餐廳","SABABA PITA BAR中東食堂","THAIHAND 右手餐廳"],
        'E': ['Mr.雪腐','鴉片粉圓','公館酒釀湯圓','藍家割包','北海道脆皮甜甜圈','老張碳烤小燒餅','倆倆號','怪舒芙 Monster Souffle','地瓜球','晴光紅豆餅'],
    },
    '清交': {
        'A': ['清大雙囍餛飩 老虎麵','香港銅鑼灣','清大滷味','如意麵食館 牛肉麵','大腸蚵仔麵線臭豆腐','新竹市清大夜市士林蔥抓餅','鴨香意麵',' 榮茂滷肉飯','大鼓肉夾饃','賈董的麵','眷村小吃','老四川麵食館','貳壹村精緻麵點'],
        'B': ['麥當勞-新竹清大店','芙歐義式餐廳(FULLPASTA)','海洋牛排','小木屋鬆餅新竹清大店','果子咖啡新竹清大店','LALA Kitchen 新美式餐廳 交大店'],
        'C': ['十六區和風料理','江之戶日式料理','山口刺身ま丼飯','哈奇客韓式炸雞','遇見韓式精研燒肉','韓鍋人','『兩餐』韓國年糕火鍋','愛烤愛對囉','牛町日式碳火燒肉','一燒十味昭和園',],
        'D': ["馬來老爹","The Spice Shop Indian Cuisine","大馬人馬來西亞鄉味館","香港銅鑼灣","泰之味","MAS India Foods","娘家","印度私廚","168 Singapore Food","Tudo Bem 哩賀巴西小館"],
        'E': ['金之鄉QQ圓','三層山冰淇淋','學府生煎包','鐵三角碳烤吐司','CaSa CAFE千層蛋糕','立晉傳統豆花','吳記蔥蔬餅','小舞台烘焙坊','招牌豬肉夾饃','小洞天香腸米腸'],
    },
    "成大": {
        "A": ['開元紅燒𩵚魠魚羹','家咖哩 台南成大店','老友小吃','成大歲月美食坊','添福麵館','加依軒（+1）小籠湯包成大店','小豬很忙蔬果滷味-台南成大勝利店','一點刈包','紅樓小館','來呷飯川食堂（成大店）','小茂屋'],
        'B': ['X Dining艾克斯義式餐酒館','庫肯花園餐廳','轉角餐廳 Corner Steak House','飛饗義法典藏料理','圓頂西餐廳','亞芙英式餐廳','陶板屋 台南勝利店','胖廚西式餐廳','Is義式餐廳'],
        'C': ['大韓名鍋韓式料理','韓佶育樂店','韓朝韓式料理','高麗館小吃店','大長今 韓國先生','韓文閣''井選日式定食','小碗和食','樂品屋','豚讚日式豬排','日船章魚小丸子'],
        'D': ["日勿墨食－墨西哥餐廳","Cocina Quesadilla","米藍花巷異國料理","MAP LAB Kitchen 異國料理 體驗廚房","品味異國料理","長鼻子泰式咖哩·南洋火鍋餐廳－台南成大店","亞風異國料理店","印度皇宮Indian Palace(南紡店)","Selamat datang 馬來西亞料理","也是瑪莉","泰好泰式美食館"],
        'E': ['山田雞蛋酥','泰式小煎餅','三元坊','勝利早點','黑工號嫩仙草','紅記早點','波美斯薯條','啾啾法式甜點','晞果甜點工作室','ㄆㄤㄆㄤ雞蛋糕'],
    }

}
for category in categoryDict:
    queryString = queryString + f'{category}: {categoryDict[category]}\n'

schools = ''
for school in restaurantDict:
    schools += f'{school} '

def getCategory(schoolRestaurant):
    choice = input(f"想要吃哪種風格的料理呢?\n{queryString}\n")
    restaurantList = schoolRestaurant.get(choice)
    return restaurantList

while True:
    school = input(f"你要找哪一所學校的料理?\n(目前開放 {schools})\n輸入0離開\n")
    if school == "0":
        print("掰掰\n")
        break

    schoolRestaurant = restaurantDict.get(school)

    if schoolRestaurant:
        restaurantList = getCategory(schoolRestaurant)
        while not restaurantList:
            print("嗚嗚~請選已有的選項~其他風格開發中")
            restaurantList = getCategory(schoolRestaurant)

        print(f"你可以試試看 {random.choice(restaurantList)}\n")
        # for r in restaurantList:
        #     print(r, end=" ")
        # print('\n')

    else:
        print("你只能選擇輸入 政大 或 台大")
    
    