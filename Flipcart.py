from bs4 import BeautifulSoup
soup = BeautifulSoup(open('hell.html'))
interestingDiv = soup.find_all('div', class_ = 'product-unit unit-4 browse-product new-design ')
for i in interestingDiv:
    productName = i.find('a', class_ = 'fk-display-block')
    print(productName['title'])
    print(productName['href'])
    price = i.find('div', class_ = 'pu-price').span
    print(price.string)
print len(interestingDiv)
