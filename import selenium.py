from selenium import webdriver
from selenium.webdriver.commom.by import By


options = webdriver.ChromeOptions()

# headless 옵션 설정
options.add_argument('headless')
options.add_argument("no-sandbox")
# 브라우저 윈도우 사이즈
options.add_argument('window-size=1920x1080')

# 사람처럼 보이게 하는 옵션들
options.add_argument("disable-gpu")   # 가속 사용 x
options.add_argument("lang=ko_KR")    # 가짜 플러그인 탑재
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 이름 설정

# 드라이버 위치 경로 입력
driver = webdriver.Chrome(r'C:\Users\82104\기상청날씨\chromedriver.exe', options=options)

driver.get('https://naver.com')
driver.implicitly_wait(3)
driver.get_screenshot_as_file('capture_naver.png')    # 화면캡처

driver.quit() # driver 종료