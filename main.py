import requests
from bs4 import BeautifulSoup
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/54.0.2840.71 Safari/537.36 '
}
url = 'https://www.amazon.in/s?k=mobile+phones+under+20000&crid=X52ZJXN5V8HD&sprefix=mobile+phones+under+%2Caps%2C277' \
      '&ref=nb_sb_ss_ts-doa-p_6_20 '
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")

title = soup.find_all(class_='a-size-medium a-color-base a-text-normal')
title = [x.text for x in title]
print(title)

price = soup.find_all(class_="a-price-whole")
price = [i.text for i in price]
print(price)

image = soup.find_all(class_="s-image")
image_list=[]
for i in image:
    try:
        image_list.append(i['src'])
    except:
        image_list.append(None)
print(list(set(image_list)))

rating = soup.find_all(class_='a-icon-alt')
rating = [i.text[:4] for i in rating]
print(rating)

fields = ['Model', 'Price', 'Image']
with open('Output.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([title, price,image])
for i in range(2, 20):
        next_page = soup.select(f"a[aria-label='Go to page {i}']")
        next_page = [x['href'] for x in next_page]
        print(next_page)
        # print(f'https://www.amazon.in{next_page[0]}')

