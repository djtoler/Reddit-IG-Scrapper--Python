# import requests
# from bs4 import BeautifulSoup as bs
# import io
 
# URL = 'https://www.geeksforgeeks.org/page/1/'
 
# req = requests.get(URL)
# soup = bs(req.text.encode('utf-8'), 'html.parser')
 
# titles = soup.find_all('div', attrs = {'class','head'})
 
# print(titles[3].text)

# filehandle = io.open('titles.txt', 'w', encoding='utf8')
# filehandle.write(soup.prettify())
# filehandle.close()


# import requests
# from bs4 import BeautifulSoup as bs
 
# URL = 'https://www.geeksforgeeks.org/page/'
 
# for page in range(1, 10):
 
#     req = requests.get(URL + str(page) + '/')
#     soup = bs(req.text.encode('utf-8'), 'html.parser')
 
#     titles = soup.find_all('div', attrs={'class', 'head'})
 
#     for i in range(4, 19):
#         if page > 1:
#             print(f"{(i-3)+page*15}: {titles[i].text}")
#         else:
#             print(f"{i-3}: " + titles[i].text)


# import requests
# from bs4 import BeautifulSoup as bs
 
# URL = ['https://www.geeksforgeeks.org','https://www.geeksforgeeks.org/page/10/']
 
# for url in range(0,2):
#     req = requests.get(URL[url])
#     soup = bs(req.text, 'html.parser')
 
#     titles = soup.find_all('div',attrs={'class','head'})
#     for i in range(4, 19):
#         if url+1 > 1:
#             print(f"{(i - 3) + url * 15}" + titles[i].text)
#         else:
#             print(f"{i - 3}" + titles[i].text)

# import requests
# from bs4 import BeautifulSoup as bs
# import io

 
# URL = 'https://www.youtube.com/watch?v=JPkgJwJHYSc'
# headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0'}

 
# req = requests.get(URL, headers=headers)
# soup = bs(req.text.encode('utf-8'), 'html.parser')
 
# # comments = soup.find_all('yt-formatted-string', attrs = {'class':'style-scope ytd-comment-renderer'})
# comments = soup.find_all('h1')

# print(comments) 
# # print(comments[0].text)

# filehandle = io.open('yt_comments-blockchain.txt', 'w', encoding='utf8')
# filehandle.write(soup.prettify())
# filehandle.close()

# !apt-get update
# !apt install chromium-chromedriver
# %pip install selenium
# !cp /usr/lib/chromium-browser/chromedriver /usr/bin

# from selenium import webdriver
# from selenium.webdriver.common.by import By 
# from selenium.webdriver.common.keys import Keys 
# import time 

# comment_array = []
# driver = webdriver.Chrome()
# driver.get('https://www.youtube.com/watch?v=qOVAbKKSH10')
# body = driver.find_element(by=By.TAG_NAME, value='body')
# for i in range(10):
#     body.send_keys(Keys.END)
#     time.sleep(2)
# print('done scrolling')
# comment_file = open('yt_comments.txt', 'w', encoding='utf8')
# for comment in driver.find_elements(by=By.XPATH, value="//yt-formatted-string[@id='content-text']"):
#     comment_array.append(comment.text)
#     comment_file.write(comment.text + '\n')
#     comment_file.write('---\n')
# print('done writing comments')
# comment_file.close()
# driver.close()


import requests
from bs4 import BeautifulSoup


# url = 'https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html'
# reqs = requests.get(url)
# soup = BeautifulSoup(reqs.text, 'html.parser')

# urls = []
# for link in soup.find_all('a'):
# 	print(link.get('href'))

url = 'https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html'
reqs = requests.get(url)
soup = BeautifulSoup('<html><body><div class="awsui_drawer-content_lm6vo_1b2gu_154 awsui_navigation_lm6vo_1b2gu_242 awsui_navigation_1fj9k_avnjw_9"> ... </div></body></html', 'html.parser')
soup.find("div", {"class": "awsui_drawer-content_lm6vo_1b2gu_154 awsui_navigation_lm6vo_1b2gu_242 awsui_navigation_1fj9k_avnjw_9"})


urls = []
for link in soup.find_all('a'):
	print(link.get('href'))
#make a directory
#run scrapy startproject <projectname>
#cd into project
#run scrapy genspider countries <url To Scrape>
#run conda install ipython
#run scrappy shell

# create variables for each aws service, set equal to scrapy.Resquest(url="<url to crawl>")
