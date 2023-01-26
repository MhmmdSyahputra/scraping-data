from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
import pandas as pd

# Inisialisasi browser
browser = webdriver.Chrome(executable_path='path/to/chromedriver')

# LINK --------------------------
index = 'https://www.radatime.co.id'

# Kunjungi halaman

browser.get(index)
time.sleep(5)

soup = BeautifulSoup(browser.page_source, 'html.parser')
semua = soup.find_all(class_='wstliststy02 clearfix')[0]

links = semua.find_all('a', href=True)
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
# print('1')
for link in links:
    # print(link)
#     print('2')
    # if link['href'] == '/ariesgold':
        
    #     browser.get('https://www.radatime.co.id/jam-tangan-aries-gold')
    #     namefile = link['href']
    #     time.sleep(3)

    #     allPage = BeautifulSoup(browser.page_source, 'html.parser')

    #     elements = allPage.find_all(class_='product-item-img pt-2 px-2')

    #     print('3')

    #     brand_list = []
    #     gender_list = []
    #     tipe_list = []
    #     price_list = []
    #     berat_list = []
    #     tebal_list = []
    #     bahan_list = []
    #     warna_list = []
    #     ketahananAir_list = []
    #     garansi_list = []

    #     for element in elements:
    #         detail_link = element.a['href']
    #         # Get detail page
    #         browser.get(detail_link)
    #         # time.sleep(5)
    #         soup_detail = BeautifulSoup(browser.page_source, 'html.parser')

    #         # product name--------------
    #         product_name = soup_detail.find(class_='mb-0 pr-5 product-item-title').get_text()

    #         # price --------------
    #         price = soup_detail.find_all("span", class_="special_price")[2].get_text()

    #         # in descripsi ------------
    #         # tebal,bahan,warna ------------------
    #         table1 = soup_detail.find_all("table", class_="table-bordered")[1]
    #         rows1 = table1.find_all("tr")

    #         # tipe : digital/analog -------
    #         table2 = soup_detail.find_all("table", class_="table-bordered")[2]
    #         rows2 = table2.find_all("tr")

    #         # berat -------
    #         table3 = soup_detail.find_all("table", class_="table-bordered")[5]
    #         rows3 = table3.find_all("tr")


    #         # berat,garansi dan ketahanan air -------
    #         for row in rows3:
    #             th = row.find("th").get_text()
    #             if th == "Berat":
    #                 berat = row.find("td").get_text()
    #             if th == "Ketahanan Air":
    #                 water = row.find("td").get_text().split("\n")[1]
    #             if th == "Warranty":
    #                 garansi = row.find("td").get_text()


    #         # tipe : digital/analog ------------
    #         for row in rows2:
    #             th = row.find("th").get_text()
    #             if th == "Dial Type":
    #                 tipe = row.find("td").get_text().split("\n")[1]
    #         #         print(tipe)

    #         # tebal,bahan,warna ------------------
    #         for row in rows1:
    #             th = row.find("th").get_text()
    #             if th == "Tebal":
    #                 tebal = row.find("td").get_text()
    #             if th == "Bahan Case":
    #                 bahan = row.find("td").get_text().split("\n")[1]
    #             if th == "Warna Case":
    #                 warna = row.find("td").get_text().split("\n")[1]
        
        

    #         #gender dan tebal--------------
    #         all = soup_detail.find("p", class_="mb-0", style="font-size: 16px;").get_text()
    #         text_list = all.split(" - ")
    #         gender = text_list[0]
    #         text_list = text_list[1].split(" (")
    #         tebal = text_list[1].replace(")","")

    #         brand_list.append(product_name)
    #         gender_list.append(gender)
    #         tebal_list.append(tebal)
    #         price_list.append(price)
    #         bahan_list.append(bahan)
    #         warna_list.append(warna)
    #         berat_list.append(berat)
    #         garansi_list.append(garansi)
    #         ketahananAir_list.append(water)

    #         print('\n')
    #         # cetak semua nya ---------------------
    #         print("Name: ", product_name)
    #         print("gender: ", gender)
    #         print("tebal: ", tebal)
    #         print("price: ", price)
    #         print("bahan: ", bahan)
    #         print("warna: ", warna)
    #         print("berat: ", berat)
    #         print("garansi: ", garansi)
    #         print("ketahanan air: ", water)
    # else:
    if link['href'] == 'https://www.radatime.co.id/jam-tangan-alexandre-christie':
        print(link['href'])

        browser.get(link['href'])
        namefile = link['href']
        time.sleep(3)

        allPage = BeautifulSoup(browser.page_source, 'html.parser')

        elements = allPage.find_all(class_='product-item-img pt-2 px-2')

        print('3')

       

        for element in elements:
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

            brand_list.append(product_name)
            gender_list.append(gender)
            tebal_list.append(tebal)
            price_list.append(price)
            bahan_list.append(bahan)
            warna_list.append(warna)
            berat_list.append(berat)
            garansi_list.append(garansi)
            ketahananAir_list.append(water)

            print('\n')
            # cetak semua nya ---------------------
            print("Name: ", product_name)
            print("gender: ", gender)
            print("tebal: ", tebal)
            print("price: ", price)
            print("bahan: ", bahan)
            print("warna: ", warna)
            print("berat: ", berat)
            print("garansi: ", garansi) 
            print("ketahanan air: ", water)
        
        print("Name: ", product_name)
        print("gender: ", gender)
        print("tebal: ", tebal)
        print("price: ", price)
        print("bahan: ", bahan)
        print("warna: ", warna)
        print("berat: ", berat)
        print("garansi: ", garansi) 
        print("ketahanan air: ", water)
    
        # Create dataframe from product list
        # Membuat tabel dengan kolom yang ditentukan
        df = pd.DataFrame({
            'Brand': brand_list,
            'Gender': gender_list,
            'Tipe': tipe_list,
            'Price': price_list,
            'Berat': berat_list,
            'Tebal': tebal_list,
            'Bahan': bahan_list,
            'Warna': warna_list,
            'Ketahanan Air': ketahananAir_list,
            'Garansi': garansi_list
        })

        # Menyimpan tabel ke dalam format excel
        df.to_excel('data.xlsx', index=False)