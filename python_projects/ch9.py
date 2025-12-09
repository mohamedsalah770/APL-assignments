#----------------------
#----  problem 1  -----
#----------------------
# import requests
# from bs4 import BeautifulSoup

# url = "https://example.com"
# response = requests.get(url)

# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, 'html.parser')
#     title = soup.title.string if soup.title else "No title found"
#     print(f"Page Title: {title}")
# else:
#     print(f"Failed to fetch page Status code: {response.status_code}")

#############################################################
#----------------------
#----  problem 2  -----
#----------------------

# import requests
# from bs4 import BeautifulSoup

# url = "https://example.com"
# response = requests.get(url)

# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, 'html.parser')
#     links = soup.find_all('a', href=True)
    
#     if links:
#         for link in links:
#             href = link['href']
#             print(href)
#     else:
#         print("No links found")
# else:
#     print(f"Failed to fetch page Status code: {response.status_code}")

#############################################################
#----------------------
#----  problem 3  -----
#----------------------

# from bs4 import BeautifulSoup

# html = """
# <table>
#     <tr><th>Name</th><th>Age</th></tr>
#     <tr><td>Alice</td><td>25</td></tr>
#     <tr><td>Bob</td><td>30</td></tr>
# </table>
# """

# soup = BeautifulSoup(html, 'html.parser')
# rows = soup.find_all('tr')

# for row in rows:
#     cells = [cell.get_text(strip=True) for cell in row.find_all(['th', 'td'])]
#     print(cells)
#######################################################################
#----------------------
#----  problem 4  -----
#----------------------

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time

# driver = webdriver.Chrome()  
# driver.get("https://www.google.com")

# search_box = driver.find_element(By.NAME, "q")
# search_box.send_keys("Python Web Scraping")
# search_box.send_keys(Keys.RETURN)

# time.sleep(2)  
# print("Page Title : ", driver.title)

# driver.quit()

#######################################################################
#----------------------
#----  problem 5  -----
#----------------------

# from bs4 import BeautifulSoup
# import csv

# html = """
# <ul>
#     <li>Apple</li>
#     <li>Banana</li>
#     <li>Cherry</li>
# </ul>
# """

# soup = BeautifulSoup(html, 'html.parser')
# fruits = [li.get_text(strip=True) for li in soup.find_all('li')]

# with open('fruits.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['Fruit'])  
#     for fruit in fruits:
#         writer.writerow([fruit])

# print("Saved to fruits.csv")
