from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://search.naver.com/search.naver?query=날씨')
# pprint(html.text)

soup = bs(html.text,'html.parser')

data1 = soup.find('div',{'class':'detail_box'})
#pprint(data1)

data2 = data1.findAll('dd')
# pprint(data2)

data3 = soup.find('div',{'class':'info_list'})
#pprint(data3)

data4 = data3.findAll('span')
#pprint(data4)

fine_dust = data2[0].find('span',{'class':'num'}).text
print(fine_dust)

ultra_fine_dust = data2[1].find('span',{'class':'num'}).text
print(ultra_fine_dust)

hot_cold = data4[0].find('span',{'class':'num'}).text
print(hot_cold)

feel_hot_cold = data4[1].find('span',{'class':'num'}).text
print(feel_hot_cold)