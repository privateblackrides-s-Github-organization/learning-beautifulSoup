from bs4 import BeautifulSoup
import requests
f = file('Phone_details.txt', 'w') # opened file in Phone_details.txt in write mode

url = 'http://www.flipkart.com/mobiles/pr?sid=tyy,4io&otracker=ch_vn_mobile_filter_Top%20Brands_All' # url to scrap
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data) #make soup
interestingDiv = soup.find_all('div', class_ = 'product-unit unit-4 browse-product new-design ') # Details we want are in div with this css class
for i in interestingDiv:
    productName = i.find('a', class_ = 'fk-display-block')
   # f.write(productName['title']) the attribute title is taken
   # f.write(productName['href']) the attribute href is taken
    price = i.find('div', class_ = 'pu-price').span
   # f.write(price.string) # Navigable string of the tag
    f.write("{0} {1}".format(productName['title'].ljust(73), price.string.ljust(15))) 
    f.write(productName['href'])
    f.write('\n')
