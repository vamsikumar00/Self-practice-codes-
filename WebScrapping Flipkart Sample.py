# Import section
import requests
import pandas
from bs4 import BeautifulSoup

response=requests.get("https://www.flipkart.com/search?q=iphone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_1_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_1_na_na_na&as-pos=1&as-type=RECENT&suggestionId=iphone%7CMobiles&requestId=e18c18fd-103a-42b6-b5e6-3cba05524f4f&as-searchtext=i")
#print(response)
soup=BeautifulSoup(response.content,'html.parser')
#print(soup)
names=soup.find_all('div',class_="_4rR01T")
name=[]
for i in names[20]:
    d=i.text
    name.append(d)
print(name)    