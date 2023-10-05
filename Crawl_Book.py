import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

browser = webdriver.Edge()

# Collecting Catagories URL
def Book_list():
    # Get URL and open Edge
    url = 'https://www.fahasa.com/sach-trong-nuoc.html'
    browser.get(url)

    # Save Source code in var: 'Page_Source'
    Page_Source = browser.page_source
    Source = BeautifulSoup(Page_Source, 'html.parser')

    # Waiting 2 second
    sleep(2)
    
    # Create List
    Book_categories = []
    List = Source.find('ol', class_= 'm-child-category-list m-expandable-filter')
    if List is not None:  # Check if List is found
        for item in List.find_all('a'):
            Name = item.get_text().strip()
            URL = item['href']
            Book_categories.append({'Name': Name, 'URL': URL})
    return Book_categories

# Collecting Product URL
def Product_URL():

    # Create list
    Product_url = []

    # Output Catagories URL
    book_categories = Book_list()
    for category in book_categories:
        browser.get(category['URL'])
        sleep(2)
        Page_Source = browser.page_source
        Source = BeautifulSoup(Page_Source, 'html.parser')
        Source = Source.find('ul', class_ = 'products-grid fhs-top')
        for item in Source.find_all('h2', class_ = 'product-name-no-ellipsis p-name-list'):
            URL = item.find('a')['href']
            Product_url.append({'Catagory': category['Name'], 'URL': URL})
    return Product_url


# Saving Data By CSV
with open('DataFasaha.csv', "w", newline="", encoding="utf-8") as file:
    headers = ['ID', 'Name', 'Catagory', 'Price', 'Cover Book', 'Author', 'Suppliers', 'Publisher', 'Description']
    writer = csv.DictWriter(file, delimiter=',', lineterminator='\n', fieldnames=headers)
    writer.writeheader()

    # Output Product URL
    Book_Details = Product_URL()
    for details in Book_Details:
        browser.get(details['URL'])
        sleep(2)
        Page_Source = browser.page_source
        Source = BeautifulSoup(Page_Source, 'html.parser')

        # Collecting Name Production
        Name = Source.find('h1').get_text().strip()
        if Name is None:
            Name = None

        # Collecting Cover Book
        Cover_Book = Source.find('img', class_ = 'swiper-lazy swiper-lazy-loaded')['src']
        if Cover_Book is None:
            Cover_Book = None

        # Collecting Price Production
        Old_Price = Source.find('p', class_ = 'old-price')
        if Old_Price is not None:
            Price = Old_Price.find('span', class_ = 'price').get_text().strip().replace('\xa0', '')
        else:
            Price_current = Source.find('p', class_ = 'special-price')
            Price = Price_current.find('span', class_ = 'price').get_text().strip().replace('\xa0', '')

        # Collecting Details Product
        Details = Source.find('table', class_ = 'data-table table-additional')

        # Collecting ID Product
        ID_Product = Details.find('td', class_ = 'data_sku').get_text().strip()
        if ID_Product is None:
            ID_Product = None

        # Collecting Suppliers
        Pos1_Suppliers = Details.find('td', class_ = 'data_supplier')
        Pos2_Suppliers = Details.find('td', class_ = 'data_supplier_list')
        if Pos1_Suppliers is not None:
            Name_Suppliers = Pos1_Suppliers.get_text().strip()
        elif Pos2_Suppliers is not None:
            Name_Suppliers = Pos2_Suppliers.get_text().strip()
        else:
            Name_Suppliers = None
        

        # Collecting Auther
        Author = Source.find('td', class_ = 'data_author')
        if Author is None:
            Name_Author = None
        else: Name_Author = Author.get_text().strip()

        # Collecting Publisher
        Publisher = Source.find('td', class_ = 'data_publisher')
        if Publisher is None:
            Name_Publisher = None
        else: Name_Publisher = Publisher.get_text().strip()

        
        # Collecting Product Description
        Product_Description = []
        tmp = Source.find('div', id = 'desc_content')
        for Description in tmp.find_all('p', style = 'text-align: justify;'):
            try:
                Des = Description.text.strip().replace('\xa0', ' ')
                Product_Description.append(Des)
            except AttributeError:
                pass
        writer.writerow({headers[0]:ID_Product, headers[1]:Name, headers[2]:details['Catagory'], headers[3]:Price, headers[4]:Cover_Book,
                        headers[5]:Name_Author, headers[6]:Name_Suppliers, headers[7]:Name_Publisher, headers[8]:Product_Description})
        
# close browser
browser.quit()