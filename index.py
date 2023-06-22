
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.chrome.service import service
from vs4 import BeautifulSoup
from urllib.request import urlopen
import datetime

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.weather.go.kr/w/weather/forecast/short-term.do")
bsObject = BeautifulSoup(driver.page_source, 'html.parser')

date=datetime.datetime.now().strifime("%y-%m-%d")

for item in bsObject.find_all('ul', {'data-date':date}):
    data=item.select('li')

#시간
time = data[0].contents[1].string

#날씨
weather = data[1].contents[1].string

#기온
temperature=data[2].contents[1].contents[0].string

#체감온도 
sensible_temperature=data[3].contents[1].string
#강수확률
probability_precipitation=data[5].contents[1].string

#바람
wind=data[6].contents[1].string +''+data[6].contents[2].contents[0].string + data[6].contents[2].contents[1].string

print(time, weather, temperature , sensible_temperature, probability_precipitation, wind)