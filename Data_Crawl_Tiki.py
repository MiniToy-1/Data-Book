from time import sleep
import csv
from selenium import webdriver
from bs4 import BeautifulSoup

# Open Browser
browser = webdriver.Chrome()
#Khoa
URL_Base = [['https://tiki.vn/nha-sach-tiki/c8322']]

def URL_Shop_All_Page():
    URL_All_Page = []
    URL_Shop = []

    # Open Browser
    URL_Page = URL_Base
    for i in range (0, 2):
        URL_Page = URL_Base[0][i]
        for j in range (1, 7):
            
            browser.get( URL_Page + str(j))
            sleep(3)
            Source = BeautifulSoup(browser.page_source, 'html.parser')
            URL = Source.find_all('a', class_ = 'styles__StoreLink-sc-w6zsy0-0 iRUTvq')

            # Save URL Shop one page in var: 'URL_Shop'
            for tmp in URL:
                links = tmp.get('href')
                URL_Shop.append(links)
            sleep(3)
    
    URL_Shop = list(set(URL_Shop))
    return URL_Shop 

def URL_Catagory():
    tmp = URL_Shop_All_Page()
    lengh_URL_Shop = len(tmp)
    Total = []

    # Open Browser
    for i in range (0, lengh_URL_Shop):
        Catagory_Data = []
        Catagory_URL = []
        Shop = []
        Shop_Name = []

        browser.get('https://tiki.vn' + str(tmp[i]))
        Source = BeautifulSoup(browser.page_source, 'html.parser')
        sleep(3)

        # Data Catagory
        Data = Source.find('div', title = "Thịt đông lạnh")
        if Data is not None:
            Title = Data.find_previous('a', class_ = "category child-category")

            # get URL and Title Catagory
            Title = Title['href'] 
            Data = Data.get_text().strip()
            if Title not in Catagory_URL:
                Catagory_URL.append(Title)
            if Data not in Catagory_Data:
                Catagory_Data.append(Data)
        

        # Data Catagory
        Data = Source.find('div', title = "Các loại thịt khác")
        if Data is not None:
            Title = Data.find_previous('a', class_ = "category child-category")
        
            # get URL and Title Catagory
            Title = Title['href'] 
            Data = Data.get_text().strip()
            if Title not in Catagory_URL:
                Catagory_URL.append(Title)
            if Data not in Catagory_Data:
                Catagory_Data.append(Data)
        

        # Data Catagory
        Data = Source.find('div', title = "Thịt heo, lợn")
        if Data is not None:
            Title = Data.find_previous('a', class_ = "category child-category")

            # get URL and Title Catagory
            Title = Title['href'] 
            Data = Data.get_text().strip()
            if Title not in Catagory_URL:
                Catagory_URL.append(Title)
            if Data not in Catagory_Data:
                Catagory_Data.append(Data)

        

        # Data Catagory
        Data = Source.find('div', title = "Trứng gà, vịt, cút")
        if Data is not None:
            Title = Data.find_previous('a', class_ = "category child-category")
        
            # get URL and Title Catagory
            Title = Title['href'] 
            Data = Data.get_text().strip()
            if Title not in Catagory_URL:
                Catagory_URL.append(Title)
            if Data not in Catagory_Data:
                Catagory_Data.append(Data)
        
        

        # Data Catagory
        Data = Source.find('div', title = "Thịt gà, vịt, chim")
        if Data is not None:
            Title = Data.find_previous('a', class_ = "category child-category")

            # get URL and Title Catagory
            Title = Title['href'] 
            Data = Data.get_text().strip()
            if Title not in Catagory_URL:
                Catagory_URL.append(Title)
            if Data not in Catagory_Data:
                Catagory_Data.append(Data)
        
        

        # Data Catagory
        Data = Source.find('div', title = "Thịt bò, bê")
        if Data is not None:
            Title = Data.find_previous('a', class_ = "category child-category")

            # get URL and Title Catagory
            Title = Title['href'] 
            Data = Data.get_text().strip()
            if Title not in Catagory_URL:
                Catagory_URL.append(Title)
            if Data not in Catagory_Data:
                Catagory_Data.append(Data)
        
        
        
        # Data Catagory
        Data = Source.find('div', title = "Thủy hải sản chế biến")
        if Data is not None:
            Title = Data.find_previous('a', class_ = "category child-category")

            # get URL and Title Catagory
            Title = Title['href'] 
            Data = Data.get_text().strip()
            if Title not in Catagory_URL:
                Catagory_URL.append(Title)
            if Data not in Catagory_Data:
                Catagory_Data.append(Data)

        

        # Data Catagory
        Data = Source.find('div', title = "Cá, hải sản đông lạnh")
        if Data is not None:
            Title = Data.find_previous('a', class_ = "category child-category")
        
            # get URL and Title Catagory
            Title = Title['href'] 
            Data = Data.get_text().strip()
            if Title not in Catagory_URL:
                Catagory_URL.append(Title)
            if Data not in Catagory_Data:
                Catagory_Data.append(Data)

        

        # Data Catagory
        Data = Source.find('div', title = "Thủy hải sản khác")
        if Data is not None:
            Title = Data.find_previous('a', class_ = "category child-category")

            # get URL and Title Catagory
            Title = Title['href'] 
            Data = Data.get_text().strip()
            if Title not in Catagory_URL:
                Catagory_URL.append(Title)
            if Data not in Catagory_Data:
                Catagory_Data.append(Data)

        

        # Data Catagory
        Data = Source.find('div', title = "Cá khô, tôm, mực khô")
        if Data is not None:
            Title = Data.find_previous('a', class_ = "category child-category")
        
            # get URL and Title Catagory
            Title = Title['href'] 
            Data = Data.get_text().strip()
            if Title not in Catagory_URL:
                Catagory_URL.append(Title)
            if Data not in Catagory_Data:
                Catagory_Data.append(Data)

        

        # Data Catagory
        Data = Source.find('div', title = "Tôm, cua, ghẹ, ốc")
        if Data is not None:
            Title = Data.find_previous('a', class_ = "category child-category")
        
            # get URL and Title Catagory
            Title = Title['href']
            Data = Data.get_text().strip()
            if Title not in Catagory_URL:
                Catagory_URL.append(Title)
            if Data not in Catagory_Data:
                Catagory_Data.append(Data)
        
        # Name Shop
        Name = Source.find('h1', class_ = "store-name")
        if Name is not None:
            Shop.append(Name.get_text().strip())

        for n in range(0, len(Shop)):
            for m in range (0, len(Catagory_Data)):
                tempt = Shop[n]
                Shop_Name.append(tempt)

        # Save in Var: Total
        for j in range (0, len(Catagory_Data)):
            Total.append([Catagory_Data[j], Catagory_URL[j], Shop_Name[j]])
    return Total

# Create file CSV:
with open('Data_Product.csv', 'w', newline = '', encoding='utf-8') as File_Output:
    headers = ['Shop Name', 'Catagory', 'Product Name', 'Sales Infomation', 'Price']
    writer = csv.DictWriter(File_Output, delimiter=',', lineterminator= '\n', fieldnames= headers)
    writer.writeheader()

    tmp = URL_Catagory()
    len_tmp = len(tmp)
    for i in range (0, len_tmp):
        Catagory = tmp[i][0]
        Name_Shop = tmp[i][2]
        URL_Product = []
        ID = 0

        # Save URL each product:
        for j in range (1, 3):
            browser.get(tmp[i][1] + '?page=' + str(j))
            sleep(3)
            Source = BeautifulSoup(browser.page_source, 'html.parser')
            URL = Source.find_all('a', class_ = "styles__ProductLink-sc-vqzx0s-0 hiCqSN")
            for link in URL:
                link = link.get('href')
                URL_Product.append(link)

        # Access to each product
        len_Product = len(URL_Product)
        for count in range (0, len_Product):
            browser.get('https://tiki.vn' + URL_Product[count])
            sleep(3)
            Source = BeautifulSoup(browser.page_source, 'html.parser')
            Info_Product = Source.find('div', class_='main')
            
            # Filter Data Product:
            if Info_Product:
                tmp_str = str('Đã bán ')
                
                Name = Info_Product.find('div', class_='styles__StyledProductName-sc-1xvsotp-3 rsaH').get_text().strip()
                Total = Info_Product.find('div', class_ = "styles__StyledReviewLine-sc-1xvsotp-2 cJVicW")

                if Total != None:
                    Total = Total.get_text().strip()
                    D = Info_Product.find('div', style = "display: flex; align-items: center;")
                    if D == None:
                        Total = Total.strip(tmp_str)
                    else:
                        Assess = D.find('div', style = "margin-left: 4px;").get_text().strip()
                        Total = Total.strip(Assess)
                        Total = Total.strip(tmp_str)
                else:
                    Sales = None

                A = Info_Product.find('div', class_ = "sale")
                B = Info_Product.find('div', class_ = "product-price has-discount")
                C = Info_Product.find('div', class_ = "product-price")

                if A is None:
                    if B is None:
                        if C is not None:
                            Price = C.find('div', class_ = "product-price__current-price").get_text().strip()
                    else:
                        Price = B.find('div', class_ = "product-price__list-price").get_text().strip()
                else:
                    Price = A.find('span', class_ = "list-price").get_text().strip()

                ID = ID + 1
                print("Sequence number: ", ID)
                print("Shop Name: ", Name_Shop)
                print("Catagory: ", Catagory)
                print("Product Name:", Name)
                print("Sales Information:", Total)
                print("Price: ", Price)
                print("\n")
                writer.writerow({headers[0]: Name_Shop, headers[1]: Catagory, headers[2]: Name, headers[3]: Total, headers[4]: Price})


# Close browser
browser.quit()
