import time
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://flight.naver.com/')

# 가는 날 클릭
# browser.find_element_by_link_text('가는 날').click()
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()
time.sleep(5)
# browser.find_elements_by_link_text('30')[0].click()
# browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[2]/button').click()

# 오는 날
# browser.find_elements_by_link_text('5')[1].click()
# browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[1]/button').click()


# 제주도 클릭
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]/b').click()
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/button[1]').click()
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/div/button[2]/span/i[1]').click()

# 항공권 검색 클릭
browser.find_element_by_link_text('항공권 검색').click()

try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')))
    print(elem.text)
except:
    print("실패했어요")

# 첫 번째 결과 출력
# elem = browser.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')
# print(elem.text) # element 내에 있는 text 부분을 출력

time.sleep(5)
browser.quit()