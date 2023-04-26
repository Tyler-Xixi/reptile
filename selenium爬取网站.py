import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

web = Chrome()
url = "https://www.lagou.com/"
web.get(url)
time.sleep(0.5)

adress = web.find_element_by_xpath('//*[@id="changeCityBox"]/ul/li[4]/a')
adress.click()
time.sleep(0.5)

serch = web.find_element_by_xpath('//*[@id="search_input"]').send_keys('python', Keys.ENTER)
time.sleep(0.5)

web.find_element_by_xpath('//*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[1]/a/h3').click()
web.switch_to.window(web.window_handles[-1])
tx = web.find_element_by_xpath('//*[@id="job_detail"]/dd[2]/div').text
print(tx, '\n')
web.close()
time.sleep(0.5)

web.switch_to.window(web.window_handles[0])
tx = web.find_element_by_xpath('//*[@id="s_position_list"]/ul/li[1]').text
print(tx)
time.sleep(0.5)
web.close()
