html = input("請輸入 html 的內容，或是輸入 default 由預設檔案示範")
default = """<div class="carosel">
        <div data-pagination='{"el": ".swiper-pagination"}' class="swiper-container swiper-init m-0 swipermultiple featured-restaurant">
            <div class="swiper-pagination"></div>
            <div class="swiper-wrapper">
                <div class="swiper-slide">
                    <label for="file1">
                        <img src="{% static 'images/add.png' %}" alt="" style="width:300px" id="pic1">
                    </label>
                </div>
                <div class="swiper-slide">
                    <label for="file2">
                        <img src="{% static 'images/add.png' %}" alt="" style="width:300px" id="pic2">
                        </label>
                    </div>
                <div class="swiper-slide">
                        <label for="file3">
                    <img src="{% static 'images/add.png' %}" alt=""  style="width:300px" id="pic3">
                            </label>
                </div>
                <div class="swiper-slide">
                        <label for="file4">
                    <img src="{% static 'images/add.png' %}" alt=""  style="width:300px" id="pic4">
                            </label>
                </div>
            </div>
        </div>
    </div>"""
if html == "default":
    print(default)
    html = default
    

start = 0            
tagList = []
while(start<len(html)):
    start = html.index('<', start)
    elementEnd = html.index('>', start)
    if html[start+1] == "/":
        finding = False
        for i in html[start:elementEnd]:
            if i.isspace():
                tag = html[start+2:i]
                finding = True
                break
        if not finding:
            tag = html[start+2:elementEnd]
        
       
        if tagList[-1] == tag:
            del tagList[-1]
        else:
            print(f"Wrong start from index {start} inconsist with {tag}, should be {tagList[-1]}")
            print(html[start:])
            break
    else:
        if (html[start+1:start+4] == 'img') or (html[start+1:elementEnd+4] == 'br'):
                pass
        else:
            count = 0
            finding = False
            for i in html[start:elementEnd]:
                if i == " ":
                    tag = html[start+1:start+count]
                    finding = True
                    break
                count = count + 1
            if not finding:
                tag = html[start+1:elementEnd]
        
            tagList.append(tag)
            
    start = elementEnd + 1
            
print("="*50)
if not tagList:
    print("Success valid html")
    
            