from codecs import ignore_errors
from selenium import webdriver
import time
from selenium.webdriver.edge.options import Options

# start web browser
#browser=webdriver.Chrome(executable_path='C:/path/to/chromedriver.exe')
#browser = webdriver.Chrome(ChromeDriverManager().install())
options = Options()
options.add_argument("--headless")
browser = webdriver.Edge(r'C:\Users\DELL\Downloads\softwares\edgedriver_win64\msedgedriver.exe', options = options)
# get source code
url = "http://liiofindia.org/in/cases/cen/INSC/2010/1004.html"
#url = "https://indiankanoon.org/doc/1563275/"
browser.get(url)

html = browser.page_source
time.sleep(2)
with open("SupremeCourt_2010_1004.html", "w", encoding='UTF-8') as f:
    f.write(html)

# close web browser
browser.close()