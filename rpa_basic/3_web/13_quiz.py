import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/')
browser.maximize_window()

browser.find_element_by_xpath('//*[@id="main"]/div[2]/div/div[1]/a[1]').click()

browser.find_element_by_xpath('//*[@id="topnav"]/div/div[1]/a[10]').click()

# browser.switch_to.frame('__uspapiLocator')

# browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[118]').click()
# browser.find_element_by_link_text('Contact Form').click() # 2개 이상의 링크 면 실패 가능 성
browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[text()="Contact Form"]').click() # 가장 좋은 방법
# browser.find_element_by_link_xpath('//*[@id="leftmenuinnerinner"]/a[contains(text(),"Contact")]') # 일부 텍스트 비교

# browser.find_element_by_xpath('//*[@id="fname"]').click()
first_name = "나도"
last_name = "코딩"
country = "Canada"
subject = "퀴즈 완료하였습니다."

browser.find_element_by_xpath('//*[@id="fname"]').send_keys(first_name)
browser.find_element_by_xpath('//*[@id="lname"]').send_keys(last_name)
# browser.find_element_by_xpath('//*[@id="country"]').click()
browser.find_element_by_xpath('//*[@id="country"]/option[text()="{}"]'.format(country)).click()
# browser.find_element_by_link_text('Canada').click()
browser.find_element_by_xpath('//*[@id="main"]/div[3]/textarea').send_keys(subject)

time.sleep(5)

browser.find_element_by_xpath('//*[@id="main"]/div[3]/a').click()

time.sleep(5)
browser.quit()