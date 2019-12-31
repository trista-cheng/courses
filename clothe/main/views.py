
import requests
import json


from bs4 import BeautifulSoup
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from google.cloud import vision
from google.cloud.vision import types

from .models import Clothes, Category, Color, ClothesByColor
ZODIAC = {
    "水瓶座": 10, "雙魚座": 11, "牡羊座": 0, "金牛座": 1, 
    "雙子座": 2, "巨蟹座": 3, "獅子座": 4, "處女座": 5, 
    "天秤座": 6, "天蠍座": 7, "射手座": 8, "摩羯座": 9
}
CITIES = ['台北', '基隆', '高雄', '屏東', '台中']

# Create your views here.
def showHome(request):

    if request.is_ajax():
        zodiac = request.GET['zodiac']
        num = ZODIAC[zodiac]
        url = f"http://astro.click108.com.tw/daily_{num}.php?iAstro={num}"
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        luckys = soup.find_all('div', {'class': 'LUCKY'}, recursive=True)
        luckyColor = luckys[1].text
        data = json.dumps({"luckyColor": luckyColor})
        return HttpResponse(data, 'application/json')
     
    zodiac = ZODIAC
    cities = CITIES
    colors = Color.objects.all()
    context = {'signs':zodiac, 'cities': cities, 'colors': colors}
    return render(request, 'main/index.html', context)
    #return render(request, 'main/Home.html')

def showClothes(request):
    gender = request.POST.get('gender')
    city = request.POST.get('city')
    color = Color.objects.get(pk=request.POST.get('color'))
    
    resp = requests.get('https://www.google.com/search?q=' + city + '天氣')
    soup = BeautifulSoup(resp.text, 'html.parser')
    temperature = soup.find_all('div', {"class": "BNeawe iBp4i AP7Wnd"})[1]
    degree = int(temperature.text[:-2])

    categories = Category.objects.filter(
        maxTemperature__gte=degree,
        minTemperature__lte=degree
    )
    clotheses = color.clothes_set.filter(
        clothes__category__in = categories,
        clothes__gender = gender
    )
    
    context = {'clotheses': clotheses}
    return render(request, 'main/ClothesList.html', context)
    #return render(request, 'main/Home.html')


# pazzo
def collectPazzo(request):
    domain = 'https://www.pazzo.com.tw/'

    # 針織衫 毛衣 F https://www.pazzo.com.tw/category/tops/knitwear 
    # https://www.pazzo.com.tw/category/bottoms/skirts 裙類
    # https://www.pazzo.com.tw/category/bottoms/longpants 長褲
    # 襯衫 https://www.pazzo.com.tw/category/tops/blouses
    category, created = Category.objects.get_or_create(name="襯衫")
    html = requests.get('https://www.pazzo.com.tw/category/tops/blouses').text
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all("ul", {'class': 'item-list'},recursive=True)[0]
    items = items.find_all('li', {'class':'item'}, recursive=True)
    for i in items:
        div = i.find('div', 'item__images')
        productUrl = domain + div.find('a').get('href')
        imgUrl = div.find('img').get('src')

        
        clothes = Clothes(
            gender='F',
            category=category,
            imgUrl=imgUrl,
            productUrl=productUrl,
        )
        clothes.save()


        singleHtml = requests.get(productUrl).text
        a = singleHtml.index("window.CustomMarketID") + 25
        b = singleHtml[a:].index("'")
        customId = singleHtml[a:a+b]
        detail = requests.get(
            'https://www.pazzo.com.tw/api/v1/market/content?CustomMarketID='
            + customId).text
        data = json.loads(detail)['Response']
        colorId = data['ColorID']
        colors = data['Colors']
        for c in colors:
            if c['ID'] == colorId:
                colorUrl = c['PintSizePictureUrl']
                break
        
        # singleSoup = BeautifulSoup(singleHtml, 'html.parser')
        # colorPart = singleSoup.find('div', 'product-color')
        # colorImg = colorPart.find('li', {'class': 'active'})
        # colorUrl = colorImg.find('img').get('src')


        client = vision.ImageAnnotatorClient()
        image = vision.types.Image()
        image.source.image_uri = colorUrl
        response = client.label_detection(image=image)
        labels = response.label_annotations
        
        for label in labels[:2]:
            color, created = Color.objects.get_or_create(
                name=label.description
            )
            colorset = ClothesByColor(
                clothes=clothes,
                color=color,
            )
            colorset.save()


    return redirect(reverse('main:showHome'))

