import time
from tkinter.tix import Tree
from urllib.parse import ParseResultBytes
from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()

browser.get('https://shopping.naver.com/home/p/index.naver')

# '무선마우스' 입력 
browser.find_element_by_xpath('//*[@id="_verticalGnbModule"]/div/div/div[2]/div/div[2]/form/fieldset/div/input').send_keys('무선마우스')

# 검색 버튼 클릭
browser.find_element_by_xpath('//*[@id="_verticalGnbModule"]/div/div/div[2]/div/div[2]/form/fieldset/div/button[2]').click()
# enter 도 가능 

# 스크롤

# 1. 지정한 위치로 스크롤 내리기 (모니터 해당도 1080 위치로 스크롤 내리기)
# browser.execute_script('window.scrollTo(0, 1080)')
# browser.execute_script('window.scrollTo(0, 2080)')

# 2. 화면 가장 아래로 스크롤 내리기
# browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')

# 3. 동적 페이지에 대해서 마지막까지 스크롤 반복 수행
interval = 2 # 2초에 한번씩 스크롤 내리기

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script('return document.body.scrollHeight')

# 반복 수행
while True:
    # 스크롤을 화면 가장 아래로 내림
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    # 페이지 로딩 대기
    time.sleep(interval)
    # 현재 문서 높이 가져와서 저장
    curr_height = browser.execute_script('return document.body.scrollHeight')
    if curr_height == prev_height: # 직전 높이와 같으면, 높이 변화가 없으면 
        break # 반복문 탈출 (모든 스크롤 동작 완료)

    prev_height = curr_height

# 맨 위로 올리기
browser.execute_script('window.scrollTo(0, 0)')

time.sleep(5)

browser.quit()