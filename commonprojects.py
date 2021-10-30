''' Price Scraper for Common Projects '''

from urllib import request
import bs4


''' dictionary of stores '''

END='https://www.endclothing.com/us/common-projects-original-achilles-low-1528-0506.html?fresh=true'

Farfetch='https://www.farfetch.com/shopping/men/common-projects-achilles-lace-up-sneakers-item-13838256.aspx'

Tres='https://tres-bien.com/common-projects-original-achilles-low-white-1528-0506-fw21'

Porter='https://www.mrporter.com/en-us/mens/product/common-projects/shoes/low-top-sneakers/original-achilles-leather-sneakers/3024088872901549'

SSENSE='https://www.ssense.com/en-us/men/product/common-projects/white-original-achilles-low-sneakers/7707471'

prices = {
    'END':'pdp__details__final-price',  #id
    'Farfetch':'priceInfo-original',    #data-tstid
    'Tres':'price',                     #class
    #'Porter':
    'SSENSE':'pdpRegularPriceText'      #id
}

header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"}

async def get_prices():
    str1 = ""
    str2 = ""
    str3 = ""

    try:
        with request.urlopen(END) as response:
            
            block = response.read()

            soup = bs4.BeautifulSoup(block, 'html.parser')

            str1 = 'END Price:' + soup.find_all(id=prices['END'])[0].text
            print(str1)
    except IndexError:
        str1 = 'END Sold out'
        print(str1)
        pass
           

    try:
        with request.urlopen(request.Request(SSENSE,headers=header)) as response:
            
            block = response.read()

            soup = bs4.BeautifulSoup(block, 'html.parser')

            str2 = 'SSENSE Price:' + soup.find_all(id=prices['SSENSE'])[0].text.strip('\n')
            print (str2)
    except IndexError:
        str2 = 'SSENSE Sold out'
        print(str2)
        pass



    try:
        with request.urlopen(Farfetch) as response:
            
            block = response.read()

            soup = bs4.BeautifulSoup(block, 'html.parser')

            str3 = 'Farfetch Price:' + soup.find_all(attrs={'data-tstid':prices['Farfetch']})[0].text
            print(str3)
    except IndexError:
        str3 = 'Farfetch Sold out'
        print(str3)
        pass

    return(str1+"\n"+str2+"\n"+str3)

    # with request.urlopen(request.Request(Porter,headers=header)) as response:
    # #with request.urlopen(Porter) as response:

    #     block = response.read()

    #     soup = bs4.BeautifulSoup(block, 'html.parser')

    #     print(soup[0:40])
    #     #texts = soup.find('span', class_='PriceWithSchema9__value PriceWithSchema9__value--details')

    #     print(soup.find_all(class_="RecommendationsProducts84__header")[0].text)

    #     #lines = [span.get_text() for span in texts]

    #     #print(texts)

    #     #print('Mr.Porter Price:', soup.find_all())

# print(get_prices())