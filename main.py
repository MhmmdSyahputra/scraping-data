from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
import pandas as pd

# Inisialisasi browser
browser = webdriver.Chrome(executable_path='path/to/chromedriver')

# LINK --------------------------
alexandre_christie = 'https://www.radatime.co.id/jam-tangan-alexandre-christie'
seiko = 'https://www.radatime.co.id/jam-tangan-seiko'
luminox = 'https://www.radatime.co.id/jam-tangan-luminox'
bonia = 'https://www.radatime.co.id/jam-tangan-bonia'
alba = 'https://www.radatime.co.id/jam-tangan-alba'
casio = 'https://www.radatime.co.id/jam-tangan-casio'
adidas = 'https://www.radatime.co.id/jam-tangan-adidas'
rado = 'https://www.radatime.co.id/jam-tangan-rado'
aries_gold = 'https://www.radatime.co.id/jam-tangan-aries-gold'
tissot = 'https://www.radatime.co.id/jam-tangan-tissot'
aigner = 'https://www.radatime.co.id/jam-tangan-aigner'
suunto = 'https://www.radatime.co.id/jam-tangan-suunto'
garmin = 'https://www.radatime.co.id/jam-tangan-garmin'
expedition = 'https://www.radatime.co.id/jam-tangan-expedition'
fila = 'https://www.radatime.co.id/jam-tangan-fila'

# Kunjungi halaman

browser.get(suunto)


time.sleep(5)

html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
elements = soup.find_all(class_='product-item-img pt-2 px-2')


# brand = clear
# gender = clear 
# digital/analog = clear
# harga kelipatan 500k = clear
# berat = clear
# tebal = clear
# bahan case = clear
# warna case  = clear 
# ketahanan air = clear
# garansi = clear

brand_list = []
gender_list = []
tipe_list = []
price_list = []
berat_list = []
tebal_list = []
bahan_list = []
warna_list = []
ketahananAir_list = []
garansi_list = []

# Loop through all elements
for element in elements:
    # Get detail link
    detail_link = element.a['href']
    # Get detail page
    browser.get(detail_link)
    # time.sleep(5)
    soup_detail = BeautifulSoup(browser.page_source, 'html.parser')

    # product name--------------
    product_name = soup_detail.find(class_='mb-0 pr-5 product-item-title').get_text()

    # price --------------
    price = soup_detail.find_all("span", class_="special_price")[2].get_text()

    # in descripsi ------------
    # tebal,bahan,warna ------------------
    table1 = soup_detail.find_all("table", class_="table-bordered")[1]
    rows1 = table1.find_all("tr")

    # tipe : digital/analog -------
    table2 = soup_detail.find_all("table", class_="table-bordered")[2]
    rows2 = table2.find_all("tr")

    # berat -------
    table3 = soup_detail.find_all("table", class_="table-bordered")[5]
    rows3 = table3.find_all("tr")


    # berat,garansi dan ketahanan air -------
    for row in rows3:
        th = row.find("th").get_text()
        if th == "Berat":
            berat = row.find("td").get_text()
        if th == "Ketahanan Air":
            water = row.find("td").get_text().split("\n")[1]
        if th == "Warranty":
            garansi = row.find("td").get_text()


    # tipe : digital/analog ------------
    for row in rows2:
        th = row.find("th").get_text()
        if th == "Dial Type":
            tipe = row.find("td").get_text().split("\n")[1]
    #         print(tipe)

    # tebal,bahan,warna ------------------
    for row in rows1:
        th = row.find("th").get_text()
        if th == "Tebal":
            tebal = row.find("td").get_text()
        if th == "Bahan Case":
            bahan = row.find("td").get_text().split("\n")[1]
        if th == "Warna Case":
            warna = row.find("td").get_text().split("\n")[1]
    
    

    #gender dan tebal--------------
    all = soup_detail.find("p", class_="mb-0", style="font-size: 16px;").get_text()
    text_list = all.split(" - ")
    gender = text_list[0]
    text_list = text_list[1].split(" (")
    tebal = text_list[1].replace(")","")

    # cetak semua nya ---------------------
    # print("Name: ", product_name)
    # print("gender: ", gender)
    # print("tebal: ", tebal)
    # print("price: ", price)
    # print("bahan: ", bahan)
    # print("warna: ", warna)
    # print("berat: ", berat)
    # print("garansi: ", garansi)
    # print("ketahanan air: ", water)
    print('\n')
    brand_list.append(product_name)
    gender_list.append(gender)
    tebal_list.append(tebal)
    price_list.append(price)
    bahan_list.append(bahan)
    warna_list.append(warna)
    berat_list.append(berat)
    garansi_list.append(garansi)
    ketahananAir_list.append(water)


# Create dataframe from product list
df = pd.DataFrame(columns=['Brand', 'Gender', 'Tebal', 'Harga', 'Bahan', 'Warna', 'Berat', 'Garansi', 'Ketahanan Air'])

df['Brand'] = brand_list
df['Gender'] = gender_list
df['Tebal'] = tebal_list
df['Harga'] = price_list
df['Bahan'] = bahan_list
df['Warna'] = warna_list
df['Berat'] = berat_list
df['Garansi'] = garansi_list
df['Ketahanan Air'] = ketahananAir_list

# Save dataframe to excel
df.to_excel("pert14/suunto.xlsx")

# Keluar dari browser
browser.quit()

